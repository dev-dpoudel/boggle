from flask import Blueprint, session, request, Response, render_template
from flask_restful import Resource, Api
from .board import BoardGenerator

boggle_bp = Blueprint('board',
                      __name__,
                      static_folder='static',
                      template_folder='templates')
boggle = Api(boggle_bp)


class BoardProvider(Resource):
    """Setup Board for the session."""

    def get(self):
        """Get lattice keys and Initializes valid words for the session.

        Returns
        -------
        JSON
            Returns the lattice points fro the board.

        """
        layout = []
        generator = BoardGenerator()
        board = generator.board
        layout = [board[i:i+4] for i in range(0, len(board), 4)]
        session["board"] = board
        session["dictionary"] = generator.dictionary
        session["words"] = []
        return Response(response=render_template('index.html', board=layout))
        return {'keys': generator.board}


class WordProvider(Resource):

    def get(self):
        """Displays all valid answer to the current board.

        Returns
        -------
        JSON
            List of Correct words.

        """
        return {'words': session.get("dictionary", [])}


class GameProvider(Resource):
    """Provides Game Functions."""

    def get(self):
        """Get Results of the session.

        Returns
        -------
        JSON
            Dictionary with Toal Correct Answers.

        """
        words = session.get("words", [])
        results = {word: len(word) for word in words}
        values = results.values()
        total = sum(values)
        results["TotalGameCount"] = total
        return {"results": results}, 200

    def put(self):
        """Validate input word against the dictionary

        Parameters
        ----------
        word : string
            Input string min length 3.

        Returns
        -------
        JSON
            Json structure with information regarding marked words.

        """
        word = request.args["word"]
        dictionary = session.get("dictionary", [])
        words = session.get("words", [])
        success = False
        message = "Word not Valid"
        if word in dictionary:
            if word in words:
                message = "Word already selected"
            else:
                success = True
                message = None
                words.append(word)
                session["words"] = words

        return {"success": success, "message": message, "words": words}


boggle.add_resource(BoardProvider, '/keys')
boggle.add_resource(GameProvider, '/results', '/valid')
boggle.add_resource(WordProvider, '/list')

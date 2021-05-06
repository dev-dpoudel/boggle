from flask import session
from flask_classful import FlaskView
from .board import BoardGenerator


class BoardView(FlaskView):
    """Setup Board for the session."""
    #: Set Routing Prefix for URL
    route_prefix = "/board"
    #: Sets route base
    route_base = "/"

    def get(self):
        """Get lattice keys and Initializes valid words for the session.

        Returns
        -------
        JSON
            Returns the lattice points fro the board.

        """
        session.clear()
        generator = BoardGenerator()
        session["board"] = generator.board
        session["dictionary"] = generator.dictionary
        return {'keys': generator.board}

    def wordlist(self):
        """Displays all valid answer to the current board.

        Returns
        -------
        JSON
            List of Correct words.

        """
        return {'words': session.get("dictionary", [])}

    def results(self):
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

    def valid(self, word: str):
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
        # Initialize local variables
        success = False
        message = None
        # Get Session Data
        dictionary = session.get("dictionary", [])
        words = session.get("words", [])

        if word in dictionary:
            if word in words:
                message = "Word already selected"
            else:
                success = True
                words.append(word)
                session["words"] = words

        return {"success": success, "message": message, "words": words}

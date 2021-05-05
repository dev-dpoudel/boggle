import random
import string
import os

base_path = os.getcwd()


class BoardGenerator:
    ''' Provides word list selected as 4 * 4.
        List all possible dictionaries related to the objects
    '''

    # Assign list of Alphabets
    _letters = list(string.ascii_uppercase)

    def __init__(self, size: int = 4, minlength: int = 3):
        self._keys = random.choices(self._letters, k=size ** 2)
        self._dictionary = None
        self._size = size
        self._minlength = minlength

        # Load vocabulary from file
        path = os.path.join(base_path, "game", "words.txt")
        with open(path) as file:
            self._vocab = set(file.read().upper().split())

        # Set Prefix Vocabulary to be used
        self._prefix = set(p for word in self._vocab
                           for p in self.prefixes(word))

    @staticmethod
    def prefixes(word):
        "List of the initial sequence of a word, not the complete word."
        return [word[:i] for i in range(len(word))]

    def neighbors(self, i):
        N = self._size
        boundary = (i - N - 1,
                    i - N,
                    i - N + 1,
                    i - 1,
                    i + 1,
                    i + N - 1,
                    i + N,
                    i + N + 1)
        neighbour = [item for item in boundary if item in range(N**2)]
        return neighbour

    @property
    def board(self):
        return self._keys

    @property
    def vocab(self):
        return self._vocab

    @property
    def dictionary(self):
        "Find all the words on this Boggle board; return as a set of words."

        wordset = set()

        for i in enumerate(self.board):
            words = self.build_words(i, self._size, i[1], set())
            for word in words:
                wordset.add(word)

        self._dictionary = list(wordset)
        return self._dictionary

    def build_words(self, i, N, str_candidate='', visited_i=set(),
                    results=set()):
        """
        Find all words on this Boggle board, starting at position i with the
        current string candidate and with a list of already visited cells"""

        # Ensure the index was not visited previously
        if i[0] in visited_i:
            return results

        # Add the nodes to visited list
        visited_in_current_scope = set()
        visited_in_current_scope = visited_i.copy()
        visited_in_current_scope.add(i[0])

        # if the current string is a word:
        # add it to the result and keep on searching
        if str_candidate in self._vocab and len(str_candidate) >= self._minlength:  # noqa E501
            results.add(str_candidate)

        # get all neighbors of the current i_th
        neighbors_i = self.neighbors(i[0])
        # loop through all neighbors searching for words
        for n in neighbors_i:
            # if it is a word and respects rules add it
            if str_candidate + self.board[n] in self._vocab:
                if len(str_candidate + self.board[n]) >= self._minlength:
                    if n not in visited_in_current_scope:
                        results.add(str_candidate + self.board[n])
            # if it is in PREFIXES search for words
            if str_candidate + self.board[n] in self._prefix:
                t = (n, self.board[n])
                self.build_words(t, N, str_candidate +
                                 self.board[n], visited_in_current_scope)
        return results

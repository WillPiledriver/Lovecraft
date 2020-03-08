import nltk
import os
import random


class Lovecraft:
    def __init__(self, directory):
        self.books = dict()
        self.directory = directory
        self.tokens = dict()
        self.load_books()

    def load_books(self):
        f = []
        for (dirpath, dirnames, filenames) in os.walk(self.directory):
            f.extend(filenames)
            break

        for book in f:
            with open(self.directory.strip("\\") + '/' + book, mode="r", encoding="utf8") as file:
                self.books[book] = file.read().split("\n\n")
                self.tokens[book] = [nltk.pos_tag(nltk.word_tokenize(self.books[book][b])) for b in range(len(self.books[book]))]

    def generate_word_map(self, books=True):
        big_map = dict()
        for book, l in self.tokens.items():
            if books:
                big_map[book] = dict()
            for i in range(len(l)):
                for k, d in l[i]:
                    if books:
                        if d not in big_map[book]:
                            big_map[book][d] = list()
                        if k not in big_map[book][d]:
                            big_map[book][d].append(k)
                    else:
                        if d not in big_map:
                            big_map[d] = list()
                        if k not in big_map[d]:
                            big_map[d].append(k)
        return big_map

    def rand_chunk(self, book):
        return random.choice(self.tokens[book])

    def shuffle_chunk(self, m, chunk):
        new = ""
        ignore = ["NNP", ",", ".", "IN", "PRP$", "WP", "‘‘", "PRP"]
        punc = [".", ",", "'", ":", "‘‘", "POS", "''"]
        for i in range(len(chunk)):
            try:
                punc_if = (" ", "")[chunk[i][1] in punc or i == 0]
                if chunk[i][1] not in ignore:
                    new += punc_if + random.choice(m[chunk[i][1]])
                else:
                    new += punc_if + chunk[i][0]
            except KeyError:
                new += punc_if + chunk[i][0]
                continue
        return new

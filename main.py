import collections.abc
import re
import csv


class CACMDocument:
    """
    Represent a single CACM document with an ID, title and a summary.
    """

    def __init__(self, num, title, summary):
        self.I = num
        self.T = title
        self.W = summary

    def __str__(self):
        return str(self.I) + '/ ' + self.T + '\n' + self.W

    def get_title(self):
        return self.T

    def get_document_number(self):
        return self.I

    def get_summary(self):
        return self.W


class CACMParser(collections.abc.Iterator):
    """
    Iterator which returns a CACMDocument on each call.
    """

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath) as f:
            file_content = f.read()
        self.documents = re.split(r'^\.I', file_content, flags=re.MULTILINE)[1:]

    def __next__(self):
        try:
            doc = self.documents.pop(0)
        except IndexError:
            raise StopIteration
        num_rest = doc.split('.T')
        I = int(num_rest[0])
        rest = num_rest[1].split('.B')
        title_summary = rest[0].split('.W')
        T = title_summary[0].strip(' \n').replace('\n', ' ')
        if len(title_summary) == 2:
            W = title_summary[1].strip(' \n').replace('\n', ' ')
        else:
            W = ''
        return CACMDocument(I, T, W)

    def __iter__(self):
        return self


class InverseFileReader:
    """
    CSV based Reader for an inverse file.
    """

    def __init__(self, filepath):
        self.path = filepath

    def get_document_words_frequencies(self, document_id):
        """
        Return a dict containing the words of a document with their frequencies.
        :param document_id: int representing ID of the document.
        :return: dict of words as keys and their frequencies as values in the selected document.
        """
        w_f = {}
        with open(self.path, newline='') as inv_file:
            inverse_file_reader = csv.reader(inv_file)
            for word_frequencies in inverse_file_reader:
                word = word_frequencies[0]
                frequency = float(word_frequencies[document_id])
                if frequency > 0:  # This word exists in this document
                    w_f[word] = frequency
        return w_f

    def get_word_documents_frequencies(self, word):
        """
        Return a list containing the frequencies of the word in each document.
        :param word: str representing the word.
        :return: list of floats.
        """
        with open(self.path, newline='') as inv_file:
            inverse_file_reader = csv.reader(inv_file)
            for word_frequencies in inverse_file_reader:
                if word_frequencies[0] == word:  # The line of the word has been found
                    return [float(x) for x in word_frequencies[1:]]

    def search_query_matching_score(self, query):
        docs_relevance = {}
        with open(self.path, newline='') as inv_file:
            inverse_file_reader = csv.reader(inv_file)
            for word_frequencies in inverse_file_reader:
                word = word_frequencies[0]
                if word in query:
                    frequencies = [float(x) for x in word_frequencies[1:]]
                    for doc_id in range(1, len(frequencies)+1):
                        try:
                            docs_relevance[doc_id] += frequencies[doc_id-1]
                        except KeyError:
                            docs_relevance[doc_id] = frequencies[doc_id-1]
        return docs_relevance


if __name__ == '__main__':
    import sys
    cacm = CACMParser(sys.argv[1])
    element = None
    print(next(cacm))
    for element in cacm:
        pass
    print(element)

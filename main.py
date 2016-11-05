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
        with open(filepath, newline='') as inv_file:
            inverse_file_reader = csv.reader(inv_file)
            self.words_frequencies = {}
            for word_frequencies in inverse_file_reader:
                self.words_frequencies[word_frequencies[0]] = [float(x) for x in word_frequencies[1:]]

    def get_document_words_frequencies(self, document_id):
        """
        Return a dict containing the words of a document with their frequencies.
        :param document_id: int representing ID of the document.
        :return: dict of words as keys and their frequencies as values in the selected document.
        """
        w_f = {}
        for word, frequencies in self.words_frequencies.items():
            frequency = frequencies[document_id-1]
            if frequency > 0:  # This word exists in this document
                w_f[word] = frequency
        return w_f

    def get_word_documents_frequencies(self, word):
        """
        Return a list containing the frequencies of the word in each document.
        :param word: str representing the word.
        :return: list of floats.
        """
        return self.words_frequencies[word]

    def search_query_matching_score(self, query):
        """
        Return a dict containing the matching score of each relevant document.
        :param query: list of str, each str is a word.
        :return: dict which its keys are the IDs of the documents and its values are the relevance of each document.
        """
        docs_relevance = {}
        for word in query:
            word_frequencies = self.get_word_documents_frequencies(word)
            for doc_id in range(1, len(word_frequencies)+1):
                try:
                    docs_relevance[doc_id] += word_frequencies[doc_id-1]
                except KeyError:
                    if word_frequencies[doc_id-1] > 0:
                        docs_relevance[doc_id] = word_frequencies[doc_id - 1]
        return docs_relevance


if __name__ == '__main__':
    import sys
    cacm = CACMParser(sys.argv[1])
    element = None
    print(next(cacm))
    for element in cacm:
        pass
    print(element)

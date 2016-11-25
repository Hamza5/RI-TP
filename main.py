import collections.abc
import re
from collections import Counter
import pickle
from math import *
import  itertools
from os.path import join, dirname

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


class InverseFileWriter:
    """
    Pickle based writer for an inverse file.
    """

    def __init__(self, cacm, inverse_file_name):
        """
        Generate an inverse file from a CACM reader.
        :param cacm: CACMParser instance.
        :param inverse_file_name: str representing the path of the inverse file.
        """
        self.inv_filename = inverse_file_name
        words_documents_frequencies = {}
        for document in cacm:
            document_words = self.document_frequencies(document)
            for word, frequency in document_words.items():
                if word not in words_documents_frequencies.keys():
                    words_documents_frequencies[word] = {}
                try:
                    words_documents_frequencies[word][document.get_document_number()] += frequency
                except KeyError:
                    words_documents_frequencies[word][document.get_document_number()] = frequency

        with open(self.inv_filename, "wb") as file:
            pickle.dump(words_documents_frequencies, file)

    @staticmethod
    def document_frequencies(cacmElem):
        normalized_title = QueryPreprocessing.normalize_simple(cacmElem.get_title())
        normalized_summary = QueryPreprocessing.normalize_simple(cacmElem.get_summary())
        all_text = normalized_title + ' ' + normalized_summary
        return Counter(QueryPreprocessing.tokenize_simple(all_text))

class TfIdfFileWriter:

    def __init__(self, cacm, TfIdf_name):
        self.cacm2 = CACMParser(cacm)
        self.cacm3 = CACMParser(cacm)
       
        self.nember_docs = len(list(self.cacm3))
        self.InverseFile = InverseFileWriter(self.cacm2, 'inv' + TfIdf_name+'.bin')

        with open('inv' + TfIdf_name+'.bin', 'rb') as inv_file:
            self.docs_words_frequencies = pickle.load(inv_file)
        self.Idf_filename = TfIdf_name
        d = {}
        for term in self.docs_words_frequencies.keys():
            d[term] = {}
            for doc in self.docs_words_frequencies[term]:
                d[term][doc] = (float(self.docs_words_frequencies[term][doc])/max(self.docs_words_frequencies[term].values()))*log10(float(self.nember_docs)/len(list(self.get_word_documents_frequencies(term)))+1)
                self.get_word_documents_frequencies(term)
        with open(self.Idf_filename, "wb") as file:
            pickle.dump(d, file)
    def get_word_documents_frequencies(self, word):
        assert isinstance(word, str)
        docs = {}
        for w in self.docs_words_frequencies.keys():
            for doc_id in self.docs_words_frequencies[w].keys():
                if w == word:
                    try:
                        docs[doc_id] += self.docs_words_frequencies[w][doc_id]
                    except KeyError:
                        docs[doc_id] = self.docs_words_frequencies[w][doc_id]
        return docs




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
    Pickle based reader for an inverse file.
    """

    def __init__(self, filepath):
        """
        Load the inverse file.
        :param filepath: str representing the path of the inverse file.
        """
        self.docs_words_frequencies = {}
        with open(filepath, 'rb') as inv_file:
            words_docs_frequencies = pickle.load(inv_file)
            for word in words_docs_frequencies.keys():
                for doc_id, frequency in words_docs_frequencies[word].items():
                    if doc_id not in self.docs_words_frequencies.keys():
                        self.docs_words_frequencies[doc_id] = {}
                    try:
                        self.docs_words_frequencies[doc_id][word] += frequency
                    except KeyError:
                        self.docs_words_frequencies[doc_id][word] = frequency
        self.word_regexp = re.compile(r'\b\w+\b')

    def get_documents_count(self):  # Number of documents in the inverse file.
        return len(self.docs_words_frequencies)

    def get_words_count(self):  # Number of words in the inverse file.
        return len(set(word for words_frequencies in self.docs_words_frequencies.values() for word in words_frequencies.keys()))

    def __len__(self):
        return self.get_words_count()

    def get_document_words_frequencies(self, document_id):
        """
        Return a dict containing the words of a document with their frequencies.
        :param document_id: int representing ID of the document.
        :return: dict of words as keys and their frequencies as values in the selected document.
        """
        assert isinstance(document_id, int)
        w_f = {}
        for word, frequency in self.docs_words_frequencies[document_id].items():
            try:
                w_f[word] += frequency
            except KeyError:
                w_f[word] = frequency
        return w_f

    def get_word_documents_frequencies(self, word):
        """
        Return a dict containing the frequencies of the word in each document.
        :param word: str representing the word.
        :return: dict of document IDs (int) as keys and the frequencies (float) as values.
        """
        assert isinstance(word, str)
        docs = {}
        for doc_id in self.docs_words_frequencies.keys():
            for w, frequency in self.docs_words_frequencies[doc_id].items():
                if w == word:
                    try:
                        docs[doc_id] += frequency
                    except KeyError:
                        docs[doc_id] = frequency
        return docs

    def search_query_matching_score(self, query):
        """
        Return a dict containing the matching score of each relevant document.
        :param query: str of words.
        :return: dict which its keys are the IDs of the documents and its values are the relevance of each document.
        """
        assert isinstance(query, str)
        docs_relevance = {}
        for word in QueryPreprocessing.tokenize_simple(QueryPreprocessing.normalize_simple(query)):
            word_frequencies = self.get_word_documents_frequencies(word)
            for doc_id in word_frequencies.keys():
                try:
                    docs_relevance[doc_id] += word_frequencies[doc_id]
                except KeyError:
                    if word_frequencies[doc_id] > 0:
                        docs_relevance[doc_id] = word_frequencies[doc_id]
        return docs_relevance

    def search_query_boolean(self, boolean_query):
        """
        Return a list of IDs of the relevant documents to a boolean query using the boolean search model.
        :param boolean_query: str representing the query.
        :return: list of IDs of the relevant documents.
        """
        assert isinstance(boolean_query, str)  # Type checking
        relevant_docs = []
        for doc_id in self.docs_words_frequencies.keys():
            relevant = eval(
                QueryPreprocessing.replace_boolean_operators(
                    re.sub(
                        self.word_regexp,
                        lambda word: str(word.group() in self.get_document_words_frequencies(doc_id)),
                        QueryPreprocessing.normalize_boolean(boolean_query)
                    )
                )
            )
            if relevant:
                relevant_docs.append(doc_id)
        return relevant_docs

    def search_query_vector(self, query, model):
        """
        Return a dict of documents IDs with the corresponding similarities.
        :param query: str representing the query.
        :param model: str representing which vector model is used.
        :return: dict whose its keys are the documents IDs and the values are the similarities.
        """
        assert isinstance(query, str)
        assert model in ('inner_product', 'dice', 'cos', 'jaccard')
        docs_relevance = {}
        query_words = set(QueryPreprocessing.tokenize_simple(QueryPreprocessing.normalize_simple(query)))
        for doc_id in self.docs_words_frequencies.keys():
            words_frequencies = self.get_document_words_frequencies(doc_id)
            similarity = len(set(words_frequencies.keys()) & query_words)
            if similarity > 0:
                docs_relevance[doc_id] = similarity
        if model == 'dice':
            for doc_id in docs_relevance.keys():
                docs_relevance[doc_id] = 2 * docs_relevance[doc_id] / (
                    len(query_words) + len(self.docs_words_frequencies[doc_id])
                )
        elif model == 'cos':
            for doc_id in docs_relevance.keys():
                docs_relevance[doc_id] /= len(query_words)**(1/2) * len(self.docs_words_frequencies[doc_id])**(1/2)
        elif model == 'jaccard':
            for doc_id in docs_relevance.keys():
                docs_relevance[doc_id] /= len(query_words) + len(self.docs_words_frequencies[doc_id])\
                                          - docs_relevance[doc_id]
        return docs_relevance


class QueryPreprocessing:
    """
    Contain set of static methods for normalization and tokenizing
    """

    eliminate_regexp = re.compile(r"[^\w'\s]+")
    eliminate_boolean_regexp = re.compile(r"[^\w'&|~()]+")
    token_simple_regexp = re.compile(r"\s+")
    token_boolean_regexp = re.compile(r"\s+|([&|~()])")
    with open(join(dirname(__file__), 'cacm', 'common_words')) as stop_file:
        stop_list = [w.rstrip('\r\n') for w in stop_file]

    @staticmethod
    def normalize_simple(query):
        assert isinstance(query, str)
        query = re.sub(QueryPreprocessing.eliminate_regexp, ' ', query.lower())
        query = ' '.join(
            w for w in QueryPreprocessing.tokenize_simple(query)
            if w not in QueryPreprocessing.stop_list
        )
        return query

    @staticmethod
    def normalize_boolean(query):
        assert isinstance(query, str)
        query = re.sub(QueryPreprocessing.eliminate_boolean_regexp, ' ', query.lower())
        query = ' '.join(
            w for w in QueryPreprocessing.tokenize_boolean(query)
            if w not in QueryPreprocessing.stop_list
        )
        return query

    @staticmethod
    def tokenize_simple(query):
        assert isinstance(query, str)
        return [w for w in re.split(QueryPreprocessing.token_simple_regexp, query) if w]

    @staticmethod
    def tokenize_boolean(query):
        assert isinstance(query, str)
        return [w for w in re.split(QueryPreprocessing.token_boolean_regexp, query) if w]

    @staticmethod
    def replace_boolean_operators(boolean_query):
        assert isinstance(boolean_query, str)
        return boolean_query.replace('&', ' and ').replace('|', ' or ').replace('~', ' not ')


if __name__ == '__main__':

    import sys
    # # cacm = CACMParser(sys.argv[1])
    # filename = 'index.bin'
    # # inv_writer = InverseFileWriter(cacm, filename)
    # Tfidf_writer = TfIdfFileWriter(sys.argv[1], filename)
    # inv_reader = InverseFileReader(filename)
    # test_query = 'User experience and Software engineering'
    # print(QueryPreprocessing.normalize_simple(test_query))

    # cacm_reader = CACMParser(join(dirname(__file__), 'cacm', 'cacm.all'))
    # inv_writer = InverseFileWriter(cacm_reader, 'index.bin')
    Tfidf_writer = TfIdfFileWriter(sys.argv[1], "Tfidfcacm")
    # inv_reader = InverseFileReader('index.bin')
    # print(inv_reader.search_query_matching_score('Hard'))


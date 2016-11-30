import sys
import time
import collections.abc
import re
import pickle
from collections import Counter
from math import log10
from os.path import join, dirname
from PyQt4.QtGui import QMainWindow, QApplication, QTableWidgetItem, QFileDialog
from MainWindow import Ui_MainWindow


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
        if self.inv_filename !="" :
            with open(self.inv_filename, "wb") as file:
                pickle.dump(words_documents_frequencies, file)
        else:
            self.to_return_inv_file = words_documents_frequencies

    def get_InverseFile(self):
        return self.to_return_inv_file

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
        self.docs_words_frequencies =  InverseFileWriter(self.cacm2,"").get_InverseFile()
        self.Idf_filename = TfIdf_name
        d = {}
        for term in self.docs_words_frequencies.keys():
            d[term] = {}
            for doc in self.docs_words_frequencies[term]:
                d[term][doc] = self.docs_words_frequencies[term][doc]/max(self.docs_words_frequencies[term].values()) * log10(self.nember_docs/len(self.docs_words_frequencies[term])+1)
        with open(self.Idf_filename, "wb") as file:
            pickle.dump(d, file)


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
        query_words = QueryPreprocessing.tokenize_simple(QueryPreprocessing.normalize_simple(query))
        for doc_id in self.docs_words_frequencies.keys():
            words_frequencies = self.get_document_words_frequencies(doc_id)
            similarity = 0
            for word in words_frequencies.keys():
                if word in query:
                    similarity += words_frequencies[word]
            if similarity > 0:
                docs_relevance[doc_id] = similarity
        if model == 'dice':
            for doc_id in docs_relevance.keys():
                docs_relevance[doc_id] = 2 * docs_relevance[doc_id] / (
                    len(query_words) + sum(p**2 for p in self.docs_words_frequencies[doc_id].values())
                )
        elif model == 'cos':
            for doc_id in docs_relevance.keys():
                docs_relevance[doc_id] /= (len(query_words) * sum(
                    p**2 for p in self.docs_words_frequencies[doc_id].values()
                ))**(1/2)
        elif model == 'jaccard':
            for doc_id in docs_relevance.keys():
                docs_relevance[doc_id] /= len(query_words) + sum(
                    p**2 for p in self.docs_words_frequencies[doc_id].values()
                ) - docs_relevance[doc_id]
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
        stop_list = set(w.rstrip('\r\n') for w in stop_file)

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


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.inverse_file_reader = None
        self.inv_msg_time = 5000  # ms
        self.inv_default_path = 'inverse.bin'

        self.clearResultsPushButton.clicked.connect(self.clear_results)

        self.vectorSearchPushButton.clicked.connect(self.search_vector)
        self.booleanSearchPushButton.clicked.connect(self.search_boolean)
        self.matchingScoreSearchPushButton.clicked.connect(self.search_matching_score)

        self.loadInverseFileLineEdit.textChanged.connect(self.load_inverse_file)
        self.loadInveseFilePushButton.clicked.connect(self.choose_load_inverse_file)
        self.saveInverseFileGeneratePushButton.clicked.connect(self.generate_inverse_file)
        self.saveInveseFilePushButton.clicked.connect(self.choose_save_inverse_file)

        self.resultsTableWidget.setColumnCount(2)
        self.loadInverseFileLineEdit.setText(self.inv_default_path)
        self.saveInverseFileLineEdit.setText(self.inv_default_path)

    def clear_results(self):
        self.resultsTableWidget.setRowCount(0)
        self.statusbar.clearMessage()

    def search_vector(self):
        user_query = self.vectorSearchLineEdit.text()
        vector_similarity_function = 'inner_product'
        if self.diceRadioButton.isChecked():
            vector_similarity_function = 'dice'
        elif self.cosRadioButton.isChecked():
            vector_similarity_function = 'cos'
        elif self.jaccardRadioButton.isChecked():
            vector_similarity_function = 'jaccard'
        start = time.perf_counter()
        docs_frequencies = self.inverse_file_reader.search_query_vector(user_query, vector_similarity_function)
        end = time.perf_counter()
        self.clear_results()
        last_index = 0
        for doc_id in sorted(docs_frequencies.keys(), key=lambda x: docs_frequencies[x], reverse=True):
            frequency = docs_frequencies[doc_id]
            self.resultsTableWidget.insertRow(last_index)
            self.resultsTableWidget.setItem(last_index, 0, QTableWidgetItem(str(doc_id)))
            self.resultsTableWidget.setItem(last_index, 1, QTableWidgetItem(str(frequency)))
            last_index += 1
        self.statusbar.showMessage('{} documents trouvés. Durée de la recherche : {}s'.format(last_index, round(end-start, 4)))

    def search_boolean(self):
        user_query = self.booleanSearchLineEdit.text()
        start = time.perf_counter()
        docs = self.inverse_file_reader.search_query_boolean(user_query)
        end = time.perf_counter()
        self.clear_results()
        last_index = 0
        for doc_id in docs:
            self.resultsTableWidget.insertRow(last_index)
            self.resultsTableWidget.setItem(last_index, 0, QTableWidgetItem(str(doc_id)))
            self.resultsTableWidget.setItem(last_index, 1, QTableWidgetItem(str(1)))
            last_index += 1
        self.statusbar.showMessage('{} documents trouvés. Durée de la recherche : {}s'.format(last_index, round(end-start, 4)))

    def search_matching_score(self):
        user_query = self.matchingScoreSearchLineEdit.text()
        start = time.perf_counter()
        docs = self.inverse_file_reader.search_query_matching_score(user_query)
        end = time.perf_counter()
        self.clear_results()
        last_index = 0
        for doc_id in sorted(docs.keys(), key=lambda x: docs[x], reverse=True):
            score = docs[doc_id]
            self.resultsTableWidget.insertRow(last_index)
            self.resultsTableWidget.setItem(last_index, 0, QTableWidgetItem(str(doc_id)))
            self.resultsTableWidget.setItem(last_index, 1, QTableWidgetItem(str(score)))
            last_index += 1
        self.statusbar.showMessage('{} documents trouvés. Durée de la recherche : {}s'.format(last_index, round(end-start, 4)))

    def choose_load_inverse_file(self):
        file_path = QFileDialog.getOpenFileName(self)
        if file_path:
            self.loadInverseFileLineEdit.setText(file_path)

    def load_inverse_file(self):
        try:
            start = time.perf_counter()
            self.inverse_file_reader = InverseFileReader(self.loadInverseFileLineEdit.text())
            end = time.perf_counter()
            self.searchTab.setEnabled(True)
            self.statusbar.showMessage('Fichier inverse a été chargé en {}s'.format(round(end-start, 4)), self.inv_msg_time)
        except (pickle.PickleError, OSError) as err:
            if isinstance(err, OSError):
                self.statusbar.showMessage('Le fichier inverse spécifié n\'existe pas !')
            else:
                self.statusbar.showMessage('Le fichier inverse spécifié est invalide !')
            self.searchTab.setEnabled(False)

    def choose_save_inverse_file(self):
        file_path = QFileDialog.getSaveFileName(self)
        if file_path:
            self.saveInverseFileLineEdit.setText(file_path)

    def generate_inverse_file(self):
        try:
            inverse_file_path = self.saveInverseFileLineEdit.text()
            start = time.perf_counter()
            if self.saveInverseFileTfIdfRadioButton.isChecked():
                TfIdfFileWriter(join(dirname(__file__), 'cacm', 'cacm.all'), inverse_file_path)
            else:
                InverseFileWriter(CACMParser(join(dirname(__file__), 'cacm', 'cacm.all')), inverse_file_path)
            end = time.perf_counter()
            self.statusbar.showMessage('Fichier inverse a été sauvegardé en {}s'.format(round(end - start, 4)), self.inv_msg_time)
        except OSError:
            self.statusbar.showMessage('Le fichier inverse ne peut pas être sauvegardé dans le chemin spécifié !')

if __name__ == '__main__':
   app = QApplication(sys.argv)
   w = MainWindow()
   w.move(app.desktop().availableGeometry().center() - w.rect().center())  # Center the window on the screen
   w.show()
   sys.exit(app.exec())

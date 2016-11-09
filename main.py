import collections.abc
import re
from collections import Counter

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

class INVERSEDFile:
    def DOCCalcul(self):  
        element = None
        d={}
        for element in cacm:
            d[element.get_document_number()]=self.DocFreq(element)
        setKeys =set()
        for key in d:
            setKeys.update(set(d[key].keys()))
        setKeys = sorted(setKeys)
        file = open("InverseFile2.txt", "w")
        """
        this will be remplaced 
        """
        for elem in setKeys:
            StringWrite = elem + ' [ '
            for elemDict in d.keys():
                if(d.get(elemDict).get(elem, 0)!=0):
                    StringWrite = StringWrite +str(elemDict) +': '+ str(d.get(elemDict).get(elem,0))+', '
            StringWrite = StringWrite[:-2]
            StringWrite = StringWrite+']\n'
            file.write(StringWrite)
        file.close
        """
        until this
        """
    def __init__(self, cacm):
        self.cacm = cacm    
        self.DOCCalcul()
    def DocFreq(self, cacmElem):
        listText = self.DeleteStopList(self.DeleteSpecCar(cacmElem.get_title())).lower().split()
        listText.extend(self.DeleteStopList(self.DeleteSpecCar(cacmElem.get_summary())).lower().split())
        return Counter(listText)
        
    def DeleteStopList(self, text):
        self.cachedStopWords = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than'}        
        textNonstop = ' '.join([word for word in text.lower().split() if word not in self.cachedStopWords])

#        textNonstop= ''        
#        for w in text.split():
#            if w.lower() not in self.cachedStopWords:
#                textNonstop+=' '+w
        return textNonstop
    def DeleteSpecCar(self, text):
        pattern=re.compile("[^\w']")
        return pattern.sub(' ', text)

        
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


class InverseFile:
    """
    CSV based reader for an inverse file.
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
        assert isinstance(document_id, int)
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
        assert isinstance(word, str)
        return self.words_frequencies[word]

    def search_query_matching_score(self, query):
        """
        Return a dict containing the matching score of each relevant document.
        :param query: list of str, each str is a word.
        :return: dict which its keys are the IDs of the documents and its values are the relevance of each document.
        """
        assert isinstance(query, list) and all([isinstance(x, str) for x in query])  # Type checking
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

    class Negation:
        """
        Represent a negated word, conjunction or disjunction.
        """

        def __init__(self, term):
            assert any((isinstance(term, str), isinstance(term, list), isinstance(term, tuple)))
            self.term = term

    def boolean_similarity_disjunctive(self, query, document_id):
        """
        Return the boolean similarity between a disjunctive complex_query and a document.
        :param query: list of str or tuples representing words or conjunctions.
        :param document_id: int representing the ID of the document.
        :return: True if one of the words or conjunctions exists in the document, False otherwise.
        """
        assert isinstance(query, list)  # Type checking
        for word in query:
            assert any((isinstance(word, str), isinstance(word, tuple), isinstance(word, self.Negation)))  # Type checking
            if isinstance(word, tuple):  # It is a conjunction
                if self.boolean_similarity_conjunctive(word, document_id):
                    return True
            elif isinstance(word, self.Negation):
                if self.boolean_similarity_negated(word, document_id):
                    return True
            elif word in self.get_document_words_frequencies(document_id).keys():
                return True
        return False

    def boolean_similarity_conjunctive(self, query, document_id):
        """
        Return the boolean similarity between a conjunctive complex_query and a document.
        :param query: tuple of str or lists representing words or disjunctions.
        :param document_id: int representing the ID of the document.
        :return: True if all of the words or disjunctions exists in the document, False otherwise.
        """
        assert isinstance(query, tuple)  # Type checking
        for word in query:
            assert any((isinstance(word, str), isinstance(word, list), isinstance(word, self.Negation)))  # Type checking
            if isinstance(word, list):  # It is a disjunction
                if not self.boolean_similarity_disjunctive(word, document_id):
                    return False
            elif isinstance(word, self.Negation):
                if not self.boolean_similarity_negated(word, document_id):
                    return False
            elif word not in self.get_document_words_frequencies(document_id).keys():
                return False
        return True

    def boolean_similarity_negated(self, query, document_id):
        """
        Return the boolean similarity between a negated term and a document.
        :param query: Negation of a word, conjunction or disjunction.
        :param document_id: int representing the ID of the document.
        :return: True if the term doesn't exist in the document, False otherwise.
        """
        assert isinstance(query, self.Negation)  # Type checking
        if isinstance(query.term, tuple):
            return not self.boolean_similarity_conjunctive(query.term, document_id)
        elif isinstance(query.term, list):
            return not self.boolean_similarity_disjunctive(query.term, document_id)
        else:
            return query.term not in self.get_document_words_frequencies(document_id).keys()

    def search_query_boolean(self, complex_boolean_query):
        """
        Return a list of IDs of the relevant documents to a boolean query using the boolean search model.
        :param complex_boolean_query: list or tuple representing the query.
        :return: list of IDs of the relevant documents.
        """
        assert isinstance(complex_boolean_query, list) or isinstance(complex_boolean_query, tuple)
        number_of_docs = len(next(iter(self.words_frequencies.values())))
        relevant_docs = []
        for doc_id in range(1, number_of_docs+1):
            if isinstance(complex_boolean_query, list):
                if self.boolean_similarity_disjunctive(complex_boolean_query, doc_id):
                    relevant_docs.append(doc_id)
            else:
                if self.boolean_similarity_conjunctive(complex_boolean_query, doc_id):
                    relevant_docs.append(doc_id)
        return relevant_docs

if __name__ == '__main__':
    import sys
    cacm = CACMParser(sys.argv[1])
#    element = None
#    print(next(cacm))
#    for element in cacm:
#        pass
#    print(element)
    INVERSEDFile(cacm)

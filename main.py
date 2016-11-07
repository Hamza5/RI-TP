import collections.abc
import re
from collections import Counter
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
        listText = self.DeleteSpecCar(self.DeleteStopList(cacmElem.get_title())).lower().split()
        listText.extend(self.DeleteSpecCar(self.DeleteStopList(cacmElem.get_summary())).lower().split())
        return Counter(listText)
        
    def DeleteStopList(self, text):
        self.cachedStopWords = {'ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than'}        
        textNonstop = ' '.join([word for word in text.split() if word not in self.cachedStopWords])
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


if __name__ == '__main__':
    import sys
    cacm = CACMParser(sys.argv[1])
#    element = None
#    print(next(cacm))
#    for element in cacm:
#        pass
#    print(element)
    INVERSEDFile(cacm)

import sys
import nltk
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer


class LSA:
    def __init__(self, stopwords):
        self.stopwords = stopwords
        self.vectorizer = TfidfVectorizer()
        self.documents = []
        self.X = None
    # end constructor


    def fit(self, documents):
        for line in documents:
            if int(sys.version[0]) == 2:
                line = line.decode('ascii', 'ignore')
            tokens = self.tokenize(line)
            self.documents.append(' '.join(tokens))
        self.X = self.vectorizer.fit_transform(self.documents)
        self.concepts()
    # end method


    def concepts(self, top_k=5):
        lsa = TruncatedSVD(20, n_iter=100)
        lsa.fit(self.X)
        terms = self.vectorizer.get_feature_names()
        for i, comp in enumerate(lsa.components_): # lsa.components_ is V of USV, of shape (concepts, terms)
            terms_comp = zip(terms, comp)
            sorted_t = sorted(terms_comp, key=lambda x: x[1], reverse=True)[:top_k]
            print("Concept %d :" % i, end = ' ')
            for term_comp in sorted_t:
                print(term_comp[0], end=' | ')
            print()
    # end method        


    def tokenize(self, string):
        string = string.lower()
        tokens = nltk.tokenize.word_tokenize(string) # more powerful split()
        tokens = [token for token in tokens if len(token)>2] # remove too short words
        tokens = [token for token in tokens if token not in self.stopwords] # remove stopwords
        tokens = [token for token in tokens if not any(c.isdigit() for c in token)] # remove any token that contains number
        return tokens
    # end method
# end class
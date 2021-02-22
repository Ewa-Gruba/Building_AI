
import math
import random
import numpy as np
import io
from io import StringIO
import numpy as np
import math

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''
def distance(row1, row2):
    # replace the following by a function that returns the sum of differences between the
    # words in row1 and row2. this is the Manhattan distance.
    # you can assume that row1 and row2 are list with equal length, containing numeric values.
    dist1 = 0
    for i in range(len(row2)):
        dist1=dist1 + abs(row1[i]-row2[i])
    #print(dist1)
    return dist1

def main(text):
    docs = [line.split() for line in text.splitlines()]
    N = len(docs)
    # create the vocabulary: the list of words that appear at least once
    vocabulary = list(set(text.split()))
    df = {}
    tf = {}
    for word in vocabulary:
        # tf: number of occurrences of word w in document divided by document length
        # note: tf[word] will be a list containing the tf of each word for each document
        # for example tf['he'][0] contains the term frequence of the word 'he' in the first
        # document
        tf[word] = [doc.count(word)/len(doc) for doc in docs]

        # df: number of documents containing word w
        df[word] = sum([word in doc for doc in docs])/N
    #print('tf', tf, tf['coffee'])
    #print('df', df, df['coffee'])
    # loop through documents to calculate the tf-idf values
    docc=-1
    big_tfidf=[]
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            # ADD THE CORRECT FORMULA HERE. Remember to use the base 10 logarithm: math.log(x, 10)
            tfidf_pre =(tf[word][doc_index]*math.log((1/df[word]), 10))
            tfidf.append(tfidf_pre)
        big_tfidf.append(tfidf)

    #print(tfidf)
    #print(type(tfidf))
    #print("big one")
    #print(big_tfidf)

    
    dist1 = [[distance(sent1, sent2) for sent1 in big_tfidf] for sent2 in big_tfidf]
    #print(dist1)
    dist=np.array(dist1)
    #print(dist)
    row=-1
    for item in range(len(dist)):
        row=row+1
        column=-1
        for i in range(len(dist)):
            column = column+1
            if (row==column):
                dist[row,column]=1000000
    #print(dist)
    print(np.unravel_index(np.argmin(dist), dist.shape))



main(text)

  
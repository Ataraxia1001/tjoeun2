from konlpy.tag import Komoran
import numpy as np
from numpy import dot
from numpy.linalg import norm

# cosine similarity
def cos_sim(vec1, vec2):
    return dot(vec1, vec2) / (norm(vec1) * norm(vec2))

# TDM
def make_term_doc_mat(sentence_bow, word_dics):
    freq_mat={}

    for word in word_dics:
        freq_mat[word] = 0
    
    for word in word_dics:
        if word in sentence_bow:
            freq_mat[word] += 1
 
    return freq_mat


# word vector
def make_vector(tdm):
    vec = []

    for key in tdm:
        vec.append(tdm[key])  # tdm[key] = value of tdm with corresponding key.
    return vec


# define sentences
sentence1 = '6월에 뉴턴은 선생님의 제안으로 트리니티에 입학했다.'
sentence2 = '6월에 뉴턴은 선생님의 제안으로 대학교에 입학했다.'
sentence3 = '나는 맛있는 밥을 뉴턴 선생님과 함께 먹었다.'

komorean = Komoran()
bow1 = komorean.nouns(sentence1)
bow2 = komorean.nouns(sentence2)
bow3 = komorean.nouns(sentence3)

print(bow1)
print(bow2)
print(bow3)
bow = bow1 + bow2 + bow3
print(bow)

# make dictionary. remove duplicates
word_dics = []
for token in bow:
    if token not in word_dics:
        word_dics.append(token)



freq_list1 = make_term_doc_mat(bow1, word_dics)
freq_list2 = make_term_doc_mat(bow2, word_dics)
freq_list3 = make_term_doc_mat(bow3, word_dics)
print(freq_list1)
print(freq_list2)
print(freq_list3)


# create sentence vector
doc1 = np.array(make_vector(freq_list1))
doc2 = np.array(make_vector(freq_list2))
doc3 = np.array(make_vector(freq_list3))
print(doc1)
print(doc2)
print(doc3)


# calculate cosine similarity
r1 = cos_sim(doc1, doc2)
r2 = cos_sim(doc3, doc1)

print(r1)
print(r2)



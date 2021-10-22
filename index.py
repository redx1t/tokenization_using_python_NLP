# CIT-227-052/2017 KATHURIMA VICTOR PETER MUTHOMI 

# NATURAL LANGUAGE PROCESSING CAT 1 - 21/10/2021

import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import  PorterStemmer
from nltk.stem import WordNetLemmatizer
text = """A Hare was making fun of the Tortoise one day for being so slow.
        Do you ever get anywhere? he asked with a mocking laugh.
        Yes, replied the Tortoise, and I get there sooner than you think.
        I'll run you a race and prove it. The Hare was much amused at the idea
        of running a race with the Tortoise, but for the fun of the thing he agreed.
        So, the Fox, who had consented to act as judge, marked the distance and 
        started the runners off."""


tokenized_text = sent_tokenize(text)
print("Tokenized text: ",tokenized_text)



tokenized_word = word_tokenize(text)
print("Tokenized words: ",tokenized_word)


stop_words = set(stopwords.words("english"))
print("English stopwords: ",stop_words)



filtered_tokens = []
for w in tokenized_word:
    if w not in stop_words:
        filtered_tokens.append(w)
print("Filtered tokens: ",filtered_tokens)



punctuations = list(string.punctuation)
filtered_tokenp = []
for i in filtered_tokens:
    if i not in punctuations:
        filtered_tokenp.append(i)
print("After removing punctuations:",filtered_tokenp)

ps = PorterStemmer()
words = word_tokenize(text)
for w in words:
    print("Stemmed words")
    print(w,":",ps.stem(w))



lemmatizer = WordNetLemmatizer()
sentence_words = nltk.word_tokenize(text)
for word in sentence_words:
    if word in punctuations:
        sentence_words.remove(word)


sentence_words
print("{0:20}{1:20}".format("Word","Lemma"))
for word in sentence_words:
    print ("{0:20}{1:20}".format(word,WordNetLemmatizer.lemmatize(word)))

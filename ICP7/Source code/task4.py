import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import wordpunct_tokenize,pos_tag,ne_chunk
from nltk.util import ngrams


#tokenization from txt file
inputfile=open("texts.txt", "r")
data=str(inputfile.readlines())
toked = sent_tokenize(data)
print("Sentence Tokenization: \n", toked)

#word tokenization
word_tokened = word_tokenize(data)                  #breaking text into words called tokens
print("Word Tokenization: \n", word_tokened)

#parts of speech
pos_token = nltk.pos_tag(word_tokened)              #Classifying words into their parts-of-speech
print("parts-of-speech: \n", pos_token)


#stemming is process of reducing words to base form
ps = PorterStemmer()                          #It is most computationally intensive technique
print("PosterStemmer:")
for i in word_tokened:
 print(ps.stem(i), end='')
print('\n')
ls = LancasterStemmer()                      #Aggressive stemming algorithm
print("Lancaster Stemmer:")
for i in word_tokened:
 print(ls.stem(i), end='')
print('\n')
ss = SnowballStemmer('english')              #faster computational time than porter
print("SnowballStemmer:")
for i in word_tokened:
 print(ss.stem(i), end='')
print('\n')



#lemmatization
wordnet_lemmatizer = WordNetLemmatizer()    #lemmatization is process of applying different normalization rules on each POS
print("Lemmatization:")
for words in word_tokened:
    print(wordnet_lemmatizer.lemmatize(words), end=' ')

 #trigrams are continuous three sequence of items from text

trigrams = list(ngrams(word_tokened, 3))
print("trigrams:")
print(trigrams)

#NER is classifying text into pre-defined categories
chunk=ne_chunk(pos_tag(wordpunct_tokenize(data)))
for i in chunk:
    print(i)


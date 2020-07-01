from sklearn.datasets import fetch_20newsgroups
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
#problem1
train = fetch_20newsgroups(subset='train', shuffle=True)
tf_vect = TfidfVectorizer()
X_train_tfidf = tf_vect.fit_transform(train.data)
clfasak = MultinomialNB()
model = SVC(kernel='linear', random_state=0)

clfasak.fit(X_train_tfidf, train.target)
model.fit(X_train_tfidf, train.target)

test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tf_vect.transform(test.data)

pred =clfasak.predict(X_test_tfidf)
pred1 = model.predict(X_test_tfidf)

score = metrics.accuracy_score(test.target, pred)
score1 = metrics.accuracy_score(test.target, pred1)
print("accuracy score with multinomialNB--------->",score)
print("accuracy score after applyingSVM----------->",score1)


#problem2
train = fetch_20newsgroups(subset='train', shuffle=True)
tf_vect = TfidfVectorizer(ngram_range=(2, 2))
X_train_tfidf = tf_vect.fit_transform(train.data)
clfasak = MultinomialNB()
clfasak.fit(X_train_tfidf, train.target)
test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tf_vect.transform(test.data)
pred =clfasak.predict(X_test_tfidf)
score = metrics.accuracy_score(test.target, pred)
print("accuracy score through bigram---------->",score)

#problem3
#stop_words = set(stopwords.words('english'))
train = fetch_20newsgroups(subset='train', shuffle=True)
tf_vect = TfidfVectorizer(stopwords.words('english'))
X_train_tfidf = tf_vect.fit_transform(train.data)
clfasak = MultinomialNB()
clfasak.fit(X_train_tfidf, train.target)
test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tf_vect.transform(test.data)
pred =clfasak.predict(X_test_tfidf)
score = metrics.accuracy_score(test.target, pred)
print("accuracy score through stopword--------->",score)
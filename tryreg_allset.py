from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from sklearn import linear_model
from sklearn.linear_model import Ridge

from nltk.corpus import stopwords
from sklearn.externals import joblib
import pickle
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import re
def penn_to_wn(tag):
	if tag.startswith('N'):
		return 'n'
	if tag.startswith('V'):
		return 'v'
	if tag.startswith('J'):
		return 'a'
	if tag.startswith('R'):
		return 'r'
	return None

def tagged_to_synset(word, tag):
	wn_tag = penn_to_wn(tag)
	if wn_tag is None:
		return None
	try:
		return wn.synsets(word, wn_tag)[0]
	except:
		return None	

def sentence_similarity(synset,sentence):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(sentence)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    sentence = pos_tag(filtered_sentence)
    synsets = [tagged_to_synset(*tagged_word) for tagged_word in sentence]
    synsets = [ss for ss in synsets if ss]
    score, count = 0.0, 0
    fin = []
    for i in synset:
        a = [i.path_similarity(ss) for ss in synsets]
        a = [ss for ss in a if ss]
        if(len(a) == 0):
        	best_score = 0.0
        else:	
        	best_score = max(a)
        score += best_score
        count += 1
        fin.append(best_score)	
    score /= count
    return fin

path ='training_set_rel3.tsv'
record = pd.DataFrame.from_csv(path, sep='\t', header=0)
record = record[['essay_set', 'essay','domain1_score']]
record = record[(record['domain1_score'] == 12)&(record['essay_set'] == 1)]
bEssay = record['essay'].tolist()
mSynset = []
for i in bEssay:
	dum = re.sub('\W+',' ',i)
	stop_words = set(stopwords.words('english'))
	word_tokens = word_tokenize(dum)
	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	s = pos_tag(filtered_sentence)
	synset = [tagged_to_synset(*tagged_word) for tagged_word in s]
	synset = [ss for ss in synset if ss]
	for j in synset:
		mSynset.append(j)
print ("master synset created")
print (len(mSynset))

path ='training_set_rel3.tsv'
record = pd.DataFrame.from_csv(path, sep='\t', header=0)
record = record[['essay_set', 'essay','domain1_score']]
record = record[record['essay_set'] == 1]
record = record[['essay','domain1_score']]
msk = np.random.rand(len(record)) < 0.7

train = record[msk]
test = record[~msk]

essays_train = train['essay'].tolist()
essays_test = test['essay'].tolist()
scores_train = train['domain1_score'].tolist()
scores_test = test['domain1_score'].tolist()

mat1 = {}
mat = []

for i in range(0,len(essays_train)):
	fin = sentence_similarity(mSynset,essays_train[i])
	mat1[i] = {v: k for v,k in enumerate(fin)}
	mat1[i]['score'] = scores_train[i]
	print (scores_train[i])
	mat.append(fin)
df = pd.DataFrame(mat1)
df = df.transpose()
#df.drop('Unnamed: 0',inplace=True)
df.to_csv('hclust30Lasso.csv',sep=',')

print ("clust done")
reg = linear_model.Ridge(alpha = .5)
reg.fit(mat, scores_train ) 

print ("training done")
#s = pickle.dumps(reg)
joblib.dump(reg, 'Regression30Lassoo.pkl') 
#reg = joblib.load('Regression10.pkl') 

# test_essay = essays_test[0:10]
# for i in range(0,len(test_essay)):
#     fin_predict = sentence_similarity(mSynset,test_essay[i])
#     predicted = reg.predict([fin_predict])
#     print ("predicted score : " + str(predicted[0]))
#     print ("actual score : " + scores_test[i])
#     print ("")


# mat = np.array(mat)
# kmeans = KMeans(n_clusters=3,random_state=0).fit(mat)
# print (kmeans.labels_)
# ----- ADD REGRESSION CODE HERE ----- #
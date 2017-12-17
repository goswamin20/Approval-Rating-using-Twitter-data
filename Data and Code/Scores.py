import nltk;
import pandas as pd;
from nltk import word_tokenize;
from random import randint
from afinn import Afinn
from nltk.corpus import sentiwordnet as sn


df = pd.read_csv("tweetdataset.csv", index_col = None, encoding="latin1", error_bad_lines=False);
result = pd.DataFrame(columns=('tId', 'tweet', 'aScore', 'sScore', 'cScore', 'nScore', 'cn','cas','mScore', 'uId', 'stTime'))

pList = [];
nList = [];

posList = [];
negList = [];

tIdList = [];
tList = [];

aScore = [];
cScore = [];
sScore=[];


f = open('positive.txt', "r");

for line in f:
	pList.append(line);

f = open('negative.txt', "r");

for line in f:
	nList.append(line);

f = open('upos.txt', "r");

for line in f:
	posList.append(line);

f = open('uneg.txt', "r");

for line in f:
	negList.append(line);



afinn = Afinn();

for i in range(0,2000):
	 subset = ((int)(i / 100)) * 1000;
	 tweet = df['tweet'].iloc[i];
	 tId = df['statusid'].iloc[i];
	 uId = df['userid'].iloc[i];
	 stTime = df['statustime'].iloc[i];
	 
	 
	 ascore = afinn.score(tweet);
	 
	 score = 0;
	 
	 nScore = 0;
		
	 
	 sentences = nltk.sent_tokenize(tweet.replace('@', '').replace('#', ''))
	 stokens = [nltk.word_tokenize(sent) for sent in sentences]
	 taggedlist=[]
	 for stoken in stokens:        
		 taggedlist.append(nltk.pos_tag(stoken))
	 wnl = nltk.WordNetLemmatizer()

	 score_list=[]
	 for idx,taggedsent in enumerate(taggedlist):
		 score_list.append([])
		 for idx2,t in enumerate(taggedsent):
			 newtag=''
			 lemmatized=wnl.lemmatize(t[0])
			 if t[1].startswith('NN'):
				 newtag='n'
			 elif t[1].startswith('JJ'):
				 newtag='a'
			 elif t[1].startswith('V'):
				 newtag='v'
			 elif t[1].startswith('R'):
				 newtag='r'
			 else:
				 newtag=''       
			 if(newtag!=''):    
				 synsets = list(sn.senti_synsets(lemmatized, newtag))
				        
				 score=0
				 if(len(synsets)>0):
					 for syn in synsets:
						 score+=syn.pos_score()-syn.neg_score()
					 score_list[idx].append(score/len(synsets))
				
	 
	 sentence_sentiment=[]

	 for score_sent in score_list:
		 if(len(score_sent)>0):
			 sentence_sentiment.append(sum([word_score for word_score in score_sent])/len(score_sent))
	 
	 if(len(sentence_sentiment)>0):
		 sentiScore=sum([word_score for word_score in sentence_sentiment])/len(sentence_sentiment)
		 	 
	 for positiveword in pList:
	 	positiveword = positiveword.replace("\n","");
	 	if positiveword != "":
	 		if positiveword.upper() in tweet.upper():
	 			score = score + 1;
	 			
	 for negativeword in nList:
	 	negativeword = negativeword.replace("\n" , "");
	 	if negativeword != "":
	 		if negativeword.upper() in tweet.upper():
	 			score = score - 1;
	 			
	 for positiveword in posList:
	 	positiveword = positiveword.replace("\n","");
	 	if positiveword != "":
	 		if positiveword.upper() in tweet.upper():
	 			nScore = nScore + 1;
	 			
	 for negativeword in negList:
	 	negativeword = negativeword.replace("\n" , "");
	 	if negativeword != "":
	 		if negativeword.upper() in tweet.upper():
	 			nScore = nScore - 1;
	 
	 tIdList.append(tId);
	 aScore.append(ascore);
	 tList.append(tweet);
	 
	 result.loc[i] = [tId, tweet, ascore, sentiScore, score, nScore, (ascore+score+sentiScore), (ascore+score+sentiScore), (ascore+score+sentiScore)/3, uId, stTime];
	 
#print(result);
fname = 'result.csv'; 
result.to_csv(fname, sep=',');



# Author: Asyraf
# Sentiment analysis for Bahasa API - For master project
# Date : 7/2/2021
# TODO : Separate API into Training, And prediction

from __future__ import unicode_literals

import datetime
import json

import numpy as np
import pandas as pd
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView

# from api.models import SpiceirExternalData
# from api.serializers import Keyword_ListSerializer

from jsonmerge import merge

# ML libraries
import re
import pickle
import numpy as np
import pandas as pd

# plotting
import matplotlib.pyplot as plt

# nltk
from nltk.stem import WordNetLemmatizer

# sklearn
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score



class SentAnalysisMalay(APIView):
		"""
		The API for sentimentAnalysis
		"""

		def post(self, request, format=None):


				data = request.data

				try:

						eventName = data["RequestHeader"]["EventName"]
						datetimeSend = data["RequestHeader"]["DateTimeSend"]
						input_text = data["RequestHeader"]["Input_Text"]
						# accNo="'"+AccNo+"'"
						# MLCode = data["RequestHeader"]["ML_Code"]


				except Exception as e:
						return Response(data="Exception in Request data: {}".format(str(e)), status=status.HTTP_400_BAD_REQUEST)


				#####============ Sentiment analysis in BM - ML  ===================########

				try:

						# assign_upd = SpiceirExternalData.objects.filter(account_number=AccNo).values()
						# print(assign_upd)

						#=======Part 1: Read data to train sentiment =========####
						dataset = pd.read_csv('sentiment-data-v2.csv')

						# Removing the unnecessary columns.
						dataset = dataset[['label','text']]

						# Storing data in lists.
						text, sentiment = list(dataset['text']), list(dataset['label'])

						print(dataset)						
						response = {'Event': 'Sentiment Analysis in Bahasa Malaysia','Model used': "Linear SVC model"}


						#==== Part 2: Preprocessing Text and Cleaning Part ====#

						# Defining dictionary containing all emojis with their meanings.
						emojis = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad', 
						          ':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
						          ':-@': 'shocked', ':@': 'shocked',':-$': 'confused', ':\\': 'annoyed', 
						          ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
						          '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
						          '<(-_-)>': 'robot', 'd[-_-]b': 'dj', ":'-)": 'sadsmile', ';)': 'wink', 
						          ';-)': 'wink', 'O:-)': 'angel','O*-)': 'angel','(:-D': 'gossip', '=^.^=': 'cat'}

						## Defining set containing all stopwords in malay
						stopwordlist = ['acap', 'acap kali','adakala','adakalanya','adalah','adapun','adoi','aduh','aduhai',
						             'agak agaknya','agar','alamak','alhasil','alkisah','amat','amboi','andai','andai kata','aneka',
						             'antara','apa','apabila','apakala', 'apa lagi','arkian',
						             'atau', 'au','auh', 'ayuh','ayuhai','bagai', 'bagaimana', 'bagaimanapun',
						            'bagi', 'bahawa', 'bahawasanya','bahkan', 'banyak', 'barangkali',
						             'beberapa','belum','benar','berapa','betul','bila','bila mana','boleh','boleh jadi',
						             'buat', 'bukan', 'dalam', 'dan', 'dapat','dari', 'darihal', 'daripada','demi','dengan', 'di',
						             'ee', 'eh', 'ehem', 'enggan', 'entah', 'entahkan','gamaknya',
						             'ha','haah','hanya','harapnya', 'harus','hatta','hei','helo', 'hendak', 'hingga',
						            'ialah', 'jangan','jemput', 'jika','jikalau', 'jua','juga','kadang','kadangkala',
						            'kelakian', 'kalau', 'ke', 'kemudian', 'kenapa', 'kendatipun' ,'kepada',
						             'kerana', 'ketika', 'kian', 'lagi', 'lagikan', 'laksana', 'lalu', 'macam', 'maha',
						             'mahu', 'mahupun', 'maka','malah','malahan','mana','manakala','mana lagi','masih', 'masing-masing', 
						             'memang', 'mengapa','meskipun', 'mesti', 'minta',
						             'misal', 'mungkin', 'nampaknya', 'namun', 'nan', 'nian', 'nun', 'oh', 'oleh', 'oleh itu',
						             'pabila', 'pada', 'padahal', 'paling','para', 'pelbagai', 'perlu', 'pernah', 'pun',
						             'sahaja', 'saja', 'sambil', 'sampai', 'sangat', 'sebab', 'sebagai',
						             'sebagaimana', 'sebermula', 'sedang', 'sedikit', 'segala', 'sejak', 'sekali', 'sekali peristiwa', 
						             'sekalian','sekiranya', 'selalu', 'seluruh', 'semasa', 'sementara', 'semoga', 'semua', 'seperti', 'serba',
						             'serta', 'sesungguhnya', 'setelah', 'setiap', 'sewaktu','siapa', 'sila', 'sudah', 'sungguh', 'sungguhpun', 
						             'supaya', 'syabas', 'syahadan', 'tatkala', 'telah', 'tentang',
						             'terhadap','terlalu','tetapi', 'tiap-tiap', 'tidak', 'tolong', 'umpama','untuk', 'usah', 'wah', 'wahai',
						             'walau','walaupun','yang']

						# def preprocess(textdata):

						# 	processedText = []
						    
						#     # Create Lemmatizer and Stemmer.
						#     wordLemm = WordNetLemmatizer()
						    
						#     # Defining regex patterns.
						#     urlPattern        = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
						#     userPattern       = '@[^\s]+'
						#     alphaPattern      = "[^a-zA-Z0-9]"
						#     sequencePattern   = r"(.)\1\1+"
						#     seqReplacePattern = r"\1\1"
						    
						#     for tweet in textdata:
						#         tweet = tweet.lower()
						        
						#         # Replace all URls with 'URL'
						#         tweet = re.sub(urlPattern,' URL',tweet)
						#         # Replace all emojis.
						#         for emoji in emojis.keys():
						#             tweet = tweet.replace(emoji, "EMOJI" + emojis[emoji])        
						#         # Replace @USERNAME to 'USER'.
						#         tweet = re.sub(userPattern,' USER', tweet)        
						#         # Replace all non alphabets.
						#         tweet = re.sub(alphaPattern, " ", tweet)
						#         # Replace 3 or more consecutive letters by 2 letter.
						#         tweet = re.sub(sequencePattern, seqReplacePattern, tweet)

						#         tweetwords = ''
						#         for word in tweet.split():
						#             # Checking if the word is a stopword.
						#             #if word not in stopwordlist:
						#             if len(word)>1:
						#                 # Lemmatizing the word.
						#                 word = wordLemm.lemmatize(word)
						#                 tweetwords += (word+' ')
						                
						#         processedText.append(tweetwords)
							        
						# return processedText

						# processedtext = preprocess(text)

						#======= Part 3: Splitting data 80% train, 20% test =======####
						# Data split to test and training set

						X_train, X_test, y_train, y_test = train_test_split(text, sentiment,
						                                                test_size = 0.2, random_state = 0)
						print(f'Data Split done.')
						print('Training size: 80%, Testing size: 20%')

						# TF-IDF transformer

						vectoriser = TfidfVectorizer(ngram_range=(1,2), max_features=500000)
						vectoriser.fit(X_train)
						print(f'Vectoriser fitted.')
						print('No. of feature_words: ', len(vectoriser.get_feature_names()))

						# Transform dataset into matrix of TF-IDF features
						X_train = vectoriser.transform(X_train)
						X_test  = vectoriser.transform(X_test)
						print(f'Data Transformed.')

						#======Part 4: MODEL EVALUATION - USE BERNOLLI NB, LINEAR SVC, Logistic Regression
						def model_Evaluate(model):

							# Predict values for Test dataset
							y_pred = model.predict(X_test)

							# Print the evaluation metrics for the dataset.
							print(classification_report(y_test, y_pred))

							# Compute and plot the Confusion matrix
							cf_matrix = confusion_matrix(y_test, y_pred)

							categories  = ['Negative','Positive']
							group_names = ['True Neg','False Pos', 'False Neg','True Pos']
							group_percentages = ['{0:.2%}'.format(value) for value in cf_matrix.flatten() / np.sum(cf_matrix)]

							labels = [f'{v1}\n{v2}' for v1, v2 in zip(group_names,group_percentages)]
							labels = np.asarray(labels).reshape(2,2)

							response['Accuracy'] = accuracy_score(y_test, y_pred)
							response['F1-Score'] = f1_score(y_test, y_pred, average='weighted')
							response['Precision'] = precision_score(y_test, y_pred, average='weighted')
							response['Recall'] = recall_score(y_test, y_pred, average='weighted')


						SVCmodel = LinearSVC()
						SVCmodel.fit(X_train, y_train)
						model_Evaluate(SVCmodel)

						### Part 5 : Saving trained model as pickle

						file = open('vectoriser-ngram-(1,2).pickle','wb')
						pickle.dump(vectoriser, file)
						file.close()

						file2 = open('Sentiment-LinearSVC.pickle','wb')
						pickle.dump(SVCmodel, file2)
						file2.close()

						###========= Part 6: Loading model==========####3


						def load_models():
							# Load the vectoriser.
							file = open('./vectoriser-ngram-(1,2).pickle', 'rb')
							vectoriser = pickle.load(file)
							file.close()
							# Load the LR Model.
							file2 = open('./Sentiment-LinearSVC.pickle', 'rb')
							SVCmodel = pickle.load(file2)
							file2.close()

							return vectoriser, SVCmodel

						###=== Part 7: Prediction of sentiment using trained ML ###

						def predict(vectoriser, model, text):
							# Predict the sentiment
							# textdata = vectoriser.transform(preprocess(text))
							textdata = vectoriser.transform(text)
							sentiment = model.predict(textdata)

							# Make a list of text with sentiment.
							data = []
							for text, pred in zip(text, sentiment):
								data.append((text,pred))

							# Convert the list into a Pandas DataFrame.
							df = pd.DataFrame(data, columns = ['text','label'])
							df = df.replace([0,1], ["Negative","Positive"])
							return df


						# Text to classify should be in a list.
						text = [input_text]
						df = predict(vectoriser, SVCmodel, text)
						sentiment_result = df.to_json(orient='records')

						# print(sentiment_result)
						parsed = json.loads(sentiment_result)
						y = json.dumps(parsed, indent=4)

						data = y
						x=json.loads(data)
						response['Sentiment_Result'] = x


						return JsonResponse(response, safe=False, status=status.HTTP_200_OK)


				#===================Throw exception if wrong processing=============================
				except Exception as e:
					print("Error:", e)
					return Response(data="Exception in Request data: {}".format(str(e)), status=status.HTTP_400_BAD_REQUEST)
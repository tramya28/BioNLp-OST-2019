import nltk
import re
import csv
import ast
import nltk.corpus
import nltk.tokenize.punkt
import nltk.stem.snowball
import string
from nltk.tokenize import WordPunctTokenizer
#extra comment


#nltk.download('all')
#Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')

fO = open("Sustained_Threat_sentences.csv" , "w")
with open('Sustained_Threat.csv') as f:
	reader = csv.reader(f, delimiter=',')
	i=0
	for row in reader:
		i = i+1
		pmid = row[0]
		title = row[1]
		abstract = row[2]
		#relevants = row[3].lower()
		#relevancies = nltk.sent_tokenize(relevants.replace("\"", ""))			
		sentences = nltk.sent_tokenize(abstract.replace("\"", ""))
		for j in range(len(sentences)):
			if sentences[j] is not None and sentences[j].strip() != "":
				fO.write(pmid + "," + "\"" + sentences[j].strip() + "\"" + "," + "\n")
				
		

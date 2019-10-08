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
def similarityCheck(a, b, threshold=0.50):
    """Check if a and b are matches."""
    tokens_a = [token.lower().strip(string.punctuation) for token in tokenizer.tokenize(a) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    tokens_b = [token.lower().strip(string.punctuation) for token in tokenizer.tokenize(b) \
                    if token.lower().strip(string.punctuation) not in stopwords]

    # Calculate Jaccard similarity
    ratio = len(set(tokens_a).intersection(tokens_b)) / float(len(set(tokens_a).union(tokens_b)))
    return (ratio >= threshold)

#nltk.download('all')
#Get default English stopwords and extend with punctuation
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')

# Create tokenizer and stemmer
tokenizer = WordPunctTokenizer()
fO = open("Sustained_Threat_sentences.csv" , "w")
with open('Sustained_Threat.csv') as f:
	reader = csv.reader(f, delimiter=',')
	i=0
	for row in reader:
		i = i+1
		pmid = row[0]
		title = row[1]
		abstract = row[2]
		relevants = row[3]
		relevancies = nltk.sent_tokenize(relevants.replace("\"", ""))			
		sentences = nltk.sent_tokenize(abstract.replace("\"", ""))
		for j in range(len(sentences)):
			hasSimilarity = False
			if sentences[j] is not None and sentences[j].strip() != "":
				for k in range(len(relevancies)):
					if similarityCheck(relevancies[k],sentences[j]):
						hasSimilarity = True
						break
				if hasSimilarity:
					fO.write(pmid + "," + "\"" + sentences[j].replace(",", "") + "\"" + "," + "1" + "\n")
				else:
					fO.write(pmid + "," + "\"" + sentences[j].replace(",","") + "\"" + "," + "0"  + "\n")
		print(len(relevancies))
		

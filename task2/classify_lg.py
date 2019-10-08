import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from keras.models import Sequential
from keras import layers
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (brier_score_loss, precision_score, recall_score, f1_score)

fO = open("predictions_task2_lg_atf.csv", "w")
filepath_dict = {'abstracts':   'train.csv'}
#test_data=open('tweettext2018_tokenized.txt')
predict_sentences=[]
predict_data=open('Acute_Threat_Fear_sentences.csv')
for sentence in predict_data:
	predict_sentences.append(sentence.replace('\n',''))

df_list = []
for source, filepath in filepath_dict.items():
    df = pd.read_csv(filepath, names=['sentence', 'label'], sep=',')
    df['source'] = source  # Add another column filled with the source name
    df_list.append(df)

df = pd.concat(df_list)
for source in df['source'].unique():
    df_source = df[df['source'] == source]
    sentences = df_source['sentence'].values
    y = df_source['label'].values

	#test_sentences.append(sentence.replace('\n',''))

    sentences_train, sentences_test, y_train, y_test = train_test_split(sentences, y, test_size=0.25, random_state=1000)

    vectorizer = CountVectorizer()
    vectorizer.fit(sentences_train)
    X_train = vectorizer.transform(sentences_train)
    X_test  = vectorizer.transform(sentences_test)
    X_predict = vectorizer.transform(predict_sentences)
    
    
    input_dim = X_train.shape[1]
    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)
    score = classifier.score(X_test, y_test)
    print('Accuracy for {} data: {:.4f}'.format(source, score))

    print("starting predictions")
    predictions = classifier.predict(X_predict)
    #y_pred = classifier.predict(y_test)
    #print("\tPrecision: %1.3f" % precision_score(y_test, y_pred))
    for i in range(len(predictions)):
        fO.write(str(predictions[i]) + "\n")
	
print("predictions done")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from keras.models import Sequential
from keras import layers
import keras_metrics as km

fO = open("predictions_task1_Potential_Threat_Anxiety_sq.csv", "w")
filepath_dict = {'abstracts':   'bionlp_train.csv'}
#test_data=open('tweettext2018_tokenized.txt')
predict_sentences=[]
predict_data=open('Potential_Threat_Anxiety.csv')
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
    model = Sequential()
    model.add(layers.Dense(10, input_dim=input_dim, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy', km.precision(), km.recall() ])
    model.summary()

    history = model.fit(X_train, y_train, epochs=10, verbose=False, validation_data=(X_test, y_test), batch_size=1000)
    loss, accuracy, precision , recall = model.evaluate(X_train, y_train, verbose=False)
    print("Training Accuracy: {:.4f}".format(accuracy))
    print("Training precision: {:.4f}".format(precision))
    print("Training recall: {:.4f}".format(recall))
    loss, accuracy , precision , recall = model.evaluate(X_test, y_test, verbose=False)
    print("Testing Accuracy:  {:.4f}".format(accuracy))
    print("Testing precision:  {:.4f}".format(precision))
    print("Testing recall:  {:.4f}".format(recall))

    print("starting predictions")
    predictions = model.predict(X_predict)
    for i in range(len(predictions)):
        fO.write(str(predictions[i]) + "\n")
	
print("predictions done")

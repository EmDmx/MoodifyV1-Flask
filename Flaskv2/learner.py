from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd

def learning(data,top_data,bad_data):

     #Define the set of features that we want to look at
    features = ["target","danceability", "loudness", "valence", "energy", "instrumentalness", "acousticness", "key", "speechiness","duration_ms"]

    features1 = ["danceability", "loudness", "valence", "energy", "instrumentalness", "acousticness", "key", "speechiness","duration_ms"]


    trainingData=pd.DataFrame(data)
    top=pd.DataFrame(top_data)
    bad=pd.DataFrame(bad_data)

    bad["target"]=0
    top["target"]=1
    trainingData["target"]=1

    trainingData=pd.concat([trainingData,top,bad])
    trainingData=trainingData[features]


    train, test = train_test_split(trainingData, test_size = 0.15)
    print("Training size: {}, Test size: {}".format(len(train),len(test)))


    #Split the data into x and y test and train sets to feed them into a bunch of classifiers!
    x_train = train[features1]
    y_train = train['target']
    x_test = test[features1]
    y_test = test['target']


    ada = AdaBoostClassifier(n_estimators=100)
    ada.fit(x_train, y_train)
    ada_pred = ada.predict(x_test)

    score = accuracy_score(y_test, ada_pred) * 100
    print("Accuracy using ada: ", round(score, 1), "%")

    return ada

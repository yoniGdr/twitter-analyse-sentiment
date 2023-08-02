import csv
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

class Knn():
    def __init__(self):
        # self.csvfile = open('test.csv', 'r')
        # self.bdd_apprentissage = csv.DictReader(self.csvfile, delimiter=',')
        pass


    def distance_tweet(self, tweet_a, tweet_b):
        list_words_a = tweet_a.split(" ")
        list_words_b = tweet_b.split(" ")
        nb_common_words = 0
        nb_max_words = max(len(list_words_a), len(list_words_b))

        for word_a in list_words_a:
            if word_a in list_words_b:
                nb_common_words += 1
        return (nb_max_words - nb_common_words) / nb_max_words


    def rate_tweet(self, k, tweet):
        df = pd.read_csv('bdd.csv')
        t = [tweet]
        # t = np.array([tweet])
        df['distance'] = df['tweet'].apply(self.distance_tweet, args=t)
        k_voisins = np.array(df.sort_values('distance')[:k]['note'], int)
        k_voisins[k_voisins == -1] = 10 # car bincount n'accepte pas les valeurs négatives
        counts = np.bincount(k_voisins)
        note = np.argmax(counts)

        if note == 10:
           return -1
        else:
           return note

    def count_occurences(self, neighbours):
        nb_occurence = {"positives": [0,1], "negatives": [0,-1], "neutres":[0,0]}
        for (_, note) in neighbours:
            if note > 0:
                nb_occurence["positives"][0] += 1
            elif note == 0:
                nb_occurence["neutres"][0] += 1
            else :
                nb_occurence["negatives"][0] += 1
        return nb_occurence

    def calcul_classe(self, target_class, predict_class):
        df = pd.read_csv('bdd.csv')
        df['note_1nn'] = df['tweet'].apply(self.rate_tweet, args=1)

        dfn = df[df['note'] == target_class]
        return dfn[dfn['note_1nn'] == predict_class].shape[0]

    def test(self, k):
        df = pd.read_csv('bdd.csv')
        
        X = df['tweet']
        y = df['note']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

        predict = []

        for index, value in X_test.items():
            predict.append(self.rate_tweet(k, value))


        y_test_val = list(y_test)

        v1 = self.calcul_classe(y_test_val, predict, 1, 1)
        v2 = self.calcul_classe(y_test_val, predict, 1, -1)
        v3 = self.calcul_classe(y_test_val, predict, 1, 0)
        v4 = self.calcul_classe(y_test_val, predict, -1, 1)
        v5 = self.calcul_classe(y_test_val, predict, -1, -1)
        v6 = self.calcul_classe(y_test_val, predict, -1, 0)
        v7 = self.calcul_classe(y_test_val, predict, 0, 1)
        v8 = self.calcul_classe(y_test_val, predict, 0, -1)
        v9 = self.calcul_classe(y_test_val, predict, 0, 0)

        print(v1, v2, v3, v4, v5, v6, v7, v8, v9)
        
    def calcul_classe(self, y_val, predict_val, target_class, predict_class):
        comp = 0
        for i in range(len(y_val)):
            if y_val[i] == target_class and predict_val[i] == predict_class:
                comp += 1
        return comp
        

        dfn = df[df['note'] == target_class]
        return dfn[dfn['note_dico'] == predict_class].shape[0]

        

# knn = Knn()
# print(knn.rate_tweet(1, "Ce n'est pas la meilleure équipe de l'histoire."))
# print(knn.calcul_classe(1, 1))
# knn.test(3)
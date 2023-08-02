import csv
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class Dico():
    def __init__(self):
        pass

    # dico
    def rate_tweet(self, tweet):
        note = 0
        with open('words/fr-positives.csv') as fr_pos:
            all_lines = csv.reader(fr_pos)
            for positive in all_lines:
                positive = " " + positive[0] + " "
                if positive in tweet: # negation pas
                    note += 1
                    tweet = tweet.replace(positive, " ", 1)
        with open('words/fr-negatives.csv') as fr_neg:
            all_lines = csv.reader(fr_neg)
            for negative in all_lines:
                negative = " " + negative[0] + " "
                if negative in tweet: # negation pas
                    note -= 1
                    tweet = tweet.replace(negative, " ", 1)
        if note == 0:
            return 0
        elif note > 0:
            return 1
        else :
            return -1

    def calcul_real(self):
        df = pd.read_csv('bdd.csv')
        df['note_dico'] = df['tweet'].apply(self.rate_tweet)

        nb_pos = df[df['note'] == 1].shape[0], 
        nb_neg = df[df['note'] == -1].shape[0], 
        nb_neutre = df[df['note'] == 0].shape[0],  
        return nb_pos, nb_neg, nb_neutre

    def calcul(self):
        df1 = pd.read_csv('bdd.csv')
        df1['note_dico'] = df['tweet'].apply(self.rate_tweet)

        nb_pos = df1[df1['note_dico'] == 1].shape[0], 
        nb_neg = df1[df1['note_dico'] == -1].shape[0], 
        nb_neutre = df1[df1['note_dico'] == 0].shape[0],  
        return nb_pos, nb_neg, nb_neutre

    def calcul_classe(self, target_class, predict_class):
        df = pd.read_csv('bdd.csv')
        df['note_dico'] = df['tweet'].apply(self.rate_tweet)

        dfn = df[df['note'] == target_class]
        return dfn[dfn['note_dico'] == predict_class].shape[0]

# print(Dico().calcul_classe(1, 1))
# print(Dico().calcul_classe(1, -1))
# print(Dico().calcul_classe(1, 0))
# print(Dico().calcul_classe(-1, 1))
# print(Dico().calcul_classe(-1, -1))
# print(Dico().calcul_classe(-1, 0))
# print(Dico().calcul_classe(0, 1))
# print(Dico().calcul_classe(0, -1))
# print(Dico().calcul_classe(0, 0))

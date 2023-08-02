import csv
from re import T
import pandas as pd
from Filter import *

csvfile = open('bdd.csv', 'r')

class Bayes():
    def __init__(self):
        self.frequence = False
        self.mots_importants = False
        self.splited_fnc = self.split_unigram

    def set_frequence(self, bool):
        self.frequence = bool

    def set_mots_importants(self, bool):
        self.mots_importants = bool

    def set_unigram(self):
        self.splited_fnc = self.split_unigram

    def set_bigram(self):
        self.splited_fnc = self.split_bigram


    # Nombre de mots’s directly jump to sample cod de la classe 
    def mots_total(self, classe):
        df = pd.read_csv('bdd.csv')
        tweets = df["tweet"]

        mots_classe = df[df["note"] == classe]["tweet"]
        mots_classe_splited = self.splited_fnc(mots_classe.str)

        nb_mots_classe = 0
        for tweet in mots_classe_splited:
            nb_mots_classe += len(tweet)

        tweets_splited = self.splited_fnc(tweets.str)
        nb_mots_total = 0
        for tweet in tweets_splited:
            nb_mots_total += len(tweet)

        return (nb_mots_classe, nb_mots_total)
    
    def nombre_mot(self, mot, classe):
        df = pd.read_csv('bdd.csv')

        mots_classe = df[df["note"] == classe]["tweet"]
        if self.mots_importants:
            filtre = Filter()
            mots_classe_splited = []

            for tweet in list(mots_classe):
                mots_classe_splited.append(self.splited_fnc(filtre.removeNoSens(tweet)))
        else :
            mots_classe_splited = mots_classe.str.split()
        

        nb_mots = 0
        for tweet in mots_classe_splited:
            if not self.frequence:
                if mot in tweet:
                    nb_mots += 1
            else:
                for m in tweet:
                    if m == mot:
                        nb_mots += 1
        return nb_mots

    def proba(self, mot, classe):
        return  (self.nombre_mot(mot, classe) + 1) / (self.mots_total(classe)[0] + self.mots_total(classe)[1])

    def proportion(self):
        df = pd.read_csv('bdd.csv')
        tweets = df["tweet"]

        nb_neg = df[df["note"] == -1]["tweet"].shape[0]
        nb_pos =  df[df["note"] == 1]["tweet"].shape[0]
        nb_neutre =  df[df["note"] == 0]["tweet"].shape[0]
        total = df.shape[0]
        return (nb_neg/total, nb_pos/total, nb_neutre/total )

    def normalisation(self, proba):
        tt = sum(proba.values())
        return {0: proba[0]/tt,
                1: proba[1]/tt,
                -1: proba[-1]/tt}

    def split_unigram(self, t):
        return t.split(" ")
    
    def split_bigram(self, tweet):
        list_bigramm = []
        tweet_splited_by_world = tweet.split(" ")
        for i in range(len(tweet_splited_by_world)-1):
            list_bigramm.append((tweet_splited_by_world[i] + " " + tweet_splited_by_world[i+1]))
        return list_bigramm


    def algo_bayes(self, t):
        classes =  [-1, 0, 1]
        mots = self.splited_fnc(t)
        probas = {0: 1,
                  1: 1,
                  -1: 1
                 }
        for mot in mots:
            for classe in classes:
                probas[classe] *= self.proba(mot, classe)

        prop = self.proportion()
        probas[-1] *= prop[0]
        probas[1] *= prop[1]
        probas[0] *= prop[2]

        print(self.normalisation(probas))

        return max(probas, key=probas.get)

    def algo_bayes_uni(self, t):
        self.set_unigram()
        return self.algo_bayes(t)

    
    def algo_bayes_bigram(self, t):
        self.set_bigram()
        return self.algo_bayes(t)


# b = Bayes()

# tweet_example1 = "Yo reufs ! Rendez-vous week-end pour une vidéos plus intéressantes sur One Piece (Vidéo qui sera bien longue d'ailleurs ) . Elle portera sur thème de Nika: Le retraçage de histoire One Piece . Tout se passera ici"
# print("default ex1")
# print(b.algo_bayes_uni(tweet_example1))

# tweet_example2 = "J’avoue maintenant y’aura Bleach , Boruto et One Piece en même temps"
# print("default ex2")
# print(b.algo_bayes_uni(tweet_example2))

# tweet_example3 = "Je deteste déteste, c'est null null null, Lol test on verra"
# print("default ex3")
# print(b.algo_bayes_uni(tweet_example3))

# print("############################################################")

# b.set_frequence(True)
# b.set_mots_importants(True)

# print("set ex1")
# print(b.algo_bayes_uni(tweet_example1))
# print("set ex2")
# print(b.algo_bayes_uni(tweet_example2))
# print("set ex3")
# print(b.algo_bayes_uni(tweet_example3))

# print(b.split_bigram("personne aime one piece"))
# print("############################# bigram")
# print("set ex1")
# print(b.algo_bayes_bigram(tweet_example1))
# print("set ex2")
# print(b.algo_bayes_bigram(tweet_example2))
# print("set ex3")
# print(b.algo_bayes_bigram(tweet_example3))
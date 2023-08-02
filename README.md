# Rapport : Twitter

## Binôme :
- Gaudiere Yoni
- Phagradiani Haik

## Description générale du projet :

### problèmatique 

L’analyse de textes et de sentiments sur les réseaux sociaux est un enjeu important pour différentes activités telles que la mise en place de stratégies d’affaires
ou de politiques publiques.
Dans ce projet notre objectif a donc été de développer des méthodes de visualitation de sentiment en analysant des tweets.

### Description générale de l'architecture de l'application

## Détails des différents travaux réalisés

### API Twitter

Pour pouvoir récupérer des tweet et les analysé nous allons nous connecté a l'API de tweeter.
Pour cela nous allons utiliser la bibliothèque tweepy. Celle-ci nous fournit une interface pratique pour accéder a l'API Twitter et facilite son utilisation.
Nous devons créer un compte de développeur Twitter et obtenir des informations d'identification. 
Avec ces informations d'identification, nous allons ensuite utiliser la bibliothèque tweepy pour nous authentifier et nous connecter à l'API Twitter.

```
import tweepy

# Enter your Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"

# Authenticate and create an API object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
```

### Préparation de la base d'apprentissage

Il est important de nettoyer notre base de données de tweets avant d'effectuer une analyse de sentiments, car une base de données propre nous donnera des résultats plus précis et plus fiables. 
Une base de données propre éliminera tous les tweets non pertinents ou dupliqués, qui peuvent biaiser notre analyse et conduire à des conclusions incorrectes.

Pour se faire nous avons commencez par :

- Supprimez les retweets : Les retweets sont essentiellement des doublons d'autres tweets, nous devons donc les supprimer de la base de données.

- Prendre que les tweet en francais (pour notre analyse nous nous intéressont qu'aux tweet francais).

- Supprimez les mots et les symboles non pertinents : Pour rendre l'analyse plus ciblée et plus précise, nous avons supprimer tous les mots ou symboles qui ne sont pas pertinents tels que la ponctuation, les hashtags et les URL.

- Transformer les tweets en minuscule : Nous sera utilise pour les comparaison de mots. ( voir plus loin pourquoi ) 

Nous allons ensuite classer les tweets avec des données discrètes correspondant à la polarité:
-1 pour les tweets considéré comme négative, 0 pour les tweets considérer comme neutre et 1 pour les tweets considérer comme positives.
Pour ce faire, nous allons dans un premier temps utiliser l'algorithme de classification par mot-clef. (voir détaille dans la partie "Algorithmes de classification")
Nous avons ensuite annoté la polarité des tweets a la main afin d'avoir une base de données avec la moins d'erreur possible.

Nous aurons donc pour notre base de données, un fichier CSV avec : id de l'utilisateur, son nom, son tweet et sa polarité. (0,1,-1) 

Pour la première version de notre Base de donnée, nous avons choisi de prendre une centaine de tweets contenant le mot-clef " les anneaux de pouvoir ".
Cependant, sur la centaine de tweets sélectionnée, nous avions beaucoup de tweets neutres.
Pour enrichir notre base de donnée nous avons donc choisie de rajouté encore une centaine de tweet mais cette fois-ci avec le mot clef " coupe du monde ", contenant une majorité de tweet positive.
Ainsi qu'une centaine de tweet avec le mot-clef "Norman" qui eux contenait beaucoup de tweet négative.
Nous avons donc une base de données plus riche avec des tweets neutre, positive et négative.

### Algorithmes de classification

#### Mots-clés

Notre première algorithme de classification utilisera la présence de certains mots-clés ou expressions.
Notre algorithme recherchera le nombre de mots positive ou negative dans le tweet. 

Pour cela il utilisera une liste de mots postive, il comptera le nombre de mots de la liste positive présent dans le tweet.
Il fera de même pour compter le nombre de mots negatives.

Il indiquera alors -1 ci celui-ci contient plus de mots negative, 1 si il contient plus de mots positive et 0 si il y a autent de mots negatives que positives dans le tweet.

Résulats : PASS

En comparant la base de donnée avec la polarité anoté à la main et la même base de donnée avec la polarité trouvée grâce à notre algorithme de classification par mots-cléfs, 
nous avons un taux d'erreurs assez élévé. Cette algorithme n'est donc pas assez efficace.

### KNN

Notre deuxième algorithme de classification va classer des tweets comme positif, négatif ou		
neutre en fonction de la	base d’apprentissage.

L'algorithme sera d'abord entraîné sur notre base de données de tweets, où chaque tweet a été manuellement affecté à une étiquette indiquant sa polarité. 

Une fois l'algorithme entraîné sur cet ensemble de données, il peut être appliqué à de nouveaux tweets non vus pour leur attribuer automatiquement une étiquette. Pour ce faire, l'algorithme calcule la distance entre le nouveau tweet et chacun des tweets de l'ensemble de données d'entraînement. Les k voisins les plus proches sont alors déterminés sur la base des distances calculées, et le nouveau tweet se voit attribuer l'étiquette la plus commune parmi ces voisins les plus proches.

En résumé, la classification automatique des tweets par KNN fonctionne en entraînant d'abord l'algorithme sur un ensemble de données étiquetées de tweets, puis en utilisant cet entraînement pour attribuer des étiquettes aux nouveaux tweets non vus en trouvant l'étiquette la plus commune parmi leurs voisins les plus proches dans l'ensemble de données d'entraînement.

### Bayes et variantes 

Notre troisième algorithme de classification va classer des tweets comme positif, négatif ou		
neutre enfonction de la	base d’apprentissage.

L'algorithme sera d'abord entraîné sur notre base de données de tweets, où chaque tweet a été manuellement affecté à une étiquette indiquant sa polarité. 

Une fois l'algorithme entraîné sur cet ensemble de données, il peut être appliqué à de nouveaux tweets non vus pour leur attribuer automatiquement une étiquette. Pour ce faire, l'algorithme utilise les probabilités d'apparition de certains mots ou expressions dans les tweets appartenant à chaque catégorie, telles que déterminées à partir de l'ensemble de données d'entraînement. Par exemple, l'algorithme peut déterminer que les tweets contenant le mot "heureux" sont plus susceptibles d'appartenir à la catégorie "positive", tandis que les tweets contenant le mot "triste" sont plus susceptibles d'appartenir à la catégorie "negative".

L'algorithme de Bayes utilise ensuite ces probabilités pour calculer la probabilité qu'un nouveau tweet appartienne à chaque catégorie, et attribue au tweet l'étiquette ayant la plus forte probabilité. 
En résumé, la classification automatique des tweets par l'algorithme de Bayes fonctionne en entraînant d'abord l'algorithme sur un ensemble de données étiquetées de tweets, puis en utilisant cet entraînement pour attribuer des étiquettes à de nouveaux tweets non vus, en fonction des probabilités d'apparition de certains mots ou expressions dans les tweets appartenant à chaque catégorie.

L'algorithme de Bayes peut être modifié pour utiliser des bigrammes, qui sont des paires de mots consécutifs, au lieu de mots individuels, pour déterminer les probabilités d'occurrence de certaines phrases dans les tweets appartenant à chaque catégorie. Cela peut fournir à l'algorithme des informations contextuelles supplémentaires qui peuvent contribuer à améliorer ses performances de classification.

L'algorithme de Bayes peut être modifié pour utiliser la représentation par fréquence, dans la version précèdente de l'algorithme nous ne nous préoccupions pas du nombre d’occurrences des mots. 
Nous allons étendre cette représentation en prenant en compte le nombre d’occurrences d’un mot du tweet. 

L'algorithme de Bayes peut être modifié en suppriment les mots non-essentiels (Exemple : mon, ma, mes, ton, tn, ta, tes, son, sa, ses, notre). Cela peut supprimer des informations non pertinente l'algorithme ce qui peu lui permettre d'augmenter l'efficacité des résultats obtenue.

Pour résumé, nous avons donc implémenté un algoritme de Baye avec 3 paramètres possible (3 variation) :

- Il pourra utiliser des Unigrams, des Bigrams ou Unigrams + Bigrams.              
- Avec une représentation par fréquence ou occurence                         
- Utilisation de tout les mots ou ne garder que les mots importants.


### Interface graphique 

Pour créer une interface graphique nous avons utiliser l'outils Qt Designer.
Celui-ci fournit une interface visuelle, par glisser-déposer, pour concevoir une interfaces utilisateur. 
Cela nous permet de créer une interfaces utilisateur d'aspect professionnel sans avoir besoin d'écrire beaucoup de code.
De plus il prend en charge Python sur plusieurs systèmes d'exploitation.

Notre interface graphique fonctionne de cette manière : 

L'utilisateur peu écrire un tweet (existant ou non) dans cette zone de saisie : 


![interface](/image/interface1.png "image1.")


Saisir l'algorithme de classification a utilisé ainsi que ces paramètres.


![interface](/image/interface2.png "image2.")



Il aura ensuite le résultat de classification de son tweet. C'est-à-dire si celui-ci est plutôt positif, negatif ou neutre.


![interface](/image/resultat.png "image1.")



### Résultats de la classification avec les différentes méthodes et analyse

Recherche par dictionnaire : 

- Matrice de confusion sur 163 données

|          | predict\_positifs | predict\_négatifs | predict\_neutres |
| -------- | ----------------- | ----------------- | ---------------- |
| positifs | 19                | 2                 | 3                |
| négatifs | 23                | 7                 | 3                |
| neutres  | 74                | 10                | 22               |

Prédction réussi pour 23% (38/163) des cas, l'aléatoire est meilleur. L'aléatoire réussi a environ 33% des cas ce qui est suppérieur à ce qu'on obtient.
Ce résultat peut être ajusté en modifiant la base de données du vocabulaire, ou en ajoutant un seuil de tolérence sur les frontières des positifs, négatifs et neutres.


Knn : k=2
Matrice de confusion sur 163 données:
  - 109 base d'apprentissages,
  - 54 base de tests 
    
|          | predict\_positifs | predict\_négatifs | predict\_neutres |
| -------- | ----------------- | ----------------- | ---------------- |
| positifs | 11                | 0                 | 0                |
| négatifs | 0                 | 10                | 0                |
| neutres  | 0                 | 0                 | 33               |

Prédiction réussi pour 100% les données de tests .


Knn : k=3
Matrice de confusion sur 163 données:
  - 109 base d'apprentissages,
  - 54 base de tests
      
|          | predict\_positifs | predict\_négatifs | predict\_neutres |
| -------- | ----------------- | ----------------- | ---------------- |
| positifs | 2                 | 1                 | 8                |
| négatifs | 0                 | 5                 | 5                |
| neutres  | 0                 | 2                 | 31               |

Prédiction réussi pour 70% les données de tests.

Cette réduction de performance pour k allant de 1 à 3 est flagrante. Cela peut s'expliquer par la taille réduite de notre base de tests, car comme il y a peu de données, quand k augmente les voisins on plus de chance de se tomper.




Algorithme de Bayes :  presence du mot (avec 90% de réussite)
Matrice de confusion sur 163 données:

|          | predict\_positifs | predict\_négatifs | predict\_neutres |
| -------- | ----------------- | ----------------- | ---------------- |
| positifs | 7                 | 0                 |   4              |
| négatifs | 0                 | 9                 | 1                |
| neutres  | 0                 | 0                 | 33               |

Algorithme de Bayes :  frequence d'un mot et on ne garde que les mots les plus importants  (avec 92% de réussite)
Matrice de confusion sur 163 données:

|          | predict\_positifs | predict\_négatifs | predict\_neutres |
| -------- | ----------------- | ----------------- | ---------------- |
| positifs | 8                 | 0                 |   3              |
| négatifs | 0                 | 9                 | 1                |
| neutres  | 0                 | 0                 | 33               |



Algorithme de Bayes :  frequence d'un mot  (avec 90% de réussite)
Matrice de confusion sur 163 données:

    
|          | predict\_positifs | predict\_négatifs | predict\_neutres |
| -------- | ----------------- | ----------------- | ---------------- |
| positifs | 7                 | 0                 |   4              |
| négatifs | 0                 | 9                 | 1                |
| neutres  | 0                 | 0                 | 33               |



### Conclusions


À travers ce projet, nous avons réussi à développer des méthodes d'analyse du sentiment des tweets. 
Nous avons utilisé l'API de Twitter et des algorithme de classification basé sur sur plusieurs méthodes pour classer les tweets en catégories positive, négative et neutre.
Chaque méthode nous on donnais un taux de satisfaction différente. 
KNN semble la méthode la plus efficace cependant nos résultats peuvent être biaisé par notre base de données qui n'est pas assez riche. 
Il faudrait donc rajoutez des tweet.
Nous avons aussi créé une interface utilisateur pour visualiser les résultats de l'analyse des sentiments.

Une des grandes difficultés rencontrées dans ce projet et dans le temps, en effet, nous n'avons malheureusement pas bien géré notre temps et nous n'avons pas pu ajoutez toutes les idées que nous voulions implémenter.
Comme par exemple, une option sur l'interface graphique permet de comparer des algorithme de classification entre eux, un graphe montrant une courbe représentatif des sentiments des utilisateurs en fonction du temps et d'un sujet précis, une interface plus "design", d'autres paramètres et variation des algorithme pour avoir de meilleurs résultats, ...

Malgré ces regrets nous avons trouvait le sujet intéressant, celui-ci nous a permis d'avoir une petite expérience dans le domaine du machine learning.
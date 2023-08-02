import re
from turtle import st

class Filter():

    def __init__(self):
        self.atUser =  "@\w+[:\.!]*"
        self.addSpace = "\s*([!\?\"\.;,])\s*"
        self.moneySign = "([\$€£])\d[\.,\d]*"#|\d[\.\d\d]*([\$|€|£])"
        self.percetage = "([0-9]{1,2}[\.,\d]*\%)"
        self.hashtag =  "#\w+"
        self.url = "(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])"

        self.mots_sans_sens = " mon | mn | ma | mes | ms| ton | tn | ta | tes | son | sa | ses | notre | nos | votre | vos , leur | leurs | le | la | les | l'| l |  un | une | des | ce | cette | cet | ces | ça | ca | ceci | cela | dans | ds | c | je | j' | moi | me | m' | moi | tu | toi | te | t' | il | lui | elle | nous | vous | ils | eux | elles "

    def removeUsername(self, tweet):
        return re.sub(self.atUser, "", tweet)

    def surroundCharWSpace(self, tweet):
        return re.sub(self.addSpace, r' \1 ', tweet) 

    def removeMoneyValue(self, tweet):
        return re.sub(self.moneySign, r'\1XX', tweet)

    def removePercentValue(self, tweet):
        return re.sub(self.percetage, "XX%", tweet)

    def removeUrl(self, tweet):
        return re.sub(self.url, "", tweet)

    def removeHashtag(self, tweet):
        return re.sub(self.hashtag, "", tweet)

    def removeNoSens(self, tweet):
        return re.sub(self.mots_sans_sens, " ", tweet)

    def filter2(self, tweet):
        return self.removeUsername(self.surroundCharWSpace(self.removeMoneyValue(self.removePercentValue(self.removeUrl(self.removeHashtag(tweet)))))).lower()

    def filter(self, tweet):
        return self.removeUsername(self.surroundCharWSpace(self.removeMoneyValue(self.removePercentValue(self.removeUrl(self.removeHashtag(self.removeNoSens(tweet))))))).lower()

# filter = Filter()

# print(filter.removeUsername("test 0 : @username"))
# print(filter.removeMoneyValue("test 1 : $45.45555"))
# print(filter.removeMoneyValue("test 2 : €45.21"))
# print(filter.removeMoneyValue("test 2bis : €45,22"))
# print(filter.removeMoneyValue("test 3 : £45"))
# print(filter.removePercentValue("test 4: 20%"))
# print(filter.removePercentValue("test 5: 20.45%"))
# print(filter.removePercentValue("test 5bis: 20,4%"))
# print(filter.removeHashtag("test 6: RT @art_svirid: Hi @WHO #COVID?  Protect yourself and others in 6steps:"))
# print(filter.removeUrl("test 7 : https://stackoverflow.com/questions/6038061/regular-expression-to-find-urls-within-a-string"))

# print(filter.filter("@username $45.45 20.45% wow!"))

# l = [" / ( [ ! \ ? \" \ . ; , ] ) /", " /(\\ $ ?\d [ \ . \ d\d ] * ) /",  " /([0-9]{1 ,2}\% ) /" ]

# def x(t):
#     return str(t.replace(" ", "")[1:-1])

# for i in l:
#     print(x(i))

# l  = " mon ; mn ; ma ; mes ; ms; ton ; tn ; ta ; tes ; son ; sa ; ses ; notre ; nos ; votre ; vos , leur ; leurs ; le ; la ; les ; l'; l ;  un ; une ; des ; ce ; cette ; cet ; ces ; ça ; ca ; ceci ; cela ; dans ; ds "

# def f(l):
#     return '('+l.replace(";", "|")+')'

# print(f(l))
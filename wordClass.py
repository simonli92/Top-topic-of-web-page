class KeyWord(object):
    def __init__(self, word):
        self.keyword = word
        #key is tag name, value is appear times, easily inspect and change weight
        self.times = {}
        #weight of different tag
        self.tag_weight = {"title" : 60,  "strong": 5, "h": 1.5 ,"p": 1,"div" : 1, "span" :0.1, "other": 0.01}
        self.score = 0
        #build positional index: key is sentence id, value is list of position of the word
        self.pos_dict = {}

    def addtimes(self, tag_name):
        if tag_name in self.times:
            self.times[tag_name] += 1
        elif (tag_name not in self.times):
            self.times[tag_name] = 1
        if tag_name in self.tag_weight:
            self.score +=self.tag_weight[tag_name]
        elif "h" in tag_name:
            self.score +=self.tag_weight["h"]
        else:
            self.score += self.tag_weight["other"]

    #build positional index
    def add_pos(self, sentenceId, pos):
        if sentenceId not in self.pos_dict:
            self.pos_dict[sentenceId] = []
        self.pos_dict[sentenceId].append(pos)

    #print object and can see the score for the word
    def __str__(self):
        return "word=%s: score=%.2f" % (self.keyword,self.score)

    #make object can be checked in dictionary or set
    def getHashables(self):
        return (self.keyword, ) # return a tuple of hashables

    def __hash__(self):
        return hash(self.getHashables())

    def __eq__(self, other):
        return (isinstance(other, KeyWord) and (self.keyword == other.keyword))
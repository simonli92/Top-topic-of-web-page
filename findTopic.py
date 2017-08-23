import sys
import re
import wordClass
import parseHTML

#if missing lib, run nltk.download()
#dir:corpora-stopword
from nltk.corpus import stopwords
#dir: corpora-wordnet
from nltk.stem import WordNetLemmatizer
#dir: models-punkt
from nltk import word_tokenize



#not include meta tag
# can add or delete depending on different situation
useless_tag = {"html", "head", "script", "style", "img", "input", "option", "link"}

#clean up each sentence:tokenization, normalization, stemming and stop words
def cleanup_words(string):
    stopwords_List =  stopwords.words("english")
    wordnet_lemmatizer = WordNetLemmatizer()
    stopwords_set = set(stopwords_List)
    cleanup_list = []

    try:
        tokens = word_tokenize(string)
        for word in tokens:
            word_lowercase = word.lower()
            if (re.match(r'[\w]+', word_lowercase)) :
                stemming_word = wordnet_lemmatizer.lemmatize(word_lowercase)
                if stemming_word not in stopwords_set:
                    cleanup_list.append(stemming_word)
        return cleanup_list
    except UnicodeEncodeError :
        print("Unicode error")
        return cleanup_list


#for demo, find top single word and continuous top double word
def create_wordDict(data):
    single_word_set = {}
    double_word_set = {}
    sentenceId = 0
    for tag in data.find_all(True):
        tagname=tag.name.lower()
        #do not care about useless tag's data
        if tagname not in useless_tag:
            str = tag.string
            if str != None:
                sentenceId += 1
                clean_list = cleanup_words(str)
                l = len(clean_list)
                for i in range(l):
                    #build single word dict
                    word = clean_list[i]
                    if word not in single_word_set:
                        single_word_set[word] = wordClass.KeyWord(word)
                    single_word_set[word].addtimes(tagname)
                    single_word_set[word].add_pos(sentenceId, i)

                    #build continuous double word dict
                    if i >= 1 and l > 1:
                        double_word = clean_list[i-1] + " " + clean_list[i]
                        if double_word not in double_word_set:
                            double_word_set[double_word] = wordClass.KeyWord(double_word)
                        double_word_set[double_word].addtimes(tagname)
                        double_word_set[double_word].add_pos(sentenceId, i)

    #transform dict to list
    single_word_list = [v for v in single_word_set.values()]
    #sort the list by score
    sorted_single_word_list = sorted(single_word_list, key=lambda x: x.score, reverse=True)
    single_word_top_list =[]
    for keyword in sorted_single_word_list:
        #only get the word has more than 60 point
        if keyword.score >= 60:
            single_word_top_list.append(keyword.keyword)
        else:
            break
    double_word_list = [v for v in double_word_set.values()]
    sorted_double_word_list = sorted(double_word_list, key=lambda x: x.score, reverse=True)
    double_word_top_list =[]
    for keyword in sorted_double_word_list:
        if keyword.score >= 60:
            double_word_top_list.append(keyword.keyword)
        else:
            break
    return (single_word_top_list,double_word_top_list)



if __name__ == '__main__':
    data = parseHTML.fetch_page(sys.argv[1])
    (single_word_top_list,double_word_top_list) = create_wordDict(data)
    print(single_word_top_list)
    print(double_word_top_list)

# for tag in data.find_all("div", class_="ad"):
#     print (tag)

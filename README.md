# Top-topic-of-web-page
Find and print top topic of a web page by python

## Files

parseHTML.py – Retrieve and parse html page from input url by urllib and BeautifulSoup.

findTopic.py – Main file. Find and print top single word list and top double word list from the html page to the console.

wordClass.py – Build KeyWord object to store and calculate scores for different word.

## Dependencies

Python v3.4.3

Nltk v3.2.4

Beautiful Soup v4.4.0

## Install

For nltk packages:

Run nltk.download() and a GUI will show up.

Under Corpora, download stopwords and wordnet.

Under Models, download punkt.

For beautiful soup:
```
pip3 install beautifulsoup4 
```

## Run
In the command window or terminal, run:
```
python findTopic.py <your_url>
```

## Working

Input a url, output a list of common topics that best describe the page.

A soup object contains all the data in html page under certain format.

The KeyWord Object contains the score for the word, a dictionary that shows the word displayed in certain tag and the times, a dictionary for the word’s positional index.

The clean up word function is used to tokenize the string into a word list, normalize the word into lower case, stemming the word and remove stopwords by the list that nltk provides.


The create word dict function iterates the whole soup object by tag and store proper data into KeyWord object. Here simply fetch the top single words and the top 2-gram words from the html page.


## Future Work

There will be a lot that can be improved for the project. 

1. The positional index built in each word object can be used to assemble more meaningful queries. Here is the link for the algorithm: https://nlp.stanford.edu/IR-book/html/htmledition/positional-indexes-1.html

2. Different level of tags should have different weights. Also, the weight can be trained by gradient decent if having a training data set.

3. Class name or id name in the tag can be considered into determine the weight of the word.

4. Word2vec model can be used to find synonyms and create n-gram query. 

5. Meta tag content can be used to identify misspells but never used in defining the content of the page.

6. Regular expression can be more specific.


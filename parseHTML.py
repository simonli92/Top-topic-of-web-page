import urllib.request, urllib.error
import sys
from bs4 import BeautifulSoup

def fetch_page(siteURL):
    #newest and usable header
    header = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13'
    }
    try:
        req = urllib.request.Request(siteURL, data = None, headers = header)
        res= urllib.request.urlopen(req).read().decode("utf-8",'ignore')
    except urllib.error.URLError as e:
        print ("reason: " + e.reason)
        return
    except urllib.error.HTTPError as e:
        print ("Http error: " + e.code)
        return
    soup = BeautifulSoup(res, 'html.parser')
    if soup :
       return soup
    else:
        print("No data available")
        return



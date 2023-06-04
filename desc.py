from bs4 import BeautifulSoup
import requests
def extract_desc(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"lxml")
    head=soup.find("head")
    try:
        desc=head.find("meta",attrs={'name':'description'}).get("content")
    except Exception as e:
        desc=""
        print(e)
    return desc

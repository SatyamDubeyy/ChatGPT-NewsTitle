from newspaper import Article
from urllib.parse import urlparse
from chat import generateTitles
import os
url=input("Enter URL: ")
title=""
def bbcExt(url):
    import requests
    from bs4 import BeautifulSoup
    r=requests.get(url)
    soup=BeautifulSoup(r.text,"lxml")
    main=soup.find("main")
    allB=main.find_all("div",{"data-component" : "text-block"})
    s=""
    for B in allB:
        s+="\n"
        s+=B.getText()

    f = open(PATHH+"\\desc.txt", "w")
    f.write(s)
    f.close()

if not os.path.exists('text_files'):
    os.makedirs('text_files')
PATHH=os.getcwd()+"\\text_files"
domain = urlparse(url).netloc
article=Article(url)
article.download()
article.parse()
f = open(PATHH+"\\title.txt", "w")
f.write(url+"\n")
title=article.title
f.write(title)
f.close()
if(domain=="www.bbc.com"):
    bbcExt(url)
else:
    f = open(PATHH+"\\desc.txt", "w")
    f.write(article.text)
    f.close()
n=0
text_title_list=[]
while(True):
    resTitle=generateTitles(title)
    n+=1
    titles=resTitle.strip().split("\n")[2:]
    # print(titles)
    for title in titles:
        if(len(text_title_list)>=6):
            break
        sp=title.split(". ")
        sp.pop(0)
        fin_title=". ".join(sp)
        if(len(fin_title)>=50 and len(fin_title)<=70 and fin_title not in text_title_list):
            f = open(PATHH+f"/title_{len(text_title_list)+1}.txt", "w")
            f.write(fin_title)
            text_title_list.append(fin_title)
            f.close()
    if(len(text_title_list)>=6 or n>3):
        break
for title in text_title_list:
    print(title,len(title)) #printing titles along with character counts
print("Completed")
    

    


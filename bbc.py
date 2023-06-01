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

    # f = open(PATHH+"\\desc.txt", "w")
    # f.write(s)
    # f.close()
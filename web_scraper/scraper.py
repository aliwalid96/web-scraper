import requests

# URL="https://pythonguides.com/python-pygame-tutorial/"
# res=requests.get(URL)
# print  ("hello")


from bs4 import BeautifulSoup

URL ="https://en.wikipedia.org/wiki/History_of_Mexico"

def get_citations_needed_count(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content,"html.parser")
    body_div = soup.find('div', id='content')
    bodycontent= body_div.find('div', id = 'bodyContent')
    text_content = bodycontent.find('div', id ='mw-content-text')
    paragraphs = text_content.findAll("p")
    paragraphs_wthout_citations =[]
    for i in paragraphs:
        if not i.find('sup', class_='reference'):
            paragraphs_wthout_citations.append(i.get_text())
            
   
    return len(paragraphs_wthout_citations)


def get_citations_needed_report(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content,"html.parser")
    body_div = soup.find('div', id='content')
    bodycontent= body_div.find('div', id = 'bodyContent')
    text_content = bodycontent.find('div', id ='mw-content-text')
    paragraphs = text_content.findAll("p")
    paragraphs_wthout_citations =[]
    for i in paragraphs:
        if not i.find('sup', class_='reference'):
            paragraphs_wthout_citations.append(i.get_text())
    
    str1="{citation needed here}\n".join(paragraphs_wthout_citations)
    return str1
    
            
print( f"The number of paragraphs without citations is: {get_citations_needed_count(URL)}")
print(get_citations_needed_report(URL))   

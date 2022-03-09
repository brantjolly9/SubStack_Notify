import requests
from bs4 import BeautifulSoup
from 

def get_stack_url_book(stackListPath = 'Stack_List.txt'):
    stackBook = {}
    with open(stackListPath, 'r') as sl:
        for name in sl.readlines():
            name = name.strip()
            stackBook[name] = r'https://' + name + '.substack.com?sort=new'
    return stackBook

def get_stack(url):
    res = None
    try:
        res = requests.get(url, timeout=20)
        return res.content
    except requests.exceptions.InvalidSchema as e:
        print('Invalid Schema')
        return None
    except Exception as e:
        print(e)
        return None
    
def get_recent_article(pageContent):
    soup = BeautifulSoup(pageContent, features='html.parser')
    
    print(type(soup))
    
    

stackBook = get_stack_url_book()
for item in stackBook.items():
    stackUrl = item[1]
    pageContent = get_stack(stackUrl)
    if pageContent:
        art = get_recent_article(pageContent)
    
    
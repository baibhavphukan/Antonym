import requests
from bs4 import *
url = "https://www.synonyms.com/antonyms/"
word = input("Enter your word:")
url = url + word
headers={'User-Agent': 'Mozilla/5.0'}
data = requests.get(url, headers = headers)
soup = BeautifulSoup(data.text,"html.parser")
data2 = soup.find('p',{'class':'ants'})
data3 = data2.find_all('a')
f = open("antonyms.txt","w")
for i in range(len(data3)):
    f.write(str(data3[i].contents[0]) + '\n')
f.close()

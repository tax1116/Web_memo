import requests
from bs4 import BeautifulSoup

url = 'https://sports.news.naver.com/wfootball/news/read.nhn?oid=417&aid=0000456627'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

og_image = soup.select_one('meta[property="og:image"]')
og_title = soup.select_one('meta[property="og:title"]')
og_description = soup.select_one('meta[property="og:description"]')

#print(og_image,og_title,og_description)

url_image = og_image['content']
url_title = og_title['content']
url_description = og_description['content']

print(url_image, url_title, url_description)
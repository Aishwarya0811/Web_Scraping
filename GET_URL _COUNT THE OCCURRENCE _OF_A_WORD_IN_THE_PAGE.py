import requests
from bs4 import BeautifulSoup
url = 'https://python-forum.io/Thread-How-to-find-a-specific-word-in-a-webpage-and-How-to-count-it'
the_word = 'code'
r = requests.get(url, allow_redirects=False)
soup = BeautifulSoup(r.content, 'lxml')
words = soup.find(text=lambda text: text and the_word in text)
count = len(words)
print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, the_word))

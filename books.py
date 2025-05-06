from __future__ import division
import nltk
import re
import pprint
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.error

nltk.download('punkt_tab')

# Hardcoded URL of a book (e.g., Pride and Prejudice from Project Gutenberg)
url = "https://www.goodreads.com/book/show/53138095-a-court-of-silver-flames?from_search=true&from_srp=true&qid=I4qsk8V925&rank=1"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    # Print only the <div> tags and their contents
    divs = soup.find('section', class_='ReviewText ReviewText--hideContent')
    for div in divs:
        print(div.prettify())  # This prints each <div> and its content nicely formatted

except urllib.error.URLError as e:
    print(f"URL Error: {e}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
    
#tokenize the text
if div:
    text = div.get_text()
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    print(tokens)
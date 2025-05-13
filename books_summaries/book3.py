from __future__ import division
import nltk
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.error

nltk.download('punkt_tab')


# Hardcoded URL of a book (Things We Hide from the Light by Lucy Score) PW 3/3/2023
url = "https://www.publishersweekly.com/9781728276113"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    # Print only the <div> tags and their contents
    divs3 = soup.find('div', class_="text-body mdc-typography--body1 font-source-serif-pro")
    for div3 in divs3:
        print(divs3.prettify())  # This prints each <div> and its content nicely formatted

except urllib.error.URLError as e:
    print(f"URL Error: {e}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
    
#tokenize the text
if divs3:
    text = divs3.get_text()
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    print(tokens)
    
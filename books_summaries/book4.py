from __future__ import division
import nltk
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.error
import pandas as pd

nltk.download('punkt_tab')


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')

# Hardcoded URL of a book (A ​Court of Silver Flames by Sarah J. Maas) PW 3/7/2022
#genre: fantasy
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
    divs4 = soup.find('div', class_="DetailsLayoutRightParagraph__widthConstrained")
    for div in divs4:
        print(divs4.prettify())  # This prints each <div> and its content nicely formatted

except urllib.error.URLError as e:
    print(f"URL Error: {e}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
long_text = "  Enter the world of Charlie's four unlikely friends, discover their story and their most important life lessons. The boy, the mole, the fox and the horse have been shared millions of times online - perhaps you've seen them? They've also been recreated by children in schools and hung on hospital walls. They sometimes even appear on lamp posts and on cafe and bookshop windows. Perhaps you saw the boy and mole on the Comic Relief T-shirt, Love Wins? Here, you will find them together in this book of Charlie's most-loved drawings, adventuring into the Wild and exploring the thoughts and feelings that unite us all."

# Tokenization: Break down the scraped text into individual tokens (words)
if divs4:
    text = divs4.get_text()
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    print(tokens)
    
# Define a function to tag and count part-of-speech (POS) tags in a list of tokens
def pos_frequency(tokens):
    pos_tags = nltk.pos_tag(tokens) # Tag parts of speech
    pos_only = [tag for word, tag in pos_tags] # Extract just the POS tags (e.g., 'NN', 'VB', etc.)
    pos_counts = Counter(pos_only) # Count frequency of each POS tag

    return pos_counts.most_common()

# Print a DataFrame displaying POS frequencies
print("Chart of all the Parts of Speech within the summary",pd.DataFrame(pos_frequency(tokens)))
# Print the most common POS tags

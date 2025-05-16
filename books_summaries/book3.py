from __future__ import division
import nltk
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.error
import pandas as pd


nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize, word_tokenize  # noqa: E402
from nltk.corpus import stopwords
from collections import Counter
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')



# Hardcoded URL of a book (Things We Hide from the Light by Lucy Score) PW 3/3/2023
#genre: romance
url = "https://www.goodreads.com/book/show/62022434-things-we-hide-from-the-light"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    # Print only the <div> tags and their contents
    divs3 = soup.find('div', class_="TruncatedContent__text TruncatedContent__text--large")
    for div3 in divs3:
        print(divs3.prettify())  # This prints each <div> and its content nicely formatted

except urllib.error.URLError as e:
    print(f"URL Error: {e}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

#summary of the book from the Goodreads website
long_text = "After Chief Nash Morgan is nearly killed in an attack he can’t fully remember, he struggles to get his life back on track—until his brother’s college ex-girlfriend, Lina Solavita, shows up in their small town, igniting a forbidden attraction. She claims she’s there to visit Nash’s brother, Knox, but really she’s tracking a missing Porsche for her work. Lina’s not forthcoming with Nash, and he explodes when he discovers her deception, despite Lina’s insistence it was a “practically insignificant omission of the truth.” Soon, however, the couple faces a bigger problem: a local crime boss is out for Nash’s head, along with those of his soon-to-be sister-in-law and niece. Meanwhile, Lina and Nash’s chemistry ignites—but an unexpected villain is determined to end their affair. By romance standards, this is a brick, but Score keeps the pages turning with a twisty, danger-laced plot; feisty leads; and blazing passion (which produces “not just any run-of-the-mill, I-could-have-done-better-with-a-vibrator orgasms”). This lively tale will delight series fans."
    
#tokenize the text
if divs3:
    text = div3.get_text()
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    print(tokens)    


def pos_frequency(tokens):
    pos_tags = nltk.pos_tag(tokens) # Tag parts of speech
    pos_only = [tag for word, tag in pos_tags] # Extract just the POS tags (e.g., 'NN', 'VB', etc.)
    pos_counts = Counter(pos_only) # Count frequency of each POS tag

    return pos_counts.most_common()

print("Chart of all the Parts of Speech within the summary",pd.DataFrame(pos_frequency(tokens)))
 
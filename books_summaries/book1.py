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


# Hardcoded URL of a book (The Let Them Theory: A Life-Changing Tool That Millions of People Can’t Stop Talking About by Mel Robbins) PW 3/3/2025
#Genre: non-fiction
url = "https://www.publishersweekly.com/9781401971366"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    # Print only the <div> tags and their contents
    divs1 = soup.find('div', class_="text-body mdc-typography--body1 font-source-serif-pro")
    for div in divs1:
        print(divs1.prettify())  # This prints each <div> and its content nicely formatted

except urllib.error.URLError as e:
    print(f"URL Error: {e}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


long_text = "outlines how accepting others for who they are and focusing instead on the actions one can take to improve things—what she calls the “let them/let me” method—helps reveal what’s within one’s control and how to manage one’s actions accordingly. Those dealing with difficult family members, for example, should avoid trying to change their opinions (“Let your dad be your dad”) and focus on building the “kind of relationship I want” with them, “based on the kind of person I want to be.” Similarly, those struggling with the tendency to compare themselves to others should recognize that harping on someone else’s advantages drains motivation for changing one's own life. In down-to-earth prose, the author lucidly distinguishes her theory from simply “letting go,” noting that “accepting the reality of your situation doesn’t mean you’re surrendering to it” but rather releasing “control you never had.” Robbins’s fans will want to snap this up."

 #makes the summaries more comapct for easier classifying   
def extractive_summary(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if w.isalpha() and w not in stop_words]

    word_freq = Counter(words)
    sentence_scores = {}
    for sent in sentences:
        sentence_words = word_tokenize(sent.lower())
        score = sum(word_freq.get(word, 0) for word in sentence_words if word in word_freq)
        sentence_scores[sent] = score

    # Return the top-ranked sentence
    return max(sentence_scores, key=sentence_scores.get)

# Tokenization: Break down the scraped text into individual tokens (words)
if divs1:
    text = divs1.get_text()
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

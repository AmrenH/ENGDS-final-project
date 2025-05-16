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

# Hardcoded URL of a book (Mostly What God Does: Reflections on Seeking and Finding His Love Everywhere) PW 3/3/2024
#genre: non-fiction, insirpational 
url = "https://www.publishersweekly.com/9781400341122"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
    req = Request(url, headers=headers)
    response = urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    # Print only the <div> tags and their contents
    divs2 = soup.find('div', class_="text-body mdc-typography--body1 font-source-serif-pro")
    for div2 in divs2:
        print(divs2.prettify())  # This prints each <div> and its content nicely formatted

except urllib.error.URLError as e:
    print(f"URL Error: {e}")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
long_text = "makes her adult debut with a poignant account of the role that religious faith has played in her life. Raised in a sin-obsessed Baptist church, Guthrie grew up burdened with intermittent guilt for “being shallow, for being ambitious... for not being more forward in my faith.” In her 30s, she was stuck in an unhappy marriage when it hit her “like a comet” that God “was, in fact, in the midst of rescuing me.” The realization sparked a renewed faith in Jesus’s love (“Mostly what God does is love us,” she writes; therefore, he “truly intends us to love ourselves”). From there, Guthrie explores prayer as a method of processing “feelings and emotions and concerns in the presence of God”; doubt as “faith being worked out, like a muscle”; and everyday kindness as a “way we transmit the love of God,” even if it’s just by “look[ing] someone in the eye, offer[ing] our coat, or invit[ing] a stranger to sit with us.” Through her candidness about the challenges she’s tackled—including the death of her often “mercurial and terrifying” father when she was 16 and her abbreviated first marriage—Guthrie persuasively renders the evolution of a hard-won religious belief that makes room for imperfection and “does not require us to ignore... the sorrows we experience or the unjustness we see but to believe past it.” This openhearted offering inspires."


#tokenize the text
if divs2:
    text = divs2.get_text()
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    print(tokens)
    

def pos_frequency(tokens):
    pos_tags = nltk.pos_tag(tokens) # Tag parts of speech
    pos_only = [tag for word, tag in pos_tags] # Extract just the POS tags (e.g., 'NN', 'VB', etc.)
    pos_counts = Counter(pos_only) # Count frequency of each POS tag

    return pos_counts.most_common()

print("Chart of all the Parts of Speech within the summary",pd.DataFrame(pos_frequency(tokens)))
    

    
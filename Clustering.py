import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

#create a dictionary of book summaries
summaries = {
    "Book 1": "outlines how accepting others for who they are and focusing instead on the actions one can take to improve things—what she calls the “let them/let me” method—helps reveal what’s within one’s control and how to manage one’s actions accordingly. Those dealing with difficult family members, for example, should avoid trying to change their opinions (“Let your dad be your dad”) and focus on building the “kind of relationship I want” with them, “based on the kind of person I want to be.” Similarly, those struggling with the tendency to compare themselves to others should recognize that harping on someone else’s advantages drains motivation for changing one's own life. In down-to-earth prose, the author lucidly distinguishes her theory from simply “letting go,” noting that “accepting the reality of your situation doesn’t mean you’re surrendering to it” but rather releasing “control you never had.” Robbins’s fans will want to snap this up.",
    "Book 2" : "From there, Guthrie explores prayer as a method of processing “feelings and emotions and concerns in the presence of God”; doubt as “faith being worked out, like a muscle”; and everyday kindness as a “way we transmit the love of God,” even if it’s just by “look[ing] someone in the eye, offer[ing] our coat, or invit[ing] a stranger to sit with us.” Through her candidness about the challenges she’s tackled—including the death of her often “mercurial and terrifying” father when she was 16 and her abbreviated first marriage—Guthrie persuasively renders the evolution of a hard-won religious belief that makes room for imperfection and “does not require us to ignore... the sorrows we experience or the unjustness we see but to believe past it.” This openhearted offering inspires.",
    "Book 3" : "Nash Morgan was always known as the good Morgan brother, with a smile and a wink for everyone. But now, this chief of police is recovering from being shot and his Southern charm has been overshadowed by panic attacks and nightmares. He feels like a broody shell of the man he once was. Nash isn’t about to let anyone in his life know he’s struggling. But his new next-door neighbor, smart and sexy Lina, sees his shadows. As a rule, she’s not a fan of physical contact unless she initiates it, but for some reason Nash’s touch is different. He feels it too. The physical connection between them is incendiary, grounding him and making her wonder if exploring it is worth the risk.",
    "Book 4" : "Nesta Archeron has always been prickly-proud, swift to anger, and slow to forgive. And ever since being forced into the Cauldron and becoming High Fae against her will, she's struggled to find a place for herself within the strange, deadly world she inhabits. Worse, she can't seem to move past the horrors of the war with Hybern and all she lost in it. The one person who ignites her temper more than any other is Cassian, the battle-scarred warrior whose position in Rhysand and Feyre's Night Court keeps him constantly in Nesta's orbit. But her temper isn't the only thing Cassian ignites. The fire between them is undeniable, and only burns hotter as they are forced into close quarters with each other. Meanwhile, the treacherous human queens who returned to the Continent during the last war have forged a dangerous new alliance, threatening the fragile peace that has settled over the realms. And the key to halting them might very well rely on Cassian and Nesta facing their haunting pasts. Against the sweeping backdrop of a world seared by war and plagued with uncertainty, Nesta and Cassian battle monsters from within and without as they search for acceptance-and healing-in each other's arms.",
    "Book 5" : "Enter the world of Charlie's four unlikely friends, discover their story and their most important life lessons. The boy, the mole, the fox and the horse have been shared millions of times online - perhaps you've seen them? They've also been recreated by children in schools and hung on hospital walls. They sometimes even appear on lamp posts and on cafe and bookshop windows. Perhaps you saw the boy and mole on the Comic Relief T-shirt, Love Wins? Here, you will find them together in this book of Charlie's most-loved drawings, adventuring into the Wild and exploring the thoughts and feelings that unite us all.",
}

# Step 1: Convert summaries to TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(summaries.values())

# Step 2: Cluster the TF-IDF vectors
k = 2  # Try different values (2, 3, 4, etc.)
kmeans = KMeans(n_clusters=2, random_state=42)
labels = kmeans.fit_predict(X)

# Step 3: Create a DataFrame with cluster labels
df = pd.DataFrame({
    'Book': list(summaries.keys()),
    'Summary': list(summaries.values()),
    'Cluster': labels
})

print(df)

# Step 4: Reduce TF-IDF vectors to 2D for plotting
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X.toarray())

# Step 5: Visualize clusters in 2D
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X_2d[:, 0], y=X_2d[:, 1], hue=labels, palette='Set2', s=100)

# Add book titles to each point
for i, title in enumerate(summaries.keys()):
    plt.text(X_2d[i, 0] + 0.01, X_2d[i, 1], title, fontsize=9)

plt.title("TF-IDF Clustering of Book Summaries")
plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.legend(title="Cluster")
plt.tight_layout()
plt.show()

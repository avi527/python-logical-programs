
from wordcloud import WordCloud, STOPWORDS
import wordcloud
from PIL import Image
import urllib
import requests
import numpy as np
import matplotlib.pyplot as plt

words = 'Avinash singh Avinash singh Avinash singh Avinash singh Avinash singh Avinash singh access guest guest apartment area area bathroom bed bed bed bed bed bedroom block coffee coffee coffee coffee entrance entry francisco free garden guest home house kettle kettle kitchen kitchen kitchen kitchen kitchen kitchenliving located microwave neighborhood new park parking place privacy private queen room san separate seperate shared space space space street suite time welcome'
mask = np.array(Image.open(requests.get('http://www.clker.com/cliparts/O/i/x/Y/q/P/yellow-house-hi.png', stream=True).raw))

# This function takes in your text and your mask and generates a wordcloud. 
def generate_wordcloud(words, mask):
    word_cloud = WordCloud(width = 300, height = 200, background_color='pink', stopwords=STOPWORDS, mask=mask).generate(words)
    plt.figure(figsize=(8,6),facecolor = 'yellow', edgecolor='red')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    
#Run the following to generate your wordcloud
generate_wordcloud(words, mask)

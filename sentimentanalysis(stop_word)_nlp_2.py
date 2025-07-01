#PRINT ALL STOP WORDS
import nltk

from nltk.corpus import stopwords

#Get english stop words
nltk.download('stopwords')
stop_words= stopwords.words('english')

#Print all stopwords
print("Total Stop Words:", len(stop_words))
print(stop_words)

!pip install textblob

from textblob import TextBlob
from textblob import download_corpora
from nltk.corpus import stopwords
from nltk.tokenize  import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')

text= "This movie is not good."
#Sentiment with all words (no stopword removal)

blob_original= TextBlob(text)
print("Original Sentence", text)
print("Sentiment (with 'not'):", blob_original.sentiment)

text='i am not sleeping.'
blob_original= TextBlob(text)
print("Original Sentence", text)
print("Sentiment (with 'not'):", blob_original.sentiment)

nltk.download('punkt_tab')

#Sentiment after removing stop words
stop_words = set(stopwords.words('english'))

#Remove stopwords
Tokens = word_tokenize(text)
filtered_tokens= [word for word in Tokens if word.lower() not in stop_words]
filtered_text= ' '.join(filtered_tokens)
filtered_text

custom_stopwords = set(stop_words) - {'not','no','never'}
print("Stop words after excluding 'not', 'no', 'never':")
print(sorted(custom_stopwords))

#Remove stopword - excluding not, never, no
Tokens = word_tokenize(text)
filtered_tokens= [word for word in Tokens if word.lower() not in custom_stopwords]
filtered_text= ' '.join(filtered_tokens)
filtered_text

#2B - STEMMING AND LEMMATIZATION

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
#nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("running", pos="v"))      #RUN
print(lemmatizer.lemmatize("better", pos="a"))       #GOOD

#Popular stemmer in NLTK
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem("running"))
print(stemmer.stem("better"))
print(stemmer.stem("responsibilities"))


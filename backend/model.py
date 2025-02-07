import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer

# Load dataset
city = pd.read_csv("../cities.csv")

# Data Cleaning
city = city.drop(['Best_time_to_visit'], axis=1, errors='ignore')  # Ignore if column doesn't exist
city = city.dropna()

# Convert descriptions to lowercase
city['City_desc'] = city['City_desc'].apply(lambda x: x.lower())

# Initialize Porter Stemmer
ps = PorterStemmer()

def stem(text):
    return " ".join([ps.stem(word) for word in text.split()])

# Apply stemming
city['City_desc'] = city['City_desc'].apply(stem)

# Convert text to vector representation
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(city['City_desc']).toarray()

# Compute cosine similarity
similarity = cosine_similarity(vectors)

# Function to get city recommendations
def recommend(city_name, top_n=5):
    city_name = city_name.lower()
    
    try:
        city_index = city[city['City'].str.lower() == city_name].index[0]
    except IndexError:
        return []

    distances = similarity[city_index]
    city_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:top_n+1]
    
    return [city.iloc[i[0]].City for i in city_list]

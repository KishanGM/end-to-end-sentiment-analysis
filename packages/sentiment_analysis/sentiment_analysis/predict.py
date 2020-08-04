import nltk
import numpy as np
import pandas as pd 
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def make_predictions(strinput) -> str:
    sinput = str(strinput)
    if sinput.isdecimal():
        return "Provide some non numerical and meaningful snetences as input"
    else:
        sid = SentimentIntensityAnalyzer()
        scores = sid.polarity_scores(sinput)
        compound = scores['compound']
        if compound > 0:
            return "Positive"
        elif compound <0:
            return "Negitive"
        else:
            return "Neutral"
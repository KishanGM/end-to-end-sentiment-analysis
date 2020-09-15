import random
from sentiment_analysis.predict import make_predictions

def test_make_prediction():
    # Given
    input1 = "This is a VERY GOOD movie !"
    input2 = "This is a VERY BAD movie !"
    input3 = "This is neither a good nor a bad movie" 
    inputs = [input1,input2,input3] 
    # When
    subject = make_predictions(random.choice(inputs))
    
    # Then
    assert subject is not None
    assert ((subject == 'Positive' )or (subject  == 'Negative') or(subject  == 'Neutral') or (subject == 'Provide non-numerical and meaningful sentences as input')) 
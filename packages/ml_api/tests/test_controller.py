from sentiment_analysis.config import config as model_config
#from sentiment_analysis.processing.data_management import load_dataset
from sentiment_analysis import __version__ as _version

import json
import math
import random
from api import __version__ as api_version

def test_health_endpoint_returns_200(flask_test_client):
    # When
    response = flask_test_client.get('/health')

    # Then
    assert response.status_code == 200




def test_version_endpoint_returns_version(flask_test_client):
    # When
    response = flask_test_client.get('/version')

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json['model_version'] == _version
    assert response_json['api_version'] == api_version



def test_prediction_endpoint_returns_prediction(flask_test_client):
    # Given
    # Load the test data from the regression_model package
    # This is important as it makes it harder for the test
    # data versions to get confused by not spreading it
    # across packages.
    input1 = "This is a VERY GOOD movie !"
    input2 = "This is a VERY BAD movie !"
    input3 = "This is neither a good nor a bad movie" 
    inputs = [input1,input2,input3] 
    # When
    subject = random.choice(inputs)
    post_json = {'input':subject}

    # When
    response = flask_test_client.post('/predict',
                                      json=post_json)

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    prediction = response_json['predictions']
    #response_version = response_json['version']
    assert prediction is not None
    assert ((prediction  == 'Positive' )or (prediction   == 'Negative') or(prediction   == 'Neutral') or (prediction  == 'Please provide a non-numerical and meaningful sentence(s) to determine sentiment')) 


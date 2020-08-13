from flask import Blueprint, Flask, request, jsonify, render_template
from sentiment_analysis.predict import make_predictions
from sentiment_analysis import __version__ as _version

from api.config import get_logger
from api import __version__ as api_version

_logger = get_logger(logger_name=__name__)


prediction_app = Blueprint('prediction_app', __name__,template_folder='templates')


@prediction_app.route('/')
def home():
    return render_template('index.html')


@prediction_app.route('/predict',methods=['POST'])
def predict():

    text = request.form['question']
    _logger.info(f'Inputs: {text}')
    #final_features = [np.array(int_features)]
    prediction = make_predictions(text)

    output = prediction

    return render_template('index.html', prediction_text='Sentiment is {}'.format(output))


#@prediction_app.route('/v1/predict/sentiment_analysis', methods=['POST'])
#def predict():
#    if request.method == 'POST':
#        json_data = request.get_json()
#        _logger.info(f'Inputs: {json_data}')
#
#        predictions  = make_predictions(json_data['input'])
#        _logger.info(f'Outputs: {predictions}')
#        #version = predictions.get('version')
#
#        return jsonify({'predictions': predictions})




@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'




@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version,
                        'api_version': api_version})



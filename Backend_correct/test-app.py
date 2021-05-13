from flask import Flask, request, jsonify, make_response
from predict import predict_model
import time
import json
import flask

app = Flask(_name_)
predict_ = predict_model()
predict_.predict('Khởi tạo lần đầu')


@app.route('/api', methods=['POST'])
def suggest():
    predict_.log.debug('### Request comming, info = ' + str(request.headers))
    # print('json:',request.get_json())
    predict_.log.debug('### json: ' + str(request.get_json()))
    # print('data', request.get_data())
    predict_.log.debug('### data: ' + str(request.get_data()))
    data = json.loads(request.get_data().decode(encoding='utf-8'))
    predict_.log.debug('### enconding data : ' + str(data))
    result = {}
    sent = data['sentence']
    result = predict_.predict(sent)
    # print(jsonify(result))

    res = make_response(jsonify(result))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res


if _name_ == '_main_':
    app.run(host='127.0.0.1', port=8890, use_debugger=False, debug=False)
    # app.run(host='192.168.0.109', port=8890)
    # app.run(debug=True)

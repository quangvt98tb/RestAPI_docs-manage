from flask import Flask, render_template, url_for, request, make_response, jsonify
from flask_cors import CORS
import bogo as bg
import re
import functions.spell_correction as spell
import functions.process_rawdata as pdata
# import functions.text_classifier as classifier

app = Flask(__name__)
CORS(app)


@app.route('/api/spell', methods=['POST'])
def process():
    if request.method == 'POST':
        raw_text = request.json.get('content')
        pattern = '\s'
        list_word_sentence, list_word_raw, sentence_raw = pdata.process_data(
            raw_text)
        check_num = re.split(pattern, sentence_raw)
        if len(check_num) > 4:
            out_put = spell.correct(sentence_raw)

            output = re.split(pattern, out_put)
            index = 0
            for wd in list_word_sentence:

                if wd['type'] == 0:
                    wd['word'] = output[index]
                    index = index + 1
        # list raw and correct
        list_raw = []
        list_correct = []
        for (index, wordd) in enumerate(list_word_sentence):
            if wordd['type'] == 0:
                if wordd['word'] != list_word_raw[index]['word']:
                    list_raw.append(list_word_raw[index])
                    list_correct.append(wordd)

        sentence = ''
        for word in list_word_sentence:
            if word['type'] == 1:
                sentence = sentence + word['word']
            elif word['type'] == 0:
                sentence = sentence + word['word'] + ' '

        rs = sentence
        dau = '.,;?:!'
        for i in dau:
            i_tag = ' <' + i+'>'
            index = rs.find(i_tag)
            if index == -1:
                rs = rs
            else:
                replace = i + ' '
                rs = rs.replace(i_tag, replace)

        # sentence_raw = ''
        # for word in list_word_raw:
        #     if word['type'] == 1:
        #         sentence_raw = sentence_raw + word['word']
        #     elif word['type'] == 0:
        #         sentence_raw = sentence_raw + word['word'] + ' '

        # rs2 = sentence_raw
        # dau = '.,;?:!'
        # for i in dau:
        #     i_tag = ' <' + i+'>'
        #     index = rs.find(i_tag)
        #     if index == -1:
        #         rs2 = rs2
        #     else:
        #         replace = i + ' '
        #         rs2 = rs2.replace(i_tag, replace)
        data = {
            'sentence_all': rs,
            'listraw': list_word_raw,
            'listcheck': list_word_sentence,
            'list_raw': list_raw,
            'list_correct': list_correct
        }
        res = make_response(jsonify(data))
        res.headers.add("Access-Control-Allow-Origin", "*")
    return res


if __name__ == '__main__':
    app.run(host='localhost', port=8890,  debug=True)

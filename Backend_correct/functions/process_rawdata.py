import re
import bogo as bg

# function


def process_data(text_raw):
    dau = '.,;?:!'
    pattern = '\s'
    pattern1 = '^<'
    pattern2 = '>$'
    pattern3 = '^<[\s|\w|\W]{1,10000}>$'
    # them khoang trang sau >
    text = text_raw.replace('>', '> ')
    text = text.replace('<', ' <')
    text = text.replace('<u>', '')
    text = text.replace('</u>', '')
    # them <> cho cac dau cau
    for i in dau:
        index = text.find(i)
        if index == -1:
            text = text
        else:
            replace = ' <' + i + '> '
            text = text.replace(i, replace)

    # lay ra list word
    list_raw = re.split(pattern, text)
    list_words = []
    for lt in list_raw:
        if lt != '':
            list_words.append(lt)

    # filter and join word
    words = []
    index = 0
    while index < len(list_words):
        regx1 = re.match(pattern1, list_words[index])
        regx2 = re.match(pattern2, list_words[index])
        regx3 = re.match(pattern3, list_words[index])
        if regx3:
            words.append(list_words[index])
            index = index + 1
        elif regx1 and not regx2:
            words.append(list_words[index] + ' ' + list_words[index + 1])
            index = index + 2
        elif regx2 and not regx1:
            index = index + 1
        elif list_words[index] == '':
            index = index + 1
        else:
            words.append(list_words[index])
            index = index + 1

    list_sen = []
    list_raw = []
    for (index, word) in enumerate(words):
        wrd = {}
        wrd1 = {}
        regx3 = re.match(pattern3, word)
        if regx3:
            wrd = {
                "index": index,
                "type": 1,
                "word": word
            }
            wrd1 = {
                "index": index,
                "type": 1,
                "word": word
            }
        else:
            wrd = {
                "index": index,
                "type": 0,
                "word": bg.process_sequence(word)
            }
            wrd1 = {
                "index": index,
                "type": 0,
                "word": word
            }
        list_sen.append(wrd)
        list_raw.append(wrd1)

    sentence_raw = ''
    for wd in list_sen:
        if wd['type'] == 0:
            sentence_raw = sentence_raw + wd['word'] + ' '

    return list_sen, list_raw, sentence_raw

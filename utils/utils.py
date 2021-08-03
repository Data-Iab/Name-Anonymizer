import re
import unidecode


def remove_accents(txt):
    txt = unidecode.unidecode(txt)
    return txt.lower()


def preprocess_dict(txt):
    return remove_accents(txt)


def preprocess_text(txt):
    custom_replace = {
        '\n': ' ',
        '\t': ' '
    }
    for c, c_r in custom_replace.items():
        txt = txt.replace(c, c_r)

    txt = remove_accents(txt)
    txt = re.sub('[^a-zA-Z]', ' ', txt)
    return ' '.join(txt.split())


def insensitive_replace(txt, sub_text, replace):
    text = re.compile(re.escape(sub_text), re.IGNORECASE)
    return text.sub(replace, txt)

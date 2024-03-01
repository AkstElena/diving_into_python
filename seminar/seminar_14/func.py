import re


def convert_str(text):
    new_str = re.compile('[^a-zA-Z ]')
    res = new_str.sub('', text).lower()
    return res
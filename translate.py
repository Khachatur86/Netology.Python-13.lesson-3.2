import requests
import os

def current_dir():
    return os.path.dirname(os.path.abspath(__file__))

def dir_path(dirname):
    return os.path.join(current_dir(), dirname)

def read_file(file_path):
    with open(file_path, mode="rt") as f:
        return f.read()

def create_dir(path=dir_path("Translate")):
    if not os.path.exists(path):
        return os.mkdir(path)

def write_file(file_path, data):
    with open(file_path,"w", encoding="utf8") as f:
        f.write(data)



def translate(source_file_path, result_file_path, lang_from, lang_to="ru"):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    api_key = "trnsl.1.1.20180324T221656Z.f7f94ef959bead81.a31606e6200131ffaec2fecb027905ff5948663d"
    lang = lang_from + "-" + lang_to
    text = read_file(source_file_path)

    params = {
        'key': api_key,
        'text': text,
        'lang': lang,
    }

    response = requests.get(url, params=params).json()

    write_file(result_file_path, ("".join(response.get("text", []))))
    return



def core():
    file_list = [f for f in os.listdir(current_dir()) if f.endswith(".txt")]
    create_dir("Translate")
    for i in file_list:
        lang_from = i.split(".")[0].lower()
        lang_to = "ru"
        source_file_path = dir_path(i)
        result_file_path = os.path.join(dir_path("Translate"), i)

        translate(source_file_path, result_file_path, lang_from, lang_to)

core()


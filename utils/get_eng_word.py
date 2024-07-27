import requests


def getNEGword(word):
    url = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + word
    r = requests.get(url)
    res = r.json()

    if type(res) == dict:
        return False
    output = {}
    meanings = res[0]['meanings'][0]['definitions']
    definitions = []
    for meaning in range(len(meanings)):
        definitions.append(f"{meaning + 1}: {meanings[meaning]['definition']}")
    output['definition'] = "\n".join(definitions)
    output['audio'] = res[0]['phonetics'][1]['audio']

    return output

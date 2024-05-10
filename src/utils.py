import requests

def fetch_bad_words():

    url = 'https://www.cs.cmu.edu/~biglou/resources/bad-words.txt'

    response = requests.get(url)

    if response.status_code == 200:
        bad_words = response.text.split()
        with open('bad-words.txt', 'w') as f:
            f.write(response.text)

    elif os.path.isfile('bad-words.txt'):
        with open('bad-words.txt', 'r') as f:
            bad_words = f.read().split()

    else:
        bad_words = []

    return bad_words
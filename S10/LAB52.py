import os
import requests


def gen_get_files(dir):
    for file in os.listdir(dir):
        full_path = os.path.join(dir, file)
        yield full_path


def gen_get_file_lines(filename):
    with open(filename) as f:
        for line in f.readlines():
            yield line.replace('\n', '')


def check_webpage(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False


try:
    os.mkdir('LAB52_files')
except:
    pass

with open('LAB52_files/pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-adres.pl/\n')
    f.write('http://www.demotywatory.pl')


with open('LAB52_files/com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')

for file in gen_get_files('LAB52_files'):
    for line in gen_get_file_lines(file):
        print("{} - {} - {}".format(file, line, check_webpage(line)))

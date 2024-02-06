import os


def count_words(file)->int:
    text = file.read()
    splitted_text = text.split()
    count = len(splitted_text)
    return count


path = "LAB4_text.txt"

if not os.path.isfile(path):
    file = open(path, 'x')
    file.write("Hello great great world!")
    file.close()

file = open(path, 'r')
counted_words = count_words(file)
print(f"There are {counted_words} words")

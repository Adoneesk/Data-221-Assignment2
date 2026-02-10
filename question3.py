import string

sample_file = open("sample-file.txt", "r")
sample_file_lines = sample_file.read_lines()

tokens = sample_file_lines.split()

clean_tokens = []

for i in tokens:
    i = i.lower()
    if i.isalpha():
        clean_tokens.append(i)

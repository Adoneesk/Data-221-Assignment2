import string

sample_file = open("sample-file.txt", "r")
sample_file_text = sample_file.read()

tokens = sample_file_text.split()

clean_tokens = []

for i in tokens:
    i = i.lower()
    i = i.strip(string.punctuation)

    if i.isalpha() and len(i) > 2:
            clean_tokens.append(i)

token_counts = {}

for i in clean_tokens:
    if i in token_counts:
        token_counts[i] = 1
    else:
        token_counts[i] = 1

most_frequent_tokens = sorted(token_counts.items(), key=lambda x: x[1], reverse=True)[:10]

for i, j, in most_frequent_tokens:
    print(f"{i} -> {j} ", end="")








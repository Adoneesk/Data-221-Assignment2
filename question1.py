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

bigrams = []

for i in range(len(clean_tokens) - 1):
    bigrams.append((clean_tokens[i], clean_tokens[i + 1]))

bigram_counts = {}
for i in bigrams:
    if i in bigram_counts:
        bigram_counts[i] +=1
    else:
        bigram_counts[i] = 1

top_bigrams = sorted(bigram_counts.items(), key=lambda x: x[1], reverse=True)[:10]

for i, j in top_bigrams:
    print(f"{i[0]} {i[1]} -> {j} ", end="")









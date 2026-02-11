import string

new_file = open("sample-file.txt", "r")
file_lines = new_file.readlines()

my_dict = {}

for i in range(len(file_lines)):
    line = file_lines[i]
    fixed = line.lower()
    cleaned = ""
    for char in fixed:
        if char not in string.whitespace and char not in string.punctuation:
            cleaned += char
    normal = cleaned

    if normal == "":
        continue

    if normal in my_dict:
        my_dict[normal].append((i+1, line.rstrip()))
    else:
        my_dict[normal] = [(i+1, line.rstrip())]

duplicate = [group for group in my_dict.values() if len(group) >1]

for i in range(min(2, len(duplicate))):
    for j, k in duplicate[i]:
        print(f"\t{j} -> {normal}")
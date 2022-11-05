file_names = ['1.txt', '2.txt', '3.txt']

file_lens = {}

for file_name in file_names:
    with open(file_name, encoding='utf8') as file:
        file_lens[file_name] = len(file.readlines())

print(f"File length by name: {file_lens}")
ordered_file_names = sorted(file_lens, key=file_lens.get)
print(f"File names sorted by length: {ordered_file_names}")

with open('result.txt', 'wt', encoding='utf8') as target_file:
    for file_name in ordered_file_names:
        print(file_name, file=target_file)
        print(file_lens[file_name], file=target_file)
        with open(file_name, encoding='utf8') as file:
            for line in file:
                print(line.strip(), file=target_file)

print("Please see result in 'result.txt'")

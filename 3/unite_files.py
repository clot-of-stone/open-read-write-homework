from pathlib import *

file_len = {}
sorted_file_len = {}


def measure_file(new_file):
    length = 0
    with open(new_file, 'r', encoding='utf-8') as entity:
        for _ in entity:
            length += 1
    return length


for file_name in Path('files').iterdir():
    file_len.update({file_name.name: measure_file(file_name)})
sorted_keys = sorted(file_len, key=file_len.get)

for position in sorted_keys:
    sorted_file_len[position] = file_len[position]

with open('result.txt', 'w', encoding='utf-8') as target:
    for name, size in sorted_file_len.items():
        target.write(f'{name}\n{size}\n')
        with open(name, encoding='utf-8') as f:
            target.write(f.read())

with open('result.txt', 'r', encoding='utf-8') as result:
    print(f'{result.read()}')

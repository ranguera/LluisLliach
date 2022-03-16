# Using readlines()
file1 = open('./data/poemes-net.txt', 'r', encoding='utf-8')
Lines = file1.readlines()

file2 = open('./data/poemes-net2.txt', 'a', encoding='utf-8')
set = ""

for line in Lines:
    if line != "\n":
        if "prompt" in line:
            file2.write(set + '\n')
            set = line.replace('\n', '')
        else:
            if "END" in line:
                set = set + line.replace('\n', '')
            else:
                set = set + line.replace('\n', '') + "\\n"

file2.close()
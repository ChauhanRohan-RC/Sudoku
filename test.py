import os

def read_words(f, count: int) -> str:
    wc = 0
    res = ""
    prev_space = True
    while wc <= count:
        c = f.read(1)
        if len(c) == 0:
            break
        ss = c.isspace()
        if not ss and prev_space:
            wc += 1
        prev_space = ss
        res += c
    return res


path = r"D:\RC\Projects\Myokinase\test\main.txt"
out_dir = r"D:\RC\Projects\Myokinase\test\splits"
word_count = 990

os.makedirs(out_dir)
with open(path, 'r', encoding="utf8") as f:
    c = 1
    while True:
        txt = read_words(f, word_count)
        if len(txt) == 0:
            break
        with open(os.path.join(out_dir, f'{c}.txt'), 'w', encoding="utf8") as out_part:
            out_part.write(txt)
        c += 1
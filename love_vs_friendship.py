def words_to_marks(s):
    y = list(map(chr, range(97, 123)))
    data = {v: k for k, v in enumerate(y, 1)}
    return sum(data[x] for x in s)


if __name__ == '__main__':
    print(words_to_marks("love"))


chars = 'abcdefghijklmnopqrstuvxyz.? '
def encoding(number):
    return chars[number % len(chars)]

if __name__ == '__main__':
    st = ''
    with open('pi.txt') as f:
        pi = f.read()
        for a, b in zip(*(iter(pi),) * 2):
            d = int(a + b)
            st += encoding(d)

    words = set()
    with open('/usr/share/dict/words') as d:
        for line in d:
            words.add(line.strip())

    for s in st.split(' '):
        if s in words and len(s) > 3:
            print s



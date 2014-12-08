import csv
import sys

def main():

    num = 7
    if len(sys.argv) == 2:
        num = int(sys.argv[1])

    with open('/usr/share/dict/words') as f:
        words = set([w.strip().lower() for w in f])
    words = sorted(words)

    with open('ptdata.csv') as f:
        reader = csv.reader(f)
        symbols = [row[1].strip().lower() for row in reader]

    with open('clues.txt', 'rU') as f:
        reader = csv.reader(f, delimiter='\t')
        ny_clues = {}
        for row in reader:
            word = row[1].strip().lower()
            clue = row[0].strip()
            if word in ny_clues and len(clue) < len(ny_clues[word]):
                continue
            ny_clues[word] = row[0]

    for word in words:
        word_copy = word
        matched_symbols = []
        num_substitutions = 0
        for sym in symbols:
            count = word.count(sym)
            if count:
                num_substitutions += count
                matched_symbols.append(sym)
                word = word.replace(sym, '')
        if not word and num_substitutions == num and word_copy in ny_clues:
            print word_copy, matched_symbols, ny_clues[word_copy]


if __name__ == '__main__':
    main()

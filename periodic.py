import csv
import sys


def get_all_words():
    words = set()
    with open('clues.txt', 'rU') as f:
        reader = csv.reader(f, delimiter='\t')
        ny_clues = {}
        for row in reader:
            word = row[1].strip().lower()
            words.add(word)
    return sorted(words)


def get_periodic_symbols():
    with open('ptdata.csv') as f:
        reader = csv.reader(f)
        return [row[1].strip().lower() for row in reader]


def get_word_clues_dict():
    with open('clues.txt', 'rU') as f:
        reader = csv.reader(f, delimiter='\t')
        ny_clues = {}
        for row in reader:
            word = row[1].strip().lower()
            clue = row[0].strip()
            if word not in ny_clues:
                ny_clues[word] = []
            ny_clues[word].append(clue)
    return ny_clues


def main():
    if len(sys.argv) == 2:
        num = int(sys.argv[1])
    else:
        print >> sys.stderr, 'Please enter number of subsitutions desired'
        sys.exit(1)
    assert num > 0

    words = get_all_words()
    symbols = get_periodic_symbols()
    ny_clues = get_word_clues_dict()

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

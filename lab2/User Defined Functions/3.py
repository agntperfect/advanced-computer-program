# Q.No.3: Create a program that reads a sentence from the user and stores each word
# as an element of a list. Then count the frequency of each word using only lists and '='.

def get_words():
    sentence = input("Enter a sentence: ")
    return sentence.split()

def count_word_frequencies(words):
    unique_words = []
    counts = []

    for word in words:
        found = False
        for i in range(len(unique_words)):
            if word == unique_words[i]:
                counts[i] = counts[i] + 1
                found = True
                break
        if not found:
            unique_words = unique_words + [word]
            counts = counts + [1]

    return unique_words, counts

def display_frequencies(unique_words, counts):
    for i in range(len(unique_words)):
        print(f"{unique_words[i]}: {counts[i]}")

def main():
    words = get_words()
    unique_words, counts = count_word_frequencies(words)
    display_frequencies(unique_words, counts)

main()
def get_sentence_input():
    """Gets a sentence input from the user."""

    sentence = input("Enter a sentence: ")
    return sentence


def count_words(sentence):
    """Counts the number of words in a sentence."""

    words = sentence.split()
    return len(words)


# Main program flow
print(f"The sentence has {count_words(get_sentence_input())} words.")
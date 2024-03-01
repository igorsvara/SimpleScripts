def word_count():
    text = input("Enter a sentence: ")

    words = text.split()
    w_count = len(words)

    print(f"The sentence contains {w_count} words.")


word_count()

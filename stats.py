def count_words(text):
    # split the text
    words = text.split()
    num_words = 0
    for word in words:
        num_words += 1
    print(f'{num_words} words found in the document')
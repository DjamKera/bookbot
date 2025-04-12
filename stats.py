def count_words(text):
    # split the text
    words = text.split()
    num_words = 0
    for word in words:
        num_words += 1
    print(f'{num_words} words found in the document')

def character_stats(text):
    lower_text = text.lower()
    characters = {}
    for character in lower_text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    print(characters)
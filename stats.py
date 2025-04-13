def count_words(text):
    # split the text
    words = text.split()
    num_words = 0
    for word in words:
        num_words += 1
    # print(f'{num_words} words found in the document')
    return num_words

def character_stats(text):
    lower_text = text.lower()
    characters = {}
    for character in lower_text:
        if character.isalpha():
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
    return characters


def printing_format(characters, words_number, file_path):
    my_list = []
    for value in characters:
        dic =  { 'char': value, 'count': characters[value] } 
        my_list.append(dic)
    my_list.sort(key=lambda character: character['count'], reverse = True )
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    print('----------- Word Count ----------')
    print(f'Found {words_number} total words')
    print('--------- Character Count -------')
    for element in my_list:
        print(f'{element["char"]}: {element["count"]}')
    print('============= END ===============')
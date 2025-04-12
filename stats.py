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
    return characters

def printing_format(characters):
    my_list = []
    for value in characters:
        dic =  { 'char': value, 'count': characters[value] } 
        my_list.append(dic)
    my_list.sort(key=lambda character: character['count'], reverse = True )
    print(my_list)
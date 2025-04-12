from stats import count_words, character_stats, printing_format

file_path = 'books/frankenstein.txt'

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return str(f.read())

def main():
    #get the text form the file
    book_text = get_book_text(file_path)    
    
    #print all characters
    character_stats(book_text)
    #print in the requested format
    printing_format(character_stats(book_text), count_words(book_text), file_path )


main()
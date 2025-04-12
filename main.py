from stats import count_words

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return str(f.read())

def main():
    #get the text form the file
    book_text = get_book_text('./books/frankenstein.txt')    
    # count the numbers of words then print it
    count_words(book_text)


main()
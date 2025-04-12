def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return str(f.read())

def main():
    #get the text form the file
    book_text = get_book_text('./books/frankenstein.txt')    
    # count the numbers of words then print it
    count_words(book_text)

def count_words(text):
    # split the text
    words = text.split()
    num_words = 0
    for word in words:
        num_words += 1
    print(f'{num_words} words found in the document')

main()
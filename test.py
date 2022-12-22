file_book_str = 'Book1.txt'
file_book_list = 'Book2.txt'

def readfile_str(file_book):
    with open(file_book, "r", encoding="utf_8") as s:
        return list(map(lambda x: x.replace('\n', ''), s.readlines()))

def readfile_list(file_book):
    with open(file_book, "r", encoding="utf_8") as s:
        return list(map(lambda x: x.replace('\n', ', '), s.read().split('\n\n')))

print(readfile_str(file_book_str))  
print(readfile_list(file_book_list))       
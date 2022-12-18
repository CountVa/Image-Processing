import csv


def get_books(name):
    with open('books.csv', 'r', newline='') as csvfile:
        row_count = 1
        name_capitalize = name.capitalize()
        books_list = list()
        booksreader = csv.reader(csvfile, delimiter='|')
        for row in booksreader:
            if row_count == 1:
                row_count += 1
                continue
            for i in range(5):
                if i == 3:
                    row[i] = int(row[i])
                if i == 4:
                    row[i] = float(row[i])
            if row[1].find(name_capitalize) != -1 or row[1].find(name) != -1:
                books_list.append(row)
        row_count += 1
        return books_list


def get_totals(books_list, sum=float(), add=float()):
    totals_list = list()
    for row in range(len(books_list)):
        isdb = str()
        full_price = 1
        for i in range(5):
            if i == 0:
                isdb = books_list[row][i]
            if i == 3:
                full_price *= books_list[row][i]
            if i == 4:
                full_price *= books_list[row][i]
        if full_price < sum:
            full_price += add
        mid_list = (f'{isdb}', float(f'{full_price}'))
        totals_list.append(mid_list)
    return totals_list


book_name = input('Введите название поиска по имени книги: ')
books = get_books(book_name)
print(books)
totals = get_totals(books, 500, 100)
print(totals)
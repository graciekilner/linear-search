



lista = [2, 34, 5, 23, 18, 13, 7, 11]


def search_item(search_term, data_list):
    for item in data_list:
        if search_term == item:
            return f'Found data item: {item}'
    return 'Data item not found.'


search_term = int(input('Enter a search term: '))


result = search_item(search_term, lista)
print(result)

def main():
    pass

if (__name__ == "__main__"):

          main()

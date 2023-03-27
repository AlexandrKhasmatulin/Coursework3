import json
from utils import sort_data
from utils import format
FILE = 'operations.json'
def main():
    with open(FILE, 'r', encoding = 'utf8') as file:
        data = json.load(file)
    data = sort_data(data)
    for i in range (5):
        print(format(data[i]))
        print()
if __name__== '__main__':
    main()
book={}
book['tom']={
    'name': 'tom',
    'address': '1, hemsen lane',
    'phone': 90909090
}
book['bob']={
    'name':'bob',
    'address':'110, CDA avenue',
    'phone': 8765432
}

import json
s=json.dumps(book)
with open("c://data//book.txt", "w") as f:
    f.write(s)
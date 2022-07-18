# Bubble Sort Exercise
# Modify bubble_sort function such that it can sort following list of transactions happening in an electronic store,
#
# elements = [
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#     ]
# bubble_sort function should take key from a transaction record and sort the list as per that key. For example,
#
# bubble_sort(elements, key='transaction_amount')
# This will sort elements by transaction_amount and your sorted list will look like,
#
# elements = [
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#     ]
# But if you call it like this,
#
# bubble_sort(elements, key='name')
# output will be,
#
# elements = [
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#     ]


def bubblesort(elements):
    size=len(elements)
    for i in range(size-1):
        swaped= False
        for j in range(size-1-i):
            if elements[j]["transaction_amount"]> elements[j+1]["transaction_amount"]:
                elements[j]["transaction_amount"], elements[j+1]["transaction_amount"] = elements[j+1]["transaction_amount"], elements[j]["transaction_amount"]
                swaped = True
        if not swaped:
            break


if __name__== "__main__":
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]

    bubblesort(elements)
    print(elements)


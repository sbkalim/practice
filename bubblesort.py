# def swap(a, b):
#     temp = a
#     a = b
#     b = temp

def bubbleSort(elements):
    size = len(elements)
    for j in range(size - 1):
        swaped = False
        for i in range(size-1-j):
                if elements[i]>elements[i+1]:
                    temp = elements[i]
                    elements[i]= elements[i+1]
                    elements[i+1]=temp

                    swaped = True
        if not swaped:
            break


if __name__== "__main__":
    elements= [1, 93, 81, 3, 51, 7, 6, 48]
    print(elements)
    bubbleSort(elements)
    print(elements)


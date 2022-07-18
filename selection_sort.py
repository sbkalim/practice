def selection_sort(elements):
    size=len(elements)
    for i in range(size-1):
        min_index= i
        for j in range(min_index+1, size):
            if elements[min_index]> elements[j]:
                elements[min_index], elements[j]= elements[j], elements[min_index]



if __name__== "__main__":
    elements = [45, 1, 56, 2, 89, 7, 23, 9]

    selection_sort(elements)
    print(elements)


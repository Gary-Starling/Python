#Двоичный поиск
#Входные данные отсортированы в порядке возрастания

A = [5, 1, 5, 8, 12, 13, 14, 15, 16, 20, 50, 60 , 90 , 200 , 300 , 4000, 50000, 200000, 1000000]
B = [5, 8, 1, 23, 1, 11, 1000000]



def b_search(array, element):

    lo, hi = 0, len(array) - 1
    while lo <= hi:
        mid = (lo+hi) // 2
        if element < array[mid]:
            hi = mid - 1    #[lo, mid - 1]
        elif element >array[mid]:
            lo = mid + 1    #[mid + 1, hi]
        else:
            return mid + 1  #1-based
    return -1


C = []
for i in B[1::1]:
    C.append(b_search(A[1::1],i))

print(*C)
     
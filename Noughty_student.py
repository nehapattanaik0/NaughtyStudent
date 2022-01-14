def mostNoughty(arr, n):
    arr.sort()
    max_count = 1; res = arr[0]; curr_count = 1

    for i in range(1, n):
        if (arr[i] == arr[i - 1]):
            curr_count += 1
        else :
            if (curr_count > max_count):
                max_count = curr_count
                res = arr[i - 1]
                curr_count = 1
    if (curr_count > max_count):
        max_count = curr_count
        res = arr[n - 1] 
    return res

def leastNoughty(arr, n) :
    arr.sort()
    least_count = n + 1
    res = -1
    curr_count = 1
    for i in range(1, n) :
        if (arr[i] == arr[i - 1]) :
            curr_count = curr_count + 1
        else :
            if (curr_count < least_count) :
                least_count = curr_count
                res = arr[i - 1]
                curr_count = 1
    if (curr_count < least_count) :
        least_count = curr_count
        res = arr[n - 1]
    return res
data = []
n = eval(input('Enter how many elements you want: '))
for i in range(0, n):
    x = input('Enter the numbers into the array: ')
    data.append(x)
print("Most Naughty: ",mostNoughty(data, n))
print("Least Naughty: ",leastNoughty(data, n))
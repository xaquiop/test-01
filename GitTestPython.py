def most_frequent(list):
    return max(set(list), key = list.count)  

numbers = [1488,666]
most_frequent(numbers)

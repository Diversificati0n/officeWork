def filter_strings(strings):
    result = []
    for string in strings:
        if len(string) <= 3:
            result.append(string)
    return result

array1 = ["hello", "2", "world", ":-)"]
filtered_array1 = filter_strings(array1)
print(filtered_array1)

array2 = ["1234", "1567", "-2", "computer science"]
filtered_array2 = filter_strings(array2)
print(filtered_array2)
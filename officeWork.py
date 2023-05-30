def filter_strings(strings):
    result = []
    for string in strings:
        if len(string) <= 3:
            result.append(string)
    return result

array1 = ["hello", "2", "world", ":-)"]
filtered_array1 = filter_strings(array1)
print(filtered_array1)
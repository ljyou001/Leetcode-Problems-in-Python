def transform_strings(arr):
    result = []
    
    for word in arr:
        if len(word) % 2 == 0:
            result.append(word[::-1])
        else:
            result.append(word.upper())
    
    return result
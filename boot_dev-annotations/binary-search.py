
def binary_search(data, followers):
    left = 0
    right = len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        if data[middle]["followers"] == followers:
            return data[middle]["name"]
        elif data[middle]["followers"] < followers:
            left = middle + 1
        else:
            right = middle - 1
    return None


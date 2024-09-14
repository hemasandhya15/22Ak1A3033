def find_nearest_zero_sum(arr):
    arr.sort()
    left, right = 0, len(arr) - 1
    nearest_sum = float('inf')
    nearest_pair = ()

    while left < right:
        current_sum = arr[left] + arr[right]
        if abs(current_sum) < abs(nearest_sum):
            nearest_sum = current_sum
            nearest_pair = (arr[left], arr[right])
        if current_sum < 0:
            left += 1
        else:
            right -= 1

    return nearest_pair

arr = [1, 5, 3, 2, 4]
print(find_nearest_zero_sum(arr))

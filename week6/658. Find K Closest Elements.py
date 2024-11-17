def findClosestElements(arr, k, x):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid

    left, right = left - 1, left

    result = []
    while k > 0:
        if left >= 0 and (
            right >= len(arr) or abs(arr[left] - x) <= abs(arr[right] - x)
        ):
            result.append(arr[left])
            left -= 1
        else:
            result.append(arr[right])
            right += 1
        k -= 1

    return sorted(result)

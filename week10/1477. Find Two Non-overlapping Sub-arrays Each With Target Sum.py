def min_sum_of_lengths(arr, target):
    n = len(arr)
    left = [float("inf")] * n
    right = [float("inf")] * n

    curr_sum = 0
    l = 0
    for r in range(n):
        curr_sum += arr[r]
        while curr_sum > target:
            curr_sum -= arr[l]
            l += 1
        if curr_sum == target:
            left[r] = r - l + 1
        if r > 0:
            left[r] = min(left[r], left[r - 1])

    curr_sum = 0
    r = n - 1
    for l in range(n - 1, -1, -1):
        curr_sum += arr[l]
        while curr_sum > target:
            curr_sum -= arr[r]
            r -= 1
        if curr_sum == target:
            right[l] = r - l + 1
        if l < n - 1:
            right[l] = min(right[l], right[l + 1])

    result = float("inf")
    for i in range(n - 1):
        result = min(result, left[i] + right[i + 1])

    return result if result < float("inf") else -1

def min_operations(nums, x):
    total = sum(nums)
    target = total - x
    if target < 0:
        return -1

    n = len(nums)
    curr_sum = 0
    max_len = -1
    left = 0

    for right in range(n):
        curr_sum += nums[right]
        while curr_sum > target and left <= right:
            curr_sum -= nums[left]
            left += 1
        if curr_sum == target:
            max_len = max(max_len, right - left + 1)

    return n - max_len if max_len != -1 else -1

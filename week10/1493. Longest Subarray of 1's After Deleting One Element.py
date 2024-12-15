def longest_subarray(nums):
    max_len = 0
    zero_count = 0
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_len = max(max_len, right - left)
    return max_len

def maximum_unique_subarray(nums):
    seen = set()
    curr_sum = 0
    max_sum = 0
    left = 0

    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            curr_sum -= nums[left]
            left += 1
        seen.add(nums[right])
        curr_sum += nums[right]
        max_sum = max(max_sum, curr_sum)

    return max_sum
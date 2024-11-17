def numberOfArithmeticSlices(nums):
    if len(nums) < 3:
        return 0

    count = 0
    current_length = 0  # Tracks the number of new slices ending at the current position

    for i in range(2, len(nums)):
        # Check if the current three elements form an arithmetic slice
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            current_length += 1
            count += current_length
        else:
            current_length = 0  # Reset if the sequence breaks

    return count

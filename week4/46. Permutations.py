def permute(nums):
    result = []

    def backtrack(current_permutation, used):
        if len(current_permutation) == len(nums):
            result.append(list(current_permutation))
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            current_permutation.append(nums[i])
            used[i] = True
            backtrack(current_permutation, used)

            current_permutation.pop()
            used[i] = False

    backtrack([], [False] * len(nums))

    return result

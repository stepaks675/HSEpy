class Solution(object):
    def maxArea(self, height):
        left = 0  # указатель на начало
        right = len(height) - 1  # указатель на конец
        max_area = 0

        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width

            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

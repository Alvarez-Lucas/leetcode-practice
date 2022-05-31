# def longestConsecutive(nums):
#     to_visit = set()
#     longest_length = 1 if len(nums) > 0 else 0
#     for num in nums:
#         to_visit.add(num)
#         right_pointer = num
#         left_pointer = num
#         instance_length = 1
#         while right_pointer + 1 in to_visit:
#             right_pointer += 1
#             instance_length += 1
#             longest_length = max(longest_length, instance_length)
#         while left_pointer - 1 in to_visit:
#             left_pointer -= 1
#             instance_length += 1
#             longest_length = max(longest_length, instance_length)
#     return longest_length


def longestConsecutive(nums):
    to_visit = set(nums)
    longest_length = 1 if len(nums) > 0 else 0
    for num in nums:
        if num in to_visit:
            to_visit.remove(num)
            right_pointer = num
            left_pointer = num
            instance_length = 1
            while right_pointer + 1 in to_visit:
                right_pointer += 1
                to_visit.remove(right_pointer)
                instance_length += 1
            while left_pointer - 1 in to_visit:
                left_pointer -= 1
                to_visit.remove(left_pointer)
                instance_length += 1
            longest_length = max(longest_length, instance_length)
    return longest_length


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

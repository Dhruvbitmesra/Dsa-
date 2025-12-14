##check if the array is sorted or not in True or False

def checker(nums):
    n = len(nums)
    i = 0
    while i < n - 1:
        if nums[i] > nums[i + 1]:
            return False
        i += 1
    return True


nums = [3, 8, 6, 8, 9, 10, 20]
print(checker(nums))   # True or Flase

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print('----------------------')
        l, r = 0, len(numbers) - 1
        print('L: ', l, ' R: ', r)
        while l < r:
            if numbers[l] + numbers[r] == target: 
                print('entered 1')
                return [l+1, r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
                print('entered 2 ', l)

            elif numbers[r] == numbers[r - 1] or numbers[l] + numbers[r] > target:
                r -= 1
                print('entered 3 ', r)

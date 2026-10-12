class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        board = {}
        for i, n in enumerate(nums):
            need = target - n
            if need in board:
                return [board[need], i]
            board[n] = i
        return [board[n],[need]]

        
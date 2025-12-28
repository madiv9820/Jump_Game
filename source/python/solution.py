from typing import List

class pySolution:
    def canJump(self, nums: List[int]) -> bool:
        # 📏 Length of the array
        n: int = len(nums)

        # 🧠 DP table
        # isPossible[i] = True if we can reach the last index starting from i
        isPossible: List[bool] = [False] * n

        # 🎯 Base case
        # From the last index, we are already at the destination
        isPossible[n - 1] = True

        # 🔁 Traverse the array from right to left
        # We solve smaller subproblems first (bottom-up DP)
        for currentPosition in range(n - 1, -1, -1):

            # 👣 Try all possible jump lengths from current position
            for step in range(1, nums[currentPosition] + 1):

                # 📦 Check the result of the next reachable position
                # If the jump goes out of bounds, treat it as invalid (False)
                nextResult: bool = (
                    isPossible[currentPosition + step]
                    if currentPosition + step < n
                    else False
                )

                # 🔗 Update current state
                # If ANY jump can reach the end, current position is valid
                isPossible[currentPosition] |= nextResult
                
                # ✂️ Early pruning: stop checking further jumps
                # if we already can reach the end
                if isPossible[currentPosition]:
                    break

        # 🚀 Final answer
        # Can we reach the last index starting from index 0?
        result: bool = isPossible[0]

        # 🧹 Cleanup (optional, improves readability)
        del isPossible

        # 🎉 Return result
        return result
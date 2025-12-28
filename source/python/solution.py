from typing import List

class pySolution:
    def canJump(self, nums: List[int]) -> bool:
        """
        🚀 Determines if you can reach the last index of the array.
        nums: List[int] - Each element represents max steps you can jump forward from that position.
        Returns True if you can reach the end, else False.
        """
        
        def isPossible(currentPosition: int = 0) -> bool:
            """
            🔍 Recursive helper function to check if the last index is reachable from currentPosition.
            
            currentPosition: int - The index we're currently at
            Returns True if end is reachable from here, else False
            """
            
            # ✅ Base case: If we've reached the last index, we succeeded!
            if currentPosition == len(nums) - 1: return True
            
            # 🔄 Try all possible jumps from current position
            for step in range(1, nums[currentPosition] + 1):
                # ⏩ Move forward by 'step' and check recursively
                if isPossible(currentPosition + step):
                    return True  # 🎯 Found a valid path to the end
            
            # ❌ If no jumps worked, we're stuck
            return False

        # 🚦 Start the recursion from the first index
        return isPossible()
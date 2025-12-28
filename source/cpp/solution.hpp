#include <vector>
using namespace std;

class Solution {
private:
    vector<int> nums; // 📦 Store the input array inside the class

    // 🔍 Recursive helper to check if we can reach the end from currentPosition
    bool isPossible(int currentPosition = 0) {
        // ✅ Base case: reached the last index
        if(currentPosition == nums.size() - 1) return true;

        // 🔄 Try all possible jumps from current position
        for(int step = 1; step <= nums[currentPosition]; ++step) {
            // ⏩ Move forward by 'step' and check recursively
            if(isPossible(currentPosition + step))
                return true; // 🎯 Found a valid path to the end
        }

        // ❌ No valid jumps from this position
        return false;
    }

public:
    // 🚦 Main function to determine if last index is reachable
    bool canJump(vector<int>& nums) {
        this->nums = nums;         // 📥 Store input array
        bool result = isPossible(); // 🔑 Start recursion from index 0
        vector<int>().swap(nums);   // 🧹 Clean up memory
        return result;             // ✅ Return final result
    }
};
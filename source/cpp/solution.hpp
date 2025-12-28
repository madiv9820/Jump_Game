#include <vector>
using namespace std;

#include <vector>
using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
        // 🏁 Initialize the farthest position we can reach
        int farthest = 0;
        // 🎯 Last index we need to reach
        int lastIndex = nums.size() - 1;

        // 🔄 Iterate through each index in the array
        for(int index = 0; index < nums.size(); ++index) {
            // 🚀 Update the farthest reachable position from current index
            farthest = max(farthest, index + nums[index]);

            // ✅ If we can reach or pass the last index, return true
            if(farthest >= lastIndex) return true;

            // 🛑 If we can't move forward from current position, break early
            if(farthest <= index) break;
        }

        // ❌ If loop ends without reaching last index, return false
        return false;
    }
};
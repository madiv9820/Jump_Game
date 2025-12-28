## 🚀 Greedy Approach

The idea of the **Greedy Approach** is simple but powerful: **always try to jump as far as possible at each step**! 🏃‍♂️💨  

### Here's how it works:

1. **Initialize the farthest reachable index**  
   - Start with `farthest = 0` and `lastIndex = nums.size() - 1` 🎯.  
   - This keeps track of how far we can go as we move through the array.

2. **Iterate through the array** 🔄  
   - At each position `index`, calculate the farthest we can reach from there:  
     ```cpp
     farthest = max(farthest, index + nums[index]);
     ```  
   - This ensures we always know the **maximum possible distance** we can jump from any point.

3. **Check if we can reach the end** ✅  
   - If `farthest >= lastIndex`, we can reach the last index, so **return true** 🎉.

4. **Detect if we are stuck** 🛑  
   - If `farthest <= index`, it means we **cannot move forward**, so break the loop and return false ❌.

5. **Return result**  
   - After the loop, if we haven't reached the last index, return false.


### **Complexity Analysis** 📊:  
- **Time Complexity:** `O(n)` – We traverse the array only once.  
- **Space Complexity:** `O(1)` – Only a few variables are needed, no extra storage.
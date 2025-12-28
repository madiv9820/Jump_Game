## 🧩 Brute Force Approach
### 🔹 Approach
- Use **recursive backtracking** to explore all possible jump paths from the first index.
- At each position, try every jump length from `1` to `nums[currentIndex]`.
- **Base case:** if the current index reaches the last element, return `True`.
- If no valid jumps reach the end, return `False`.

### Steps:
1. Start recursion at index `0`.
2. For current index `i`, iterate over all possible steps `1…nums[i]`.
3. Recursively check if jumping `step` positions reaches the end.
4. Return `True` if any recursive call succeeds; otherwise, return `False`.

### ⚡ Complexity Analysis
- **Time Complexity:** `O(2^n)`
    - In the worst case, each position can branch to multiple jumps → exponential number of paths.

- **Space Complexity:** `O(n)`
    - Recursion stack depth can go up to n (length of the array).

### 📝 Notes
- This is the **simplest brute-force solution**.
- ✅ Easy to understand and implement.
- ⚠️ Not efficient for large inputs; better approaches (greedy or DP) exist for optimized solutions.
---
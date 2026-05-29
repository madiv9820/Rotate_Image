## 🧅 Approach 1: Layer-by-Layer Simulation

### 🧠 Intuition
The mental model for this algorithm is **peeling an onion**. Instead of trying to shift all numbers at once, we treat the matrix as a series of concentric rings (or layers). 

We start with the outermost ring. By defining four boundaries (`Top`, `Bottom`, `Left`, `Right`), we can grab four corners of the ring and rotate them in a 4-way swap. Once the entire outer ring is rotated, we step inward by shrinking our boundaries by one and repeat the process on the next inner ring. We keep doing this until we reach the center of the matrix.

### 🚶‍♂️ Step-by-Step Logic
> 1. **Set Up Boundaries:** Initialize four pointers to represent the absolute edges of the current ring: `Left = 0`, `Right = n - 1`, `Top = 0`, `Bottom = n - 1`.
> 2. **Loop Through Layers:** Create an outer `while` loop that runs as long as `Left < Right`. (Once the pointers meet or cross, we've hit the center of the matrix).
> 3. **Iterate Through the Current Layer:** Create an inner `for` loop that uses an offset variable `i` to walk through the elements of the current top row (from `Left` to `Right - 1`).
> 4. **The 4-Way Swap:** For each element at offset `i`:
>       * **Store:** Save the top-left element in a temporary variable so it isn't overwritten.
>       * **Move ⬆️:** Overwrite the top-left with the bottom-left.
>       * **Move ⬅️:** Overwrite the bottom-left with the bottom-right.
>       * **Move ⬇️:** Overwrite the bottom-right with the top-right.
>       * **Move ➡️:** Overwrite the top-right with the saved temporary variable.
> 5. **Shrink the Onion:** Once the `for` loop finishes, the entire outer ring is successfully rotated. Increment `Left` and `Top`, and decrement `Right` and `Bottom` to move to the next inner ring.

### 💻 Pseudocode

```text
function rotate(matrix):
    left = 0
    right = length(matrix) - 1
    top = 0
    bottom = length(matrix) - 1

    while left < right:
        for i from 0 to (right - left - 1):
            
            // 1. Save the top-left element
            temp = matrix[top][left + i]
            
            // 2. Move bottom-left into top-left
            matrix[top][left + i] = matrix[bottom - i][left]
            
            // 3. Move bottom-right into bottom-left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            
            // 4. Move top-right into bottom-right
            matrix[bottom][right - i] = matrix[top + i][right]
            
            // 5. Move saved temp into top-right
            matrix[top + i][right] = temp
        
        // Shrink the boundaries inward for the next layer
        left = left + 1
        right = right - 1
        top = top + 1
        bottom = bottom - 1
```

### 📊 Complexity Analysis
* **Time Complexity:** `O(n^2)`
    * We touch every single element in the `n x n` matrix exactly once during our 4-way swaps. There is no redundant processing, making this the optimal mechanical time complexity.

* **Space Complexity:** `O(1)`
    * The rotation is done strictly in-place. Aside from a few integer pointers (`left`, `right`, `top`, `bottom`, `i`) and a single `temp` variable for swapping, no extra memory is allocated, regardless of how large the matrix grows.
---
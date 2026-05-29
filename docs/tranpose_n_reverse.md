## ✨ Approach 2: Transpose and Reverse

### 🧠 Intuition
This approach leverages a beautiful property of linear algebra. Instead of trying to calculate complex 2D spatial rotations, we can break a 90-degree clockwise rotation into two extremely simple, independent geometric transformations:

1. **Transpose the Matrix:** Swap the rows and columns. (Imagine folding the matrix in half diagonally from the top-left to the bottom-right).
2. **Reflect Horizontally:** Reverse the elements of each row. (Imagine folding the matrix in half vertically, right down the middle).

Applying these two transformations sequentially results in a perfect 90-degree clockwise rotation!

### 🚶‍♂️ Step-by-Step Logic
> **Step 1: The Transpose**
> 1. Loop through the matrix rows using an index `i`.
> 2. Loop through the columns using an index `j`, but **start `j` at `i`**. (This ensures we only visit the "upper right" triangle of the matrix. If we started `j` at `0`, we would swap elements twice, completely undoing our work!)
> 3. Swap the element at `matrix[i][j]` with the element at `matrix[j][i]`.

> **Step 2: The Horizontal Reflection**
> 1. Loop through each row in the matrix.
> 2. For each row, set up two pointers: a `Left` pointer at the start `0`, and a `Right` pointer at the end `n - 1`.
> 3. Swap the elements at the `Left` and `Right` pointers, then move them inward (`Left + 1`, `Right - 1`).
> 4. Stop swapping when the pointers meet in the middle. 

### 💻 Pseudocode

```text
function rotate(matrix):
    n = length(matrix)
    
    // Step 1: Transpose across the main diagonal
    for i from 0 to n - 1:
        // Start j at i to only process the upper triangle
        for j from i to n - 1:
            swap(matrix[i][j], matrix[j][i])
            
    // Step 2: Reverse every row (Horizontal Reflection)
    for i from 0 to n - 1:
        left = 0
        right = n - 1
        
        while left < right:
            swap(matrix[i][left], matrix[i][right])
            left = left + 1
            right = right - 1
```

### 📊 Complexity Analysis
* **Time Complexity:** `O(n^2)`
    * We visit the elements twice: once during the transpose phase (touching about half the elements to swap them), and once during the row-reversal phase. While it requires technically more memory reads/writes than the simulation approach, it simplifies to the exact same Big-O time complexity.

* **Space Complexity:** `O(1)`
    * The rotation is done strictly in-place. We only allocate a few integer variables for our `i`, `j`, `left`, and `right` iterators, meaning memory usage remains constant regardless of the matrix size.
---
# [Rotate Image ♻️](https://leetcode.com/problems/rotate-image/description/?envType=study-plan-v2&envId=top-interview-150)

### 📘 Problem

You are given an **`n x n`** 2D matrix representing an image. Your task is to rotate that image by **90 degrees clockwise** 🔄

The catch:

- 🛠️ You must do it **in-place**
- 🚫 You are **not allowed** to create another 2D matrix
- 🎯 The original matrix itself must be updated

### ❓ What Is The Question Asking?

Think of the matrix like a square picture made of numbers.

You need to rotate that picture clockwise so that:

- ⬅️ the left side moves to the top
- ⬇️ the top moves to the right
- ➡️ the right side moves to the bottom
- ⬆️ the bottom moves to the left

And you must make that change directly inside the same matrix.

### 🧪 Example 1

![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

**Input**
```text
matrix = [[1,2,3],[4,5,6],[7,8,9]]
```

**Output**
```text
[[7,4,1],[8,5,2],[9,6,3]]
```

### 🧪 Example 2

![](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)

**Input**
```text
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
```

**Output**
```text
[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

### 📏 Constraints

- **`n == matrix.length == matrix[i].length`**
- **`1 <= n <= 20`**
- **`-1000 <= matrix[i][j] <= 1000`**

---

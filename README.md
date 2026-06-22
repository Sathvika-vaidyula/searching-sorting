# 🔍 Searching and Sorting Algorithms in Python

# 1️⃣ Linear Search

## 📌 Explanation

Linear Search checks each element one by one until the target element is found.

## 📝 Example

**Array**

```text
[10, 20, 30, 40]
```

**Target**

```text
30
```

**Process**

```text
10 ❌
20 ❌
30 ✅
```

**Output**

```text
Index = 2
```

## 📋 Pseudocode

```text
LinearSearch(arr, target)

FOR each element in arr
    IF element == target
        RETURN index

RETURN -1
```

## ⏱ Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(1) |
| Average | O(n) |
| Worst | O(n) |

### Why?

- Best Case: Element found at first position
- Worst Case: Element found at last position or not found

## 💾 Space Complexity

```text
O(1)
```

## 🎯 Interview Questions

1. What is Linear Search?
2. Can Linear Search work on unsorted arrays?
3. Difference between Linear Search and Binary Search?

---

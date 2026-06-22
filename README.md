# 🔍 Searching and Sorting Algorithms
# 1. Linear Search

## Definition
Checks elements one by one until the target is found.

## Real World Example
📌 Finding a student's name in an attendance register.

## Algorithm

```text
Start from first element
Compare with target

If found
    Return index

Else
    Move to next element

If end reached
    Return -1
```

## Example

```text
Array = [10,20,30,40]
Target = 30

10 ❌
20 ❌
30 ✅

Output = 2
```

## Time Complexity

| Case | Complexity |
|--------|------------|
| Best | O(1) |
| Average | O(n) |
| Worst | O(n) |

## Space Complexity

```text
O(1)
```

## Interview Questions

✅ Can Linear Search work on unsorted arrays?

✅ Difference between Linear Search and Binary Search?

---

# 2. Binary Search

## Definition

Searches a sorted array by repeatedly dividing it into halves.

## Real World Example

📌 Searching a word in a dictionary.

## Algorithm

```text
Find middle element

If target == middle
    Return index

If target > middle
    Search right half

Else
    Search left half

Repeat
```

## Example

```text
Array = [1,2,3,4,5]

Target = 4

mid = 3

Target > 3

Search right half

Found 4
```

## Time Complexity

| Case | Complexity |
|--------|------------|
| Best | O(1) |
| Average | O(log n) |
| Worst | O(log n) |

## Space Complexity

```text
O(1)
```

## Interview Questions

✅ Why must Binary Search use a sorted array?

✅ Can Binary Search work on linked lists?

---

# 3. Bubble Sort

## Definition

Repeatedly swaps adjacent elements.

Largest element moves to the end after each pass.

## Real World Example

📌 Air bubbles rising in water.

## Algorithm

```text
Compare adjacent elements

If left > right

Swap

Repeat for all passes
```

## Example

```text
[5,4,3]

5 ↔ 4

[4,5,3]

5 ↔ 3

[4,3,5]

4 ↔ 3

[3,4,5]
```

## Time Complexity

| Case | Complexity |
|--------|------------|
| Best | O(n) |
| Average | O(n²) |
| Worst | O(n²) |

## Space Complexity

```text
O(1)
```

## Interview Questions

✅ Why is it called Bubble Sort?

✅ Is Bubble Sort stable?

---

# 4. Selection Sort

## Definition

Select the minimum element and place it at the correct position.

## Real World Example

📌 Arranging books from shortest to tallest.

## Algorithm

```text
Find minimum element

Swap with first unsorted position

Repeat
```

## Example

```text
[4,3,2]

Minimum = 2

Swap

[2,3,4]
```

## Time Complexity

```text
Best    O(n²)
Average O(n²)
Worst   O(n²)
```

## Space Complexity

```text
O(1)
```

## Interview Questions

✅ Difference between Bubble and Selection Sort?

---

# 5. Insertion Sort

## Definition

Inserts each element into its correct position.

## Real World Example

📌 Arranging playing cards in hand.

## Algorithm

```text
Pick current element

Shift larger elements right

Insert current element
```

## Example

```text
[5,2,4]

Insert 2

[2,5,4]

Insert 4

[2,4,5]
```

## Time Complexity

```text
Best    O(n)
Average O(n²)
Worst   O(n²)
```

## Space Complexity

```text
O(1)
```

## Interview Questions

✅ Why is Insertion Sort good for nearly sorted arrays?

---

# 6. Quick Sort

## Definition

Uses a Pivot and Divide & Conquer.

## Real World Example

📌 Organizing people by height around a chosen person.

## Algorithm

```text
Choose Pivot

Smaller → Left

Larger → Right

Recursively sort both sides
```

## Example

```text
[5,2,8,1,4]

Pivot = 5

[2,1,4] 5 [8]

↓

[1,2,4,5,8]
```

## Time Complexity

```text
Best    O(n log n)
Average O(n log n)
Worst   O(n²)
```

## Space Complexity

```text
O(log n)
```

## Interview Questions

✅ What is Pivot?

✅ Why O(n²) in worst case?

---

# 7. Merge Sort

## Definition

Divides the array into halves and merges sorted halves.

## Real World Example

📌 Merging sorted exam papers from different classrooms.

## Algorithm

```text
Divide

Sort Left

Sort Right

Merge
```

## Example

```text
[5,2,8,1]

↓

[5,2] [8,1]

↓

[5] [2] [8] [1]

↓

[2,5] [1,8]

↓

[1,2,5,8]
```

## Time Complexity

```text
Best    O(n log n)
Average O(n log n)
Worst   O(n log n)
```

## Space Complexity

```text
O(n)
```

## Interview Questions

✅ Why is Merge Sort stable?

✅ Difference between Merge Sort and Quick Sort?

---

# 📊 Quick Revision Table

| Algorithm | Best | Average | Worst |
|------------|---------|---------|---------|
| Linear Search | O(1) | O(n) | O(n) |
| Binary Search | O(1) | O(log n) | O(log n) |
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Selection Sort | O(n²) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |

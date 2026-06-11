# SDESheet

My solutions to the **SDE Sheet** — a curated list of Data Structures & Algorithms
problems for interview preparation. Each problem is solved in Python, often with
multiple approaches (brute force → better → optimal) and annotated with time and
space complexity.

## Structure

Problems are grouped by day. Each file is a single problem and contains a
`Solution` class exposing one method per approach, followed by a small driver
that runs the approaches on a sample input.

```
SDESheet/
├── Day1/
│   ├── 1_set_matrix_zero        # Set Matrix Zeroes
│   ├── 2_pascal_triangle.py     # Pascal's Triangle
│   └── 3_next_permutation.py    # Next Permutation
├── Day2/
│   ├── 1_kadane_s_algorithm_maximum_subarray_sum_in_an_array.py   # Maximum Subarray Sum
│   ├── 2_sort_an_array_of_0s_1s_and_2s.py                         # Sort 0s, 1s and 2s
│   └── 3_stock_buy_and_sell.py                                    # Best Time to Buy and Sell Stock
├── Day3/
│   ├── 1_Rotate_omage_by_90_degree.py                            # Rotate Image by 90°
│   ├── 2_merge_overlapping_sub_intervals.py                      # Merge Overlapping Intervals
│   └── 3_merge_two_sorted_arrays_without_extra_space.py          # Merge Two Sorted Arrays
├── Day4/
│   ├── 1_find_the_duplicate_in_an_array.py                       # Find the Duplicate Number
│   ├── 2_find_the_repeating_and_missing_numbers.py               # Repeating and Missing Numbers
│   └── 3_count_inversions_in_an_array.py                         # Count Inversions
├── Day5/
│   ├── 1_search_in_a_sorted_2d_matrix.py                         # Search in a Sorted 2D Matrix
│   ├── 2_x_raised_to_the_power_n.py                              # Pow(x, n)
│   └── 3_majority_element_that_occurs_more_than_half_of_n_times.py  # Majority Element (> N/2)
├── Day6/
│   ├── 1_find_elements_that_appears_more_than_N_of_3_times.py    # Majority Element (> N/3)
│   ├── 2_grid_unique_paths.py                                    # Grid Unique Paths
│   └── 3_count_reverse_pairs.py                                  # Count Reverse Pairs
├── Day7/
│   ├── 1_two_sum.py                                              # Two Sum
│   ├── 2_four_sum.py                                             # 4Sum
│   └── 3_longest_consecutive_sequence_in_array.py               # Longest Consecutive Sequence
├── Day8/
│   ├── 1_length_of_longest_subarray_with_zero_sum.py            # Longest Subarray with Sum Zero
│   ├── 2_count_the_number_of_subarrays_with_given_xor_K.py      # Subarrays with XOR K
│   └── 3_length_of_longest_substring_without_any_repeating_character.py  # Longest Substring Without Repeats
├── Day9/
│   ├── 1_reverse_ll.py                                           # Reverse a Linked List
│   ├── 2_find_middle_of_ll.py                                    # Middle of a Linked List
│   └── 3_merge_two_sorted_lists.py                              # Merge Two Sorted Lists
├── Day10/
│   ├── 1_remove_N_th_node_from_the_end_of_a_Linked_List.py      # Remove Nth Node From End
│   ├── 2_add_2_numbsers_represented_as_ll.py                    # Add Two Numbers
│   └── 3_delete_given_node_in_a_ll.py                           # Delete a Given Node
└── Day11/
    ├── 1_find_intersection_of_two_linked_lists.py              # Intersection of Two Linked Lists
    ├── 2_detect_a_cycle_in_linked_list.py                      # Detect a Cycle in a Linked List
    └── 3_reverse_ll_in_group_of_size_k.py                      # Reverse Nodes in k-Group
```

## Problems

### Day 1 — Arrays

| # | Problem | Approaches | Best Time | Best Space |
|---|---------|------------|-----------|------------|
| 1 | [Set Matrix Zeroes](Day1/1_set_matrix_zero) | Brute force, Better, Optimal | O(M·N) | O(1) |
| 2 | [Pascal's Triangle](Day1/2_pascal_triangle.py) | Brute force, Better, Optimal | O(N·K) | O(1) |
| 3 | [Next Permutation](Day1/3_next_permutation.py) | Brute force, Optimal | O(N) | O(1) |

#### 1. Set Matrix Zeroes
Given an `M × N` matrix, if an element is `0`, set its entire row and column to `0` — in place.
- **Brute force** — mark cells with a sentinel, then convert. `O((M·N)·(M+N))` time, `O(1)` space.
- **Better** — track zero rows/columns in two boolean arrays. `O(M·N)` time, `O(M+N)` space.
- **Optimal** — use the first row and column as markers. `O(M·N)` time, `O(1)` space.

#### 2. Pascal's Triangle
- **Brute force** — build the full triangle row by row.
- **Better** — generate a single row using the binomial coefficient relation.
- **Optimal** — compute a single element `C(r-1, c-1)` directly.

#### 3. Next Permutation
Rearrange numbers into the lexicographically next greater permutation, in place.
- **Brute force** — generate all permutations, sort, and pick the next one. Expensive: `O(N! · N)`.
- **Optimal** — find the pivot, swap with the next greater element, then reverse the suffix. `O(N)` time, `O(1)` space.

### Day 2 — Arrays

| # | Problem | Approaches | Best Time | Best Space |
|---|---------|------------|-----------|------------|
| 1 | [Maximum Subarray Sum (Kadane's)](Day2/1_kadane_s_algorithm_maximum_subarray_sum_in_an_array.py) | Brute force, Better, Optimal | O(N) | O(1) |
| 2 | [Sort an Array of 0s, 1s and 2s](Day2/2_sort_an_array_of_0s_1s_and_2s.py) | Brute force, Better, Optimal | O(N) | O(1) |
| 3 | [Best Time to Buy and Sell Stock](Day2/3_stock_buy_and_sell.py) | Brute force, Optimal | O(N) | O(1) |

#### 1. Maximum Subarray Sum (Kadane's Algorithm)
Find the largest sum of any contiguous subarray.
- **Brute force** — try every subarray and track the maximum sum. `O(N²)` time, `O(1)` space.
- **Better / Optimal** — Kadane's algorithm: extend the running sum, reset to 0 when it goes negative. `O(N)` time, `O(1)` space.
- **Optimal (with indices)** — same as Kadane's, but also tracks the start and end indices of the best subarray.

#### 2. Sort an Array of 0s, 1s and 2s
Sort an array containing only `0`, `1`, and `2` in place.
- **Brute force** — count each value, then overwrite the array.
- **Better** — count each value, then fill ranges by count.
- **Optimal** — Dutch National Flag algorithm with `low`, `mid`, `high` pointers in a single pass. `O(N)` time, `O(1)` space.

#### 3. Best Time to Buy and Sell Stock
Maximize profit from a single buy-then-sell.
- **Brute force** — check every buy/sell pair. `O(N²)` time, `O(1)` space.
- **Optimal** — track the minimum price seen so far and the best profit against it. `O(N)` time, `O(1)` space.

### Day 3 — Arrays

| # | Problem | Approaches | Best Time | Best Space |
|---|---------|------------|-----------|------------|
| 1 | [Rotate Image by 90°](Day3/1_Rotate_omage_by_90_degree.py) | Brute force, Optimal | O(N²) | O(1) |
| 2 | [Merge Overlapping Intervals](Day3/2_merge_overlapping_sub_intervals.py) | Brute force, Optimal | O(N log N) | O(N) |
| 3 | [Merge Two Sorted Arrays Without Extra Space](Day3/3_merge_two_sorted_arrays_without_extra_space.py) | Optimal | O(M+N) | O(1) |

#### 1. Rotate Image by 90°
Rotate an `N × N` matrix 90° clockwise.
- **Brute force** — copy each element into a new matrix at its rotated position. `O(N²)` time, `O(N²)` space.
- **Optimal** — transpose the matrix in place, then reverse each row. `O(N²)` time, `O(1)` space.

#### 2. Merge Overlapping Intervals
Given a list of intervals, merge all that overlap.
- **Brute force** — sort, then for each interval scan ahead to absorb every overlapping neighbour. `O(N log N)` time, `O(N)` space.
- **Optimal** — sort, then sweep once, extending the last merged interval or appending a new one. `O(N log N)` time, `O(N)` space.

#### 3. Merge Two Sorted Arrays Without Extra Space
Merge `nums2` into `nums1`, which has trailing space for the combined result.
- **Optimal** — fill `nums1` from the back, comparing the largest remaining elements of both arrays. `O(M+N)` time, `O(1)` space.

### Day 4 — Arrays

| # | Problem | Approaches | Best Time | Best Space |
|---|---------|------------|-----------|------------|
| 1 | [Find the Duplicate Number](Day4/1_find_the_duplicate_in_an_array.py) | Brute force, Better, Optimal | O(N) | O(1) |
| 2 | [Repeating and Missing Numbers](Day4/2_find_the_repeating_and_missing_numbers.py) | Brute force, Better, Optimal | O(N) | O(1) |
| 3 | [Count Inversions](Day4/3_count_inversions_in_an_array.py) | Brute force, Optimal | O(N log N) | O(N) |

#### 1. Find the Duplicate Number
Given `N+1` integers in the range `[1, N]`, find the single repeated number.
- **Brute force** — sort, then scan for adjacent equal elements. `O(N log N)` time, `O(1)` space.
- **Better** — count frequencies in a hash array, return the first value seen twice. `O(N)` time, `O(N)` space.
- **Optimal** — Floyd's cycle detection (slow/fast pointers) treating values as next-node links. `O(N)` time, `O(1)` space.

#### 2. Find the Repeating and Missing Numbers
In an array of `[1, N]` with one number repeated and one missing, find both.
- **Brute force** — count occurrences of each value `1..N`. `O(N²)` time, `O(1)` space.
- **Better** — tally frequencies in a hash array, then scan for the count-2 and count-0 values. `O(N)` time, `O(N)` space.
- **Optimal (math)** — solve from the sum and sum-of-squares differences. `O(N)` time, `O(1)` space.
- **Optimal (XOR)** — XOR all elements and `1..N`, split by a differing bit to isolate both numbers. `O(N)` time, `O(1)` space.

#### 3. Count Inversions
Count pairs `(i, j)` with `i < j` and `arr[i] > arr[j]`.
- **Brute force** — check every pair. `O(N²)` time, `O(1)` space.
- **Optimal** — merge sort, counting cross-pair inversions during each merge. `O(N log N)` time, `O(N)` space.

### Day 5 — Search & Math

| # | Problem | Approaches | Best Time | Best Space |
|---|---------|------------|-----------|------------|
| 1 | [Search in a Sorted 2D Matrix](Day5/1_search_in_a_sorted_2d_matrix.py) | Brute force, Better, Optimal | O(log(M·N)) | O(1) |
| 2 | [Pow(x, n)](Day5/2_x_raised_to_the_power_n.py) | Brute force, Optimal | O(log N) | O(log N) |
| 3 | [Majority Element (> N/2)](Day5/3_majority_element_that_occurs_more_than_half_of_n_times.py) | Brute force, Better, Optimal | O(N) | O(1) |

#### 1. Search in a Sorted 2D Matrix
Search for a target in a matrix where each row is sorted and the first element of each row exceeds the last of the previous.
- **Brute force** — scan every cell. `O(M·N)` time, `O(1)` space.
- **Better** — pick the candidate row by range, then binary search it. `O(M + log N)` time, `O(1)` space.
- **Optimal** — treat the matrix as one flattened sorted array and binary search it. `O(log(M·N))` time, `O(1)` space.

#### 2. Pow(x, n)
Compute `x` raised to the power `n`.
- **Brute force** — multiply `x` by itself `|n|` times, inverting for negative `n`. `O(N)` time, `O(1)` space.
- **Optimal** — binary exponentiation: square the base and halve the exponent. `O(log N)` time, `O(log N)` space (recursion).

#### 3. Majority Element (> N/2 times)
Find the element appearing more than `N/2` times.
- **Brute force** — count occurrences of each element. `O(N²)` time, `O(1)` space.
- **Better** — tally counts in a hash map, return the one exceeding `N/2`. `O(N)` time, `O(N)` space.
- **Optimal** — Boyer–Moore voting algorithm, with a final verification pass. `O(N)` time, `O(1)` space.

### Day 6 — Arrays & DP

| # | Problem | Approaches | Best Time | Best Space |
|---|---------|------------|-----------|------------|
| 1 | [Majority Element (> N/3)](Day6/1_find_elements_that_appears_more_than_N_of_3_times.py) | Brute force, Better, Optimal | O(N) | O(1) |
| 2 | [Grid Unique Paths](Day6/2_grid_unique_paths.py) | Optimal (DP) | O(M·N) | O(N) |
| 3 | [Count Reverse Pairs](Day6/3_count_reverse_pairs.py) | Optimal | O(N log N) | O(N) |

#### 1. Majority Element (> N/3 times)
Find all elements appearing more than `N/3` times (at most two).
- **Brute force** — count occurrences of each element, skipping ones already added. `O(N²)` time, `O(1)` space.
- **Better** — tally counts in a hash map, collect those reaching `N/3 + 1`. `O(N)` time, `O(N)` space.
- **Optimal** — extended Boyer–Moore voting with two candidates, then a verification pass. `O(N)` time, `O(1)` space.

#### 2. Grid Unique Paths
Count the distinct paths from the top-left to the bottom-right of an `M × N` grid, moving only right or down.
- **Optimal (DP)** — roll a single row, accumulating `up + left` for each cell. `O(M·N)` time, `O(N)` space.

#### 3. Count Reverse Pairs
Count pairs `(i, j)` with `i < j` and `arr[i] > 2 · arr[j]`.
- **Optimal** — merge sort, counting qualifying cross pairs before each merge. `O(N log N)` time, `O(N)` space.

### Day 7 — Two Pointers & Hashing

| # | Problem | Approaches | Best Time | Best Space |
|---|---------|------------|-----------|------------|
| 1 | [Two Sum](Day7/1_two_sum.py) | Optimal | O(N log N) | O(N) |
| 2 | [4Sum](Day7/2_four_sum.py) | Optimal | O(N³) | O(1) |
| 3 | [Longest Consecutive Sequence](Day7/3_longest_consecutive_sequence_in_array.py) | Optimal | O(N) | O(N) |

#### 1. Two Sum
Find whether two elements sum to a target — both as a yes/no check and returning their indices.
- **Optimal** — pair each value with its index, sort by value, then close in with two pointers from both ends. `O(N log N)` time, `O(N)` space.

#### 2. 4Sum
Find all unique quadruplets that sum to the target.
- **Optimal** — sort, fix the first two elements with deduping, then two-pointer scan the rest, skipping duplicates. `O(N³)` time, `O(1)` space (excluding output).

#### 3. Longest Consecutive Sequence
Find the length of the longest run of consecutive integers in an unsorted array.
- **Optimal** — load values into a set, start a count only at sequence heads (no value one less present), and extend forward. `O(N)` time, `O(N)` space.

### Day 8 — Prefix Sums & Hashing

| # | Problem | Approaches | Best Time | Best Space |
|---|---------|------------|-----------|------------|
| 1 | [Longest Subarray with Sum Zero](Day8/1_length_of_longest_subarray_with_zero_sum.py) | Optimal | O(N) | O(N) |
| 2 | [Subarrays with XOR K](Day8/2_count_the_number_of_subarrays_with_given_xor_K.py) | Optimal | O(N) | O(N) |
| 3 | [Longest Substring Without Repeating Characters](Day8/3_length_of_longest_substring_without_any_repeating_character.py) | Optimal | O(N) | O(1) |

#### 1. Longest Subarray with Sum Zero
Find the length of the longest contiguous subarray that sums to zero.
- **Optimal** — track running prefix sums in a hash map; when a sum repeats (or hits zero), the span between is a zero-sum subarray. `O(N)` time, `O(N)` space.

#### 2. Count Subarrays with XOR K
Count the contiguous subarrays whose XOR equals `K`.
- **Optimal** — keep prefix-XOR frequencies in a hash map; for each prefix, add the count of the complementary prefix (`prefix ^ K`). `O(N)` time, `O(N)` space.

#### 3. Longest Substring Without Repeating Characters
Find the length of the longest substring with all distinct characters.
- **Optimal** — sliding window with a last-seen index per character; jump the left bound past any repeat. `O(N)` time, `O(1)` space (fixed 256-char table).

### Day 9 — Linked Lists

| # | Problem | Approaches | Best Time | Best Space |
|---|---------|------------|-----------|------------|
| 1 | [Reverse a Linked List](Day9/1_reverse_ll.py) | Optimal (recursive) | O(N) | O(N) |
| 2 | [Middle of a Linked List](Day9/2_find_middle_of_ll.py) | Optimal | O(N) | O(1) |
| 3 | [Merge Two Sorted Lists](Day9/3_merge_two_sorted_lists.py) | Optimal | O(M+N) | O(1) |

#### 1. Reverse a Linked List
Reverse a singly linked list.
- **Optimal (recursive)** — recurse to the tail, then flip each `next` pointer on the way back. `O(N)` time, `O(N)` space (call stack).

#### 2. Middle of a Linked List
Return the middle node of a linked list.
- **Optimal** — slow/fast pointers; when fast reaches the end, slow sits at the middle. `O(N)` time, `O(1)` space.

#### 3. Merge Two Sorted Lists
Merge two sorted linked lists into one sorted list.
- **Optimal** — splice nodes onto a dummy head, always taking the smaller front, then attach the remaining tail. `O(M+N)` time, `O(1)` space.

### Day 10 — Linked Lists

| # | Problem | Approaches | Best Time | Best Space |
|---|---------|------------|-----------|------------|
| 1 | [Remove Nth Node From End](Day10/1_remove_N_th_node_from_the_end_of_a_Linked_List.py) | Optimal | O(N) | O(1) |
| 2 | [Add Two Numbers](Day10/2_add_2_numbsers_represented_as_ll.py) | Optimal | O(max(M,N)) | O(1) |
| 3 | [Delete a Given Node](Day10/3_delete_given_node_in_a_ll.py) | Optimal | O(1) | O(1) |

#### 1. Remove Nth Node From End
Remove the `N`th node counting from the end of the list.
- **Optimal** — advance a fast pointer `N+1` steps ahead of a slow one from a dummy head, then move both until fast falls off; slow now precedes the target. `O(N)` time, `O(1)` space.

#### 2. Add Two Numbers
Add two numbers stored as digit-per-node linked lists (least significant first).
- **Optimal** — walk both lists together, summing with a carry and building the result on a dummy head. `O(max(M,N))` time, `O(1)` space (excluding output).

#### 3. Delete a Given Node
Delete a node given only a reference to it (not the head).
- **Optimal** — copy the next node's value into this node, then unlink the next node. `O(1)` time, `O(1)` space.

### Day 11 — Linked Lists

| # | Problem | Approaches | Best Time | Best Space |
|---|---------|------------|-----------|------------|
| 1 | [Intersection of Two Linked Lists](Day11/1_find_intersection_of_two_linked_lists.py) | Optimal | O(M+N) | O(1) |
| 2 | [Detect a Cycle in a Linked List](Day11/2_detect_a_cycle_in_linked_list.py) | Hashing | O(N) | O(N) |
| 3 | [Reverse Nodes in k-Group](Day11/3_reverse_ll_in_group_of_size_k.py) | Optimal | O(N) | O(1) |

#### 1. Intersection of Two Linked Lists
Find the node where two singly linked lists merge, if any.
- **Optimal** — walk both lists with two pointers, redirecting each to the other list's head on reaching the end; they align at the intersection (or both at `None`) after equalising the path lengths. `O(M+N)` time, `O(1)` space.

#### 2. Detect a Cycle in a Linked List
Determine whether the list contains a cycle.
- **Hashing** — record each visited node in a set; a node seen twice means a loop. `O(N)` time, `O(N)` space.

#### 3. Reverse Nodes in k-Group
Reverse the list in consecutive groups of `k`, leaving a trailing remainder untouched.
- **Optimal** — for each full group, locate the `k`th node, reverse the group's links in place, then splice it back between the surrounding nodes via a dummy head. `O(N)` time, `O(1)` space.

## Running

Each file is self-contained and runs the included sample driver:

```bash
python3 Day1/2_pascal_triangle.py
python3 Day1/3_next_permutation.py
python3 Day2/1_kadane_s_algorithm_maximum_subarray_sum_in_an_array.py
python3 Day2/2_sort_an_array_of_0s_1s_and_2s.py
python3 Day2/3_stock_buy_and_sell.py
python3 Day3/1_Rotate_omage_by_90_degree.py
python3 Day3/2_merge_overlapping_sub_intervals.py
python3 Day3/3_merge_two_sorted_arrays_without_extra_space.py
python3 Day4/1_find_the_duplicate_in_an_array.py
python3 Day4/2_find_the_repeating_and_missing_numbers.py
python3 Day4/3_count_inversions_in_an_array.py
python3 Day5/1_search_in_a_sorted_2d_matrix.py
python3 Day5/2_x_raised_to_the_power_n.py
python3 Day5/3_majority_element_that_occurs_more_than_half_of_n_times.py
python3 Day6/1_find_elements_that_appears_more_than_N_of_3_times.py
python3 Day6/2_grid_unique_paths.py
python3 Day6/3_count_reverse_pairs.py
python3 Day7/1_two_sum.py
python3 Day7/2_four_sum.py
python3 Day7/3_longest_consecutive_sequence_in_array.py
python3 Day8/1_length_of_longest_subarray_with_zero_sum.py
python3 Day8/2_count_the_number_of_subarrays_with_given_xor_K.py
python3 Day8/3_length_of_longest_substring_without_any_repeating_character.py
python3 Day9/1_reverse_ll.py
python3 Day9/2_find_middle_of_ll.py
python3 Day9/3_merge_two_sorted_lists.py
python3 Day10/1_remove_N_th_node_from_the_end_of_a_Linked_List.py
python3 Day10/2_add_2_numbsers_represented_as_ll.py
python3 Day10/3_delete_given_node_in_a_ll.py
python3 Day11/1_find_intersection_of_two_linked_lists.py
python3 Day11/2_detect_a_cycle_in_linked_list.py
python3 Day11/3_reverse_ll_in_group_of_size_k.py
```

The matrix file has no `.py` extension; run it explicitly through Python:

```bash
python3 Day1/1_set_matrix_zero
```

## Goal

Work through the sheet one day at a time, implementing each problem with
increasingly efficient approaches and documenting the complexity trade-offs.

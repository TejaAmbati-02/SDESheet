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
└── Day2/
    ├── 1_kadane_s_algorithm_maximum_subarray_sum_in_an_array.py   # Maximum Subarray Sum
    ├── 2_sort_an_array_of_0s_1s_and_2s.py                         # Sort 0s, 1s and 2s
    └── 3_stock_buy_and_sell.py                                    # Best Time to Buy and Sell Stock
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

## Running

Each file is self-contained and runs the included sample driver:

```bash
python3 Day1/2_pascal_triangle.py
python3 Day1/3_next_permutation.py
python3 Day2/1_kadane_s_algorithm_maximum_subarray_sum_in_an_array.py
python3 Day2/2_sort_an_array_of_0s_1s_and_2s.py
python3 Day2/3_stock_buy_and_sell.py
```

The matrix file has no `.py` extension; run it explicitly through Python:

```bash
python3 Day1/1_set_matrix_zero
```

## Goal

Work through the sheet one day at a time, implementing each problem with
increasingly efficient approaches and documenting the complexity trade-offs.

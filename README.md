# Algorithms

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Sora&weight=700&size=22&duration=2800&pause=1000&color=6C63FF&center=true&vCenter=true&width=700&lines=150+Problems.+30+Patterns.+1+Repo.;Hash+Maps+%C2%B7+Two+Pointers+%C2%B7+DP+%C2%B7+Graphs+%C2%B7+Backtracking;Pattern-first+DSA+practice+in+Python;Built+for+recognizing+the+shape%2C+not+memorizing+the+problem.)](https://git.io/typing-svg)

</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Patterns](https://img.shields.io/badge/Patterns-30-6C63FF?style=for-the-badge)
![Problems](https://img.shields.io/badge/Problems-150-DC244C?style=for-the-badge)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

</div>

---

## Overview

**Algorithms** is a personal Data Structures & Algorithms practice repository, organized by *pattern* rather than by difficulty or source. Each of the 30 folders represents one recurring problem-solving pattern (hash maps, two pointers, sliding window, backtracking, and so on), and every file inside is a standalone Python solution to a specific problem that pattern applies to.

The goal isn't to grind problems in random order — it's to drill the underlying technique until the pattern is recognizable on sight, then apply it across five related problems per folder to confirm the recognition actually transfers.

**Repository** → [github.com/Fuad-Haque/algorithms](https://github.com/Fuad-Haque/algorithms)

---

## Table of Contents

- [Features](#features)
- [Structure](#structure)
- [Patterns](#patterns)
- [File Naming Convention](#file-naming-convention)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Progress Tracker](#progress-tracker)
- [Notes on Repeated Problems](#notes-on-repeated-problems)
- [Author](#author)

---

## Features

| Feature | Detail |
|---|---|
| Pattern-First Organization | 30 numbered folders, each isolating one core technique instead of mixing techniques by topic |
| Five Problems per Pattern | Each folder walks the same pattern across five progressively varied problems |
| One File, One Problem | Every solution lives in its own `snake_case.py` file — no bundling, no notebooks |
| Language-Consistent | Every solution written in Python for direct comparison across patterns |
| Cross-Pattern Callbacks | A handful of problems (e.g. *Find the Duplicate Number*, *Merge k Sorted Lists*) appear in more than one folder on purpose — see [Notes on Repeated Problems](#notes-on-repeated-problems) |
| Self-Contained Files | Each file is runnable on its own — no shared imports across problems |

---

## Structure

```
Pattern Folder (e.g. 01_Hash_Map_Complement_Lookup)
│
├── Problem 1 → two_sum.py
├── Problem 2 → 3sum.py
├── Problem 3 → 4sum.py
├── Problem 4 → two_sum_ii.py
└── Problem 5 → two_sum_less_than_k.py
```

Every one of the 30 folders follows this same shape: five files, one pattern, increasing variation in constraints (sorted vs. unsorted input, extra space limits, multiple valid outputs, etc.) so the pattern gets tested from a few different angles rather than just once.

---

## Patterns

| # | Folder | Pattern | Core Idea |
|---|---|---|---|
| 01 | `01_Hash_Map_Complement_Lookup` | Hash Map / Complement Lookup | Trade space for O(1) lookups to find pairs/tuples summing to a target |
| 02 | `02_Single_Pass_Greedy_Buy_Sell` | Single Pass / Greedy | Track running min/max in one pass to maximize profit under constraints |
| 03 | `03_Hash_Set_Duplicate_Detection` | Hash Set | Detect duplicates or missing values in O(n) using set membership |
| 04 | `04_Hash_Set_Sequence` | Hash Set + Sequence Building | Use a set to build or detect consecutive runs in unsorted data |
| 05 | `05_Hashing_Sorted_Key_Anagrams` | Hashing with Sorted Key | Use a sorted string or char-count tuple as a hash key to group anagrams |
| 06 | `06_Frequency_Counting` | Frequency Counting | Compare character/element counts between two inputs |
| 07 | `07_Prefix_Suffix_Arrays` | Prefix & Suffix Arrays | Precompute left-to-right and right-to-left running values to avoid recomputation |
| 08 | `08_Stack_Parentheses` | Stack | Match/validate nested structures using a LIFO stack |
| 09 | `09_Linked_List_Reversal` | Linked List Reversal | Reverse pointers iteratively or recursively, in full or in a sub-range |
| 10 | `10_Floyds_Tortoise_Hare` | Floyd's Tortoise and Hare | Fast/slow pointers to detect cycles in O(1) space |
| 11 | `11_Merging_Sorted_Lists` | Merging Sorted Lists | Two-pointer merge of sorted linked structures |
| 12 | `12_Heap_Divide_Conquer` | Heap / Divide & Conquer | Min-heap or divide-and-conquer for k-way merge problems |
| 13 | `13_Two_Pointers_Fast_Slow` | Two Pointers (Fast‑Slow with Gap) | Maintain a fixed gap between two pointers to find/remove nodes from the end |
| 14 | `14_Basic_Binary_Search` | Basic Binary Search | Classic O(log n) search over a sorted, monotonic search space |
| 15 | `15_Binary_Search_Rotated` | Binary Search on Rotated Array | Binary search adapted to a rotated (but still piecewise sorted) array |
| 16 | `16_BST_Validation` | BST Validation / In‑order Property | Exploit the in-order traversal property to validate or navigate a BST |
| 17 | `17_BFS_Level_Order` | BFS / Level Order Traversal | Queue-based level-by-level traversal of a tree |
| 18 | `18_Tree_DFS_Depth` | Tree DFS (Depth / Height) | Recursive depth computation and comparison across subtrees |
| 19 | `19_Tree_Recursion_LCA` | Tree Recursion (LCA / Path) | Recursive path-finding and lowest common ancestor logic |
| 20 | `20_Tree_Recursion_Mirror` | Tree Recursion (Mirror / Transformation) | Recursive tree transformation — invert, merge, prune, rebuild |
| 21 | `21_Graph_Traversal_BFS_DFS` | Graph Traversal — Connected Components | BFS/DFS over a grid or graph to find connected regions |
| 22 | `22_Topological_Sort` | Topological Sort / Cycle Detection | Order nodes under directed dependencies; detect cycles |
| 23 | `23_Trie_Prefix_Tree` | Trie (Prefix Tree) | Prefix-based tree structure for word storage and lookup |
| 24 | `24_Heap_Bucket_Sort` | Heap / Bucket Sort (Top K) | Find the k most/least significant elements without a full sort |
| 25 | `25_Sliding_Window` | Sliding Window (Variable Length) | Expand/contract a window over a sequence to satisfy a constraint |
| 26 | `26_1D_DP_Fibonacci` | 1D DP (Fibonacci / Climbing Stairs) | Bottom-up DP with O(1) or O(n) state, building on prior subproblems |
| 27 | `27_DP_Unbounded_Knapsack` | DP – Unbounded Knapsack / Coin Change | DP over unlimited-use items to hit a target sum or count combinations |
| 28 | `28_Backtracking` | Backtracking | Explore/prune a decision tree to enumerate subsets, permutations, combinations |
| 29 | `29_Intervals` | Intervals | Sort by start/end and sweep to merge, insert, or count overlaps |
| 30 | `30_Monotonic_Stack` | Monotonic Stack | Maintain an increasing/decreasing stack to find next-greater/smaller elements |

---

## File Naming Convention

Every problem file is named in `snake_case`, derived directly from the problem title:

```
Two Sum                          → two_sum.py
Best Time to Buy and Sell Stock  → best_time_to_buy_and_sell_stock.py
Kth Smallest Element in a BST    → kth_smallest_element_in_a_bst.py
```

Roman numerals in a title (e.g. "II", "III") are kept as-is rather than converted to digits, so `Contains Duplicate III` becomes `contains_duplicate_iii.py`, not `contains_duplicate_3.py`.

---

## Quick Start

Clone the repository:

```bash
git clone https://github.com/Fuad-Haque/algorithms
cd algorithms
```

Run any individual solution directly:

```bash
python 01_Hash_Map_Complement_Lookup/two_sum.py
```

No dependencies, virtual environment, or `requirements.txt` needed — every file is plain, self-contained Python 3.

---

## Project Structure

```
algorithms/
├── 01_Hash_Map_Complement_Lookup/
│   ├── two_sum.py
│   ├── 3sum.py
│   ├── 4sum.py
│   ├── two_sum_ii.py
│   └── two_sum_less_than_k.py
├── 02_Single_Pass_Greedy_Buy_Sell/
│   ├── best_time_to_buy_and_sell_stock.py
│   ├── best_time_to_buy_and_sell_stock_ii.py
│   ├── best_time_to_buy_and_sell_stock_iii.py
│   ├── best_time_to_buy_and_sell_stock_with_cooldown.py
│   └── best_time_to_buy_and_sell_stock_with_transaction_fee.py
├── 03_Hash_Set_Duplicate_Detection/
│   ├── contains_duplicate.py
│   ├── contains_duplicate_ii.py
│   ├── contains_duplicate_iii.py
│   ├── missing_number.py
│   └── find_the_duplicate_number.py
├── 04_Hash_Set_Sequence/
│   ├── longest_consecutive_sequence.py
│   ├── first_missing_positive.py
│   ├── find_all_numbers_disappeared_in_an_array.py
│   ├── minimum_number_of_operations_to_make_array_continuous.py
│   └── maximum_gap.py
├── 05_Hashing_Sorted_Key_Anagrams/
│   ├── group_anagrams.py
│   ├── valid_anagram.py
│   ├── find_all_anagrams_in_a_string.py
│   ├── group_shifted_strings.py
│   └── minimum_number_of_steps_to_make_two_strings_anagram.py
├── 06_Frequency_Counting/
│   ├── valid_anagram.py
│   ├── ransom_note.py
│   ├── palindrome_permutation.py
│   ├── find_the_difference.py
│   └── isomorphic_strings.py
├── 07_Prefix_Suffix_Arrays/
│   ├── product_of_array_except_self.py
│   ├── trapping_rain_water.py
│   ├── find_pivot_index.py
│   ├── replace_elements_with_greatest_element_on_right_side.py
│   └── minimum_number_of_operations_to_move_all_balls_to_each_box.py
├── 08_Stack_Parentheses/
│   ├── valid_parentheses.py
│   ├── longest_valid_parentheses.py
│   ├── minimum_add_to_make_parentheses_valid.py
│   ├── remove_invalid_parentheses.py
│   └── check_if_a_parentheses_string_can_be_valid.py
├── 09_Linked_List_Reversal/
│   ├── reverse_linked_list.py
│   ├── reverse_linked_list_ii.py
│   ├── palindrome_linked_list.py
│   ├── swap_nodes_in_pairs.py
│   └── reverse_nodes_in_k_group.py
├── 10_Floyds_Tortoise_Hare/
│   ├── linked_list_cycle.py
│   ├── linked_list_cycle_ii.py
│   ├── find_the_duplicate_number.py
│   ├── happy_number.py
│   └── middle_of_the_linked_list.py
├── 11_Merging_Sorted_Lists/
│   ├── merge_two_sorted_lists.py
│   ├── merge_k_sorted_lists.py
│   ├── sort_list.py
│   ├── intersection_of_two_linked_lists.py
│   └── add_two_numbers.py
├── 12_Heap_Divide_Conquer/
│   ├── merge_k_sorted_lists.py
│   ├── kth_smallest_element_in_a_sorted_matrix.py
│   ├── find_k_pairs_with_smallest_sums.py
│   ├── smallest_range_covering_elements_from_k_lists.py
│   └── top_k_frequent_elements.py
├── 13_Two_Pointers_Fast_Slow/
│   ├── remove_nth_node_from_end_of_list.py
│   ├── delete_the_middle_node_of_a_linked_list.py
│   ├── rotate_list.py
│   ├── remove_duplicates_from_sorted_list_ii.py
│   └── reorder_list.py
├── 14_Basic_Binary_Search/
│   ├── binary_search.py
│   ├── search_insert_position.py
│   ├── find_first_and_last_position_of_element_in_sorted_array.py
│   ├── sqrtx.py
│   └── guess_number_higher_or_lower.py
├── 15_Binary_Search_Rotated/
│   ├── search_in_rotated_sorted_array.py
│   ├── search_in_rotated_sorted_array_ii.py
│   ├── find_minimum_in_rotated_sorted_array.py
│   ├── find_minimum_in_rotated_sorted_array_ii.py
│   └── find_peak_element.py
├── 16_BST_Validation/
│   ├── validate_binary_search_tree.py
│   ├── recover_binary_search_tree.py
│   ├── kth_smallest_element_in_a_bst.py
│   ├── convert_sorted_array_to_binary_search_tree.py
│   └── binary_search_tree_iterator.py
├── 17_BFS_Level_Order/
│   ├── binary_tree_level_order_traversal.py
│   ├── binary_tree_zigzag_level_order_traversal.py
│   ├── binary_tree_right_side_view.py
│   ├── populating_next_right_pointers_in_each_node.py
│   └── average_of_levels_in_binary_tree.py
├── 18_Tree_DFS_Depth/
│   ├── maximum_depth_of_binary_tree.py
│   ├── balanced_binary_tree.py
│   ├── diameter_of_binary_tree.py
│   ├── same_tree.py
│   └── symmetric_tree.py
├── 19_Tree_Recursion_LCA/
│   ├── lowest_common_ancestor_of_a_binary_search_tree.py
│   ├── lowest_common_ancestor_of_a_binary_tree.py
│   ├── maximum_difference_between_node_and_ancestor.py
│   ├── all_nodes_distance_k_in_binary_tree.py
│   └── binary_tree_paths.py
├── 20_Tree_Recursion_Mirror/
│   ├── invert_binary_tree.py
│   ├── merge_two_binary_trees.py
│   ├── binary_tree_pruning.py
│   ├── increasing_order_search_tree.py
│   └── trim_a_binary_search_tree.py
├── 21_Graph_Traversal_BFS_DFS/
│   ├── number_of_islands.py
│   ├── max_area_of_island.py
│   ├── surrounded_regions.py
│   ├── pacific_atlantic_water_flow.py
│   └── rotting_oranges.py
├── 22_Topological_Sort/
│   ├── course_schedule.py
│   ├── course_schedule_ii.py
│   ├── alien_dictionary.py
│   ├── minimum_height_trees.py
│   └── parallel_courses.py
├── 23_Trie_Prefix_Tree/
│   ├── implement_trie.py
│   ├── add_and_search_word.py
│   ├── word_search_ii.py
│   ├── replace_words.py
│   └── longest_word_in_dictionary.py
├── 24_Heap_Bucket_Sort/
│   ├── top_k_frequent_elements.py
│   ├── k_closest_points_to_origin.py
│   ├── kth_largest_element_in_an_array.py
│   ├── sort_characters_by_frequency.py
│   └── top_k_frequent_words.py
├── 25_Sliding_Window/
│   ├── longest_substring_without_repeating_characters.py
│   ├── longest_substring_with_at_most_two_distinct_characters.py
│   ├── longest_substring_with_at_most_k_distinct_characters.py
│   ├── minimum_window_substring.py
│   └── subarrays_with_k_different_integers.py
├── 26_1D_DP_Fibonacci/
│   ├── climbing_stairs.py
│   ├── fibonacci_number.py
│   ├── min_cost_climbing_stairs.py
│   ├── decode_ways.py
│   └── tribonacci_number.py
├── 27_DP_Unbounded_Knapsack/
│   ├── coin_change.py
│   ├── coin_change_2.py
│   ├── perfect_squares.py
│   ├── minimum_cost_for_tickets.py
│   └── combination_sum_iv.py
├── 28_Backtracking/
│   ├── subsets.py
│   ├── subsets_ii.py
│   ├── permutations.py
│   ├── combination_sum.py
│   └── n_queens.py
├── 29_Intervals/
│   ├── merge_intervals.py
│   ├── insert_interval.py
│   ├── meeting_rooms.py
│   ├── meeting_rooms_ii.py
│   └── non_overlapping_intervals.py
└── 30_Monotonic_Stack/
    ├── next_greater_element_i.py
    ├── daily_temperatures.py
    ├── largest_rectangle_in_histogram.py
    ├── trapping_rain_water.py
    └── sum_of_subarray_minimums.py
```

---

## Progress Tracker

| Range | Patterns | Focus Area |
|---|---|---|
| 01 – 07 | Hashing & Arrays | Hash maps/sets, prefix sums, greedy single-pass |
| 08 – 13 | Linked Lists & Stacks | Reversal, cycle detection, merging, fast/slow pointers |
| 14 – 20 | Binary Search & Trees | Search space reduction, BST properties, tree recursion |
| 21 – 24 | Graphs & Heaps | Traversal, topological sort, tries, top-k selection |
| 25 – 30 | Windows, DP & Backtracking | Sliding window, 1D/knapsack DP, backtracking, intervals, monotonic stack |

---

## Notes on Repeated Problems

A few problems intentionally appear in more than one folder, since they're valid entry points for more than one pattern:

| Problem | Folders | Why |
|---|---|---|
| `find_the_duplicate_number.py` | `03_Hash_Set_Duplicate_Detection`, `10_Floyds_Tortoise_Hare` | Solvable with a hash set (O(n) space) or with Floyd's cycle detection (O(1) space) — both are worth practicing |
| `valid_anagram.py` | `05_Hashing_Sorted_Key_Anagrams`, `06_Frequency_Counting` | Solvable by sorting both strings or by comparing character counts |
| `merge_k_sorted_lists.py` | `11_Merging_Sorted_Lists`, `12_Heap_Divide_Conquer` | Solvable with pairwise two-list merging or with a min-heap across all lists |
| `top_k_frequent_elements.py` | `12_Heap_Divide_Conquer`, `24_Heap_Bucket_Sort` | Solvable with a heap or with bucket sort by frequency |
| `trapping_rain_water.py` | `07_Prefix_Suffix_Arrays`, `30_Monotonic_Stack` | Solvable with precomputed prefix/suffix max arrays or with a monotonic stack |

Each appearance is a deliberate re-solve using that folder's specific technique, not a duplicate file left in by accident.

---

## Author

Built by [Fuad Haque](https://github.com/Fuad-Haque)

[GitHub](https://github.com/Fuad-Haque)

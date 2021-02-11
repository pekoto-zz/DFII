## Red-Black Trees
A red-black tree is a self-balancing binary search tree.

Each node uses an extra bit to represent color (red or black), and certain properties are used to ensure the tree remains balanced.

In Java 8, the HashMap was modified to use a red-black tree instead of a LinkedList to store colliding elements, reducing time from O(n) to O(log n).

|   	 |   Avg	 | Worst Case  	|
|---	 |---     	 |---	        |
| Space  | O(n)      | O(n)         |
| Find   | O(log n)  | O(log n)     |
| Insert | O(log n)  | O(log n)     |
| Delete | O(log n)  | O(log n)     |
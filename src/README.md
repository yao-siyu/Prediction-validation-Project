This is the main python code.

- A sliding_window is adopted to maintain the rolling source data over a pre-defined window size of K.
- Deque is used for the sliding_window implementation based on its optimized performance, i.e., amortized O(1) time complexity for pop() and append() operations.

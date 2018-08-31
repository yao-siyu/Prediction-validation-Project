# Siyu's Prediction-Validation-Project

- Main python code: ./src/prediction-validation.py
  - A sliding_window is adopted to maintain the rolling source data over a pre-defined window size of K. 
  - Deque is used for the sliding_window implementation based on its optimized performance, i.e., amortized O(1) time complexity for pop() and append() operations.


- Test Cases (TC) validations for both Functionality and Performance: ./insight_testsuite/tests/test_1-9
  - TC1: Given TC with over ~1000 actual and predicted stock prices and window size of 4
  - TC2: Modified TC1 with larger window size of 1000
  - TC3: Large actual data (~1000) and very small predicted data (less than 10) with window size of 4
  - TC4: Modified TC3 with larger window size of 1000
  - TC5: Valid actual data, but invalid predicted data
  - TC6: Valid predicted data, but invalid actual data 
  - TC7: Negative TC: window size larger than actual data size
  - TC8: Negative TC: (invalid) window size of 0
  - TC9: Negative TC: predicted data not exist in actual data


- Time complexity analysis:
  - Total System Time complexicity: O(NK) # N is # of predicated stocks, K is the window size
  - Calculate errors at given hour over all source file (N predicated sotcks): O(N) # need to iterate each stock, but no repeated iterations
  - Maintain and save record at each (given) window size K: O(1) * O(K) # O(1) for pop() or append(), K is the window size
 
  
- Further Improvements provided more resources:
  - Has limited time (5 hours) to complete the project due to tight full-time work;
  - Further optimizations on time complexity might be possible;
  - Consider use Map reduce for larger scale data;
  - Extensive test case validation.

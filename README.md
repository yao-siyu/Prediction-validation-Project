# Siyu's Prediction-Validation-Project

- Main python code: ./src/prediction-validation.py


- A sliding_window is adopted to maintain the rolling source data over a pre-defined window size of K. 
- Deque is used for the sliding_window implementation based on its optimized performance, i.e., amortized O(1) time complexity for pop() and append() operations.


- Various test cases (TC) have been tested and verified (for both Functionality and Performance of python source code):
  - TC1: Normal TC with small actual.txt (tested againest given ~10 actual stock prices and window size 2)
  - TC2: Normal TC with larger actual.txt (tested againest given ~1000 actual stock prices and SMALL window size 4)
  - TC3: Normal TC with larger actual.txt (tested againest given ~1000 actual stock prices and LARGE window size 200)
  - TC4: Large actual.txt and very small predicted.txt
  - TC5: Large window size and small window size 
  - TC6: Invalid actual.txt or predicted.txt or window.txt
  - TC7: Valid actual.txt with Empty predicted.txt
  - TC8: Empty actual.txt with un-Empty predicted.txt


- Time complexity analysis:
  - Total System Time complexicity: O(NK) # N is # of predicated stocks, K is the window size
  - Calculate errors at given hour over all source file (N predicated sotcks): O(N) # need to iterate each stock, but no repeated iterations
  - Maintain and save record at each (given) window size K: O(1) * O(K) # O(1) for pop() or append(), K is the window size
 
  
- Further Improvements provided more resources:
  - Has limited time (5 hours) to complete the project due to tight full-time work;
  - Further optimizations on time complexity might be possible;
  - Consider use Map reduce for larger scale data;
  - Extensive test case validation.

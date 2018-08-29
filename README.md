# Prediction Validation Project
- Solution in Python3: src/prediction-validation.py

- Use a quene to maintain and update the calculated errors in a given window, more details available in the code comments

- Time complexity analysis:
  - Get stock price for each stock at a given hour: O(n)
  - Calculate total counts of matching stocks and their total errors at a given hour: O(n)
  - Calculate average error of a given window, a quene used: O(n)
  
- Test cases created in insight_testsuite/tests
  - Test_1: Initial test case from Insight
  - Test_2: Edge case of no matching stock in a given window
  - Test_3: 

- Improvements if there is more time:
  - Make the main code more organized and clearer
  - Add more test cases 


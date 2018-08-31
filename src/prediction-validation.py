import collections
import sys


class HourStats(object):
    """
    Args:
        error_sum (float): sum of the obtained errors.
        error_count (int): total number of the obtained errors.

    Attributes:
        error_sum (float): sum of the obtained errors.
        error_count (int): total number of the obtained errors.

    """
    def __init__(self, error_sum, error_count):
        self.error_sum = error_sum
        self.error_count = error_count


def GetPricesAtHour(source, index, hour):
    """GetPricesAtHour.

    Args:
        source (list):	The source data.
        index (int):	The interested source data's index.
	hour (int):	The interested hour

    Returns:
	stock_price (list):	The obtained stock_price list
	index (int):	The ending index of the obtained stock_price
    
    """ 
    stock_price = {}
    while index < len(source):
        item = source[index].strip()
        if not item: # to deal with edge case of NULL item
            index += 1
            continue

        hr, name, price = item.split('|')
        if int(hr) == hour:
            stock_price[name] = float(price)
            index += 1
            continue
        break # to break out call earlier when the interested hour completed
    return stock_price, index

try: 
    with open(sys.argv[1], 'r') as window_file:
        window = int(window_file.read().strip())
    if window <= 0:
        print('Window size must be a positive integer!')
        sys.exit(1)
except IOError as e:
        print('Error in opening file!')
        print(e)

try: 
    with open(sys.argv[2], 'r') as actual_file:
        sourceActual = actual_file.readlines()
except IOError as e:
        print('Error in opening file!')
        print(e)

try:
    with open(sys.argv[3], 'r') as predicted_file:
        sourcePredicted = predicted_file.readlines()
except IOError as e:
        print('Error in opening file!')
        print(e)


""" 
Use a sliding_window to maintain the interested errors within a given window size K.
For an optimized system performance, use deque to implement the sliding_window, i.e.,
with amortized O(1) time complexicity for pop() or apend() operations.
"""

sliding_window_stats = collections.deque()
output = []
stock_price = {}
actIdx = preIdx = 0
hr = 1	# pre-defined starting hour
total = 0
count = 0

while actIdx < len(sourceActual):
    actual_prices, actIdx = GetPricesAtHour(sourceActual, actIdx, hr)
    predicted_prices, preIdx = GetPricesAtHour(sourcePredicted, preIdx, hr)
    total_errs = 0
    cnt = 0

    # To calculate each matched errors, and maintain their sum and total count
    # Time complexity is O(n), where n is number of line/number from the source file 
    for name, price in predicted_prices.items():
	if name not in actual_prices:
	    print('Invalid Stock in predictaed file detected!')
	else:
            total_errs += abs(price - actual_prices[name])
            cnt += 1

    # To use a sliding_window to update the calculated errors within the given window
    # Time complexity is O(1) for each popleft() and append() operations.
    if len(sliding_window_stats) == window:
        avg_err = total / float(count) if count != 0 else -1 # to deal with edge case of no avg_err in a window
        output.append(avg_err)
        stats = sliding_window_stats.popleft()
        total -= stats.error_sum
        count -= stats.error_count

    total += total_errs
    count += cnt
    sliding_window_stats.append(HourStats(total_errs, cnt))

    hr += 1


avg_err = total / float(count) if count != 0 else -1	# need to save avg_error in float format
output.append(avg_err)


with open(sys.argv[4], 'w') as comparison_file:
    for i, avg_err in enumerate(output):
        line = '%d|%d|' % (i + 1, i + window)
        if avg_err == -1:
            line += 'NA'	# adding mark "NA" as an invalid entry
        else:
            line += '{:0.2f}'.format(avg_err) # to save the accuracy according to predefined requirement
        comparison_file.write(line + '\n')

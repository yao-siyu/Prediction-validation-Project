from os.path import abspath, exists
import sys

#load data from files
def load_data(file_name):
    file_path = abspath(file_name)
    try:
        handle = open(file_path)
    except:
        print("Cannot find file:", file_name)

    data = []
    for line in handle:
        data.append(line)

    return data

#process data as time/stock ID pair and stock price
def process_line(data):
    dic = {}
    for record in data:
        details = record.split("|")
        pair = details[0] + "|" + details[1]
        price = float(details[2])
        dic[pair] = price

    return dic

#find the matched pair and compute error
def compute_error(actual, predicted):
    errors = {}
    for pair in predicted:
        if pair in actual:
            errors[pair] = abs(actual[pair] - predicted[pair])

    return errors

#compute average error
def average_error ():
    actual = process_line(load_data(sys.argv[2]))
    predicted = process_line(load_data(sys.argv[3]))
    errors = compute_error(actual, predicted)
    window = int(load_data(sys.argv[1])[0])
    output_file = sys.argv[4]
    res = {}
    for pair in errors:
        num = 0
        time = int(pair.split("|")[0])
        if time not in res:
            res[time] = [errors[pair], 1]
        else:
            res[time] = [res[time][0] + errors[pair], res[time][1] + 1]

    comparision = []
    for time in res:
        start = time
        end = start + window - 1
        temp = start
        total_nums = 0
        total_errors = 0
        while temp <= end:
            if temp in res:
                total_errors = total_errors + res[start][0]
                total_nums += total_nums + res[start][1]
            temp += 1
        ave_error = "{0:.2f}".format(total_errors / total_nums)
        comparision.append(str(start) + "|" + str(end) + "|" + str(ave_error))

    #Generate output
    with open(output_file, 'w') as outfile:
        for i in comparision:
            outfile.write(i + "\n")
        outfile.close

print(average_error())

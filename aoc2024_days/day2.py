print("Advent of Code 2024, Day 2!")
print("Shadowdara's Version:\n")

data_string1 = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

data_string2 = """

"""

data_string3 = """
1 2 7 8 9
9 8 7 2 1
1 2 7 8 9
9 7 6 2 1
1 3 8 9 10
"""

print("=== Part 1 ===\n")

def process_lines(input_data):
    lines = input_data.strip().split("\n")
    
    arrays = [list(map(int, line.split())) for line in lines]
    
    return arrays


result1 = process_lines(data_string1)
result2 = process_lines(data_string2)
result3 = process_lines(data_string3)

def increasing(list):
    length = len(list)
    for a in range(0, length - 1):
        if (list[a+1] - list[a]) >= 1 and (list[a+1] - list[a]) <= 3:
            pass
        else:
            return False
    return True

def decreasing(list):
    length = len(list)
    for b in range(0, length - 1):
        if (list[b] - list[b+1]) >= 1 and (list[b] - list[b+1]) <= 3:
            pass
        else:
            return False
    return True

def count2(arraylist):
    global counter
    counter = 0
    for c in range(0, len(arraylist)):
        if increasing(arraylist[c]):
            counter += 1
        if decreasing(arraylist[c]):
            counter += 1

count2(result1)

print("Test:")
print(counter)

count2(result2)

print("\nSolution:")
print(counter)
print("Correct Answer!")

print("\n=== Part 2 ===\n")

def increasing_with_dampener(lst):
    if increasing(lst):
        return True
    
    for i in range(len(lst)):
        new_lst = lst[:i] + lst[i+1:]
        if increasing(new_lst):
            return True

    return False

def decreasing_with_dampener(lst):
    if decreasing(lst):
        return True
    
    for i in range(len(lst)):
        new_lst = lst[:i] + lst[i+1:]
        if decreasing(new_lst):
            return True

    return False

def count3(arraylist):
    global counter2
    counter2 = 0
    for c in range(0, len(arraylist)):
        if (increasing_with_dampener(arraylist[c]) == True):
            counter2 += 1
        elif (decreasing_with_dampener(arraylist[c]) == True):
            counter2 += 1

count3(result1)

print("Test:")
print(counter2)

count3(result3)

print("\nTest 2:")
print(counter2)

count3(result2)

print("\nSolution:")
print(counter2)
print("Correct Answer!")

print("\nDay Finished!!!")

input()

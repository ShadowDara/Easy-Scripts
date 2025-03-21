print("Advent of Code 2024, Day 1!")
print("Shadowdara's Version:\n")

bsp_list1 = [3, 4, 2, 1, 3, 3]
bsp_list2 = [4, 3, 5, 3, 9, 3]

daten_string = """

"""

daten = [zeile.split() for zeile in daten_string.strip().split("\n")]

links = [int(paar[0]) for paar in daten]
rechts = [int(paar[1]) for paar in daten]

def bubblesort(list):
    size_count = len(list)
    for i in range(1, size_count):
        for j in range(0, size_count-i):
            if(list[j] > list[j+1]):
                tmp = list[j+1]
                list[j+1] = list[j]
                list[j] = tmp

def calculate(list1, list2):
    global tmp_cal
    lenght = len(list1)
    tmp = 0
    tmp_cal = 0
    for k in range(0,lenght):
        if list1[k] >= list2[k]:
            tmp = list1[k] - list2[k]
        else:
            tmp = list2[k] - list1[k]
        tmp_cal += tmp

print("=== Part 1 ===\n")

bubblesort(bsp_list1)
bubblesort(bsp_list2)

print(bsp_list1)
print(bsp_list2)

calculate(bsp_list1, bsp_list2)

print("Test:")
print(tmp_cal)

bubblesort(links)
bubblesort(rechts)

calculate(links, rechts)
print("\nSolution:")
print(tmp_cal)
print("Correct Answer!")

print("\n=== Part 2 ===\n")

def count(list1, list2):
    global count_v
    lenght = len(list1)
    count_v = 0
    for l in range(0, lenght):
        tmp_count = 0
        tmp = list1[l]
        for m in range(0, lenght):
            if list2[m] == tmp:
                tmp_count += 1
        count_v += (tmp * tmp_count)


count(bsp_list1, bsp_list2)

print("Test:")
print(count_v)

count(links, rechts)

print("\nSolution:")
print(count_v)
print("Correct Answer!")

print("\nDay Finished!!!")

input()

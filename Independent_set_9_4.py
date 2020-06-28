import math

print("Loading data from file ... ")

directory = "C:\\Users\\Nathan Hayes\\Desktop\\College\\Extracurriculars\\Research\\Wiseley\\partitions-3.txt"

raw_file = open(directory, "r")
data = []

for line in raw_file:
    stripped_line = [int(i) for i in line[1:-2].split(",")]
    stripped_line.sort()
    data.append(stripped_line)
raw_file.close()

print("Data loaded.")
print(str(len(data))+" lines.")

def col_count(x):
    vals = [0, 1, 1, 2, 2, 3, 3, "a", 4, 5, 5, 5, 6, 6, 7, 7, 7, 8, 8]
    if x <= 18:
        return vals[x]
    return math.ceil(x/3)

def col_count_2(x):
    return max(0, math.ceil((x-10)/3))

def get_large_ind_sets(line):
    ret = []
    for i in line:
        if i > 1:
            ret.append(col_count(i))
    return ret
            
cases_eliminated = 0
non_eliminated = []

for line in data:
    flag = True
    flag_2 = True
    total = 0
    total_2 = 0
    total_3 = 0
    for p in line:
        if p == 1:
            total += 1
            total_2 += 1
            total_3 += 1
        elif flag:
            flag = False
            total_3 += col_count(p)
            total_2 += col_count_2(p)
            total += col_count_2(p)
        elif flag_2:
            total += col_count(p)
            total_3 += col_count(p)
            total_2 += col_count_2(p)
            flag_2 = False 
        else:
            total += col_count(p)
            total_2 += col_count(p)
            total_3 += col_count(p)
    if total >= 53:
        cases_eliminated += 1
    elif total_2 >= 50:
        cases_eliminated += 1
    elif total_3 >= 56:
        cases_eliminated += 1
    else:
        non_eliminated.append(line)
        #print(total)
        #print(total_2)


print(cases_eliminated)

exit_file = open("out-3.txt", "w")

for line in non_eliminated:
    dressed_line = "{" + str(line)[1:-1] + "}\n"
    exit_file.write(dressed_line)
    dressed_col_count = "{" + str(sum([col_count(i) for i in line])) + "}\n"
    exit_file.write(dressed_col_count)
exit_file.close()

import math

print("Loading data from file ... ")

directory = "C:\\Users\\Nathan Hayes\\Desktop\\College\\Extracurriculars\\Research\\Wiseley\\partitions-1.txt"

raw_file = open(directory, "r")
data = []

for line in raw_file:
    stripped_line = [int(i) for i in line[1:-2].split(",")]
    data.append(stripped_line)
raw_file.close()

print("Data loaded.")
print(str(len(data))+" lines.")

def col_count(x):
    return math.ceil(x/3)

cases_eliminated = 0
non_eliminated = []

for line in data:
    flag = True
    flag_2 = True
    total = 0
    total_2 = 0
    for p in line:
        if p == 1:
            total += 1
            total_2 += 1
        elif flag:
            flag = False
        elif flag_2:
            total += col_count(p)
            flag_2 = False
        else:
            total += col_count(p)
            total_2 += col_count(p)
    if total >= 53:
        cases_eliminated += 1
    elif total_2 >= 50:
        cases_eliminated += 1
    else:
        non_eliminated.append(line)


print(cases_eliminated)

exit_file = open("out.txt", "w")

for line in non_eliminated:
    dressed_line = "{" + str(line)[1:-1] + "}\n"
    exit_file.write(dressed_line)
exit_file.close()

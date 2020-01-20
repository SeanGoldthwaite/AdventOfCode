import io
import json

program = open("intcode.txt", "r")
string = program.read()
list = string.split()
for i, num in enumerate(list):
    list[i] = int(list[i])
list[1] = 12
list[2] = 2
print(list)
i = 0
while (i < len(list)):
    print(i)
    print(list[i])
    print(list)
    if list[i] == 1:
        print("adding", list[list[i + 2]], list[list[i + 1]], "storing at", list[list[i + 3]])
        list[list[i + 3]] = list[list[i + 2]] + list[list[i + 1]]
        i += 4
        print("new i value", i)
    if list[i] == 2:
        print("multiplying", list[list[i + 2]], list[list[i + 1]], "storing at", list[list[i + 3]])
        list[list[i + 3]] = list[list[i + 2]] * list[list[i + 1]]
        i += 4
        print("new i value", i)
    if list[i] == 99:
        print("exiting")
        break

print(len(list))
print(list)
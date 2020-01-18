def main():
    passwords_part_one = []
    passwords_part_two = []
    # print("112233", check_password_two(112233))
    # print("123444", check_password_two(123444))
    # print("111122", check_password_two(111122))
    #print("255565", check_password_two(255565))
    for i in range(245318, 765747):
        # if check_password_one(i):
        #     passwords_part_one.append(i)
        if check_password_two(i):
            passwords_part_two.append(i)
        print(i)
    print(passwords_part_one)
    print(passwords_part_two)


def check_password_one(password):
    list = [int(x) for x in str(password)]
    repeat = False
    for i in range(1, len(list)):
        if list[i] < list[i - 1]:
            print("done 1")
            return False
        if list[i] is list[i - 1]:
            repeat = True
    print("done 1")
    return repeat

def check_password_two(password):
    list = [int(x) for x in str(password)]
    repeat = False
    repeats = []
    for i in range(1, len(list)):
        if list[i] < list[i - 1]:
            print("done 2")
            return False
        if list[i] is list[i - 1]:
            repeats.append(i - 1)
    #print(password)
    i = 0
    while i < len(repeats) - 1:
        print(repeats)
        #print(i)
        if repeats[i] is repeats[i + 1] - 1:
            j = i + 1
            while j < len(repeats) - 1:
                if repeats[j] is repeats[j + 1] - 1:
                    j += 1
            print("removing from ", i, j)
            del repeats[i:j + 1]
        i += 1
    #print(repeats)
    #print(len(repeats))
    print("done 2")
    return len(repeats) > 0

if __name__ == '__main__':
    main()
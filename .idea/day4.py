def main():
    passwords = 0
    # print("111111", checkPassword(111111))
    # print("223450", checkPassword(223450))
    # print("123789", checkPassword(123789))
    for i in range(245318, 765747):
        if checkPassword(i):
            passwords += 1
            print("Found Password: ", i)
        print(i, checkPassword(i))
    print(passwords)


def checkPassword(password):
    list = [int(x) for x in str(password)]
    repeat = False
    for i in range(1, len(list)):
        if list[i] < list[i - 1]:
            return False
        if list[i] is list[i - 1]:
            repeat = True
    return repeat

if __name__ == '__main__':
    main()
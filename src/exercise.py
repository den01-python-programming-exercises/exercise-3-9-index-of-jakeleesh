def main():
    #write your code below this line
    nums = []
    while True:
        num = int(input())
        if (num == -1):
            break
        else:
            nums.append(num)
    search = int(input("Search for?"))
    for i in range(len(nums)):
        if (nums[i] == search):
            print(str(search) + " is at index " + str(i))

if __name__ == '__main__':
    main()

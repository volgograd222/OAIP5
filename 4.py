def main():


nums = []
while True:
    num = int(input())
    if num == 0:
        break
    nums.append(num)
result = [num for num in nums if num % len(nums) == 0]
print(result)




if __name__ == "__main__":
    main()
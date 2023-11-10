def main():


n = int(input())
nums = set()
for i in range(n): 
    num = input()
    for j in num: nums.add(j)
print(len(nums))


if __name__ == "__main__":
    main()
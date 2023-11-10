def main():


num = int(input())
colors = [input() for i in range(num)]
all = int(input())
for i in range(all):
    print(colors[i % num])





if __name__ == "__main__":
    main()
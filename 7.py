def main():


dict = {}
while True:
    a = input()
    if a == "": break
    bird, count = a.split(": ")
    count = int(count)
    if bird in dict: dict[bird] += count
    else: dict[bird] = count
print(dict)



if __name__ == "__main__":
    main()
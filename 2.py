def main():


a = input()
b = input()
c = input()
a1 = set(a)
b1 = set(b)
c1 = set(c)
final = (a1 & b1) | (b1 & c1) | (a1 & c1)
#print(''.join(sorted(result_set)))
print(*final, sep='')


if __name__ == "__main__":
    main()
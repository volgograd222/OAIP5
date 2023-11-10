def main():


period_time = {
    'Archaea': 2800000,
    'Proterozoic': 635000,
    'Paleozoic': 300000,
    'Mesozoic': 145000,
    'Cenozoic': 0
}
while True:
    age = input()
    if age == '':
        break
    age = int(age)
    for period, period_age in period_time.items():
        if age > period_age:
            print(period)
            break






if __name__ == "__main__":
    main()
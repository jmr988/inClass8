lst = []
num = 5

for n in range(num) :
    numbers = int(input('Enter number between 0 and 10,000: '))
    while (numbers < 0 or numbers > 10000):
        print('Numbers must be between 0 and 10,0000')
        numbers = int(input('Enter number: '))
    lst.append(numbers)



print('Largest number is:', max(lst), 'Smallest number is:', min(lst))




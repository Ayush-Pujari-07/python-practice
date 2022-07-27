def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover

    return round(number_of_cans)


def check_prime(num):
    flag = False
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        return print(num, "is not a prime number")
    else:
        return print(num, "is a prime number")


text_h = int(input('Enter the Height of wall: '))
text_w = int(input('Enter the width of wall: '))
coverage = 5

Cans = paint_calc(height=text_h, width=text_w, cover=coverage)

print(f'No of can required for Painting is: {Cans}')

# n = int(input('Check This number: '))
check_prime(num=Cans)

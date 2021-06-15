def find_positive(num):
    sum_positive = 0
    for n in num:
        if n >= 0:
            sum_positive += n
    return sum_positive


def find_negative(num):
    sum_negative = 0
    for n in num:
        if n < 0:
            sum_negative += n
    return sum_negative


numbers = [int(num) for num in input().split()]
print(find_negative(numbers))
print(find_positive(numbers))
if abs(find_negative(numbers)) > abs(find_positive(numbers)):
    print("The negatives are stronger than the positives")
elif abs(find_negative(numbers)) < abs(find_positive(numbers)):
    print("The positives are stronger than the negatives")
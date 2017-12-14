
#
# Solution to Project Euler problem ID 20
# 
# @author tidmmar
#

def main():
    nums = 100
    sum_factorial = 0
    factorial = nums
    while nums != 1:
        nums -= 1
        factorial = factorial * nums
        print(factorial)
    for i in str(factorial):
        sum_factorial += int(i)
        print(i, sum_factorial)
    print()
    print('The sum of all the elements in the largest factorial is {}'.format(sum_factorial))
if __name__ == "__main__": main()
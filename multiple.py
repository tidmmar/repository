
#
# Solution to project Euler problem ID 1
#
# @author tidmmar
#

def main():
    nums = range(1,1000)
    case1 = 3
    case2 = 5
    sum = 0
    for i in nums:
        if i % case1 == 0:
            sum += i
            print(i, end = ' ')
        elif i % case2 == 0:
            sum += i
            print(i, end = ' ')
    print()
    print('The sum of all the elements is {}'.format(sum))
if __name__ == "__main__": main()
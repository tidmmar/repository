
#
# Solution to Project Euler problem ID 5
# personally I think this solution is easier to read but it isn't as quick as the fast solution...
# 
# @author tidmmar
#

def main():
    passfunc(20)
    


def passfunc(num):
    c = range(1, num+1)
    count = 20
    while True:
        for i in c:
            print(i, count)
            if count % i == 0:
                print('{} divisible by {}'.format(count, i))
                matched = True
            else:
                matched = False
                break
        if matched == True:
            print('found the smallest multiple {}'.format(count))
            break
        count = count + 20
        
    pass #command doesn't do anything but makes the function complete

if __name__ == "__main__": main()
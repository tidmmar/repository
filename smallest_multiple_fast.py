
#
# Solution to Project Euler problem ID 5
# personally I don't think this solution is very elegant but it sure is quick...
# 
# @author tidmmar
#

def main():
    passfunc(20)
    


def passfunc(num):
    c = range(1, num+1)
    count = 20
    while count % 2 != 0 or count % 3 != 0 or count % 4 != 0 or count % 5 != 0 or count % 6 != 0 or count % 7 != 0 or count % 8 != 0 or count % 9 != 0 or count % 10 != 0 or count % 11 != 0 or count % 12 != 0 or count % 13 != 0 or count % 14 != 0 or count % 15 != 0 or count % 16 != 0 or count % 17 != 0 or count % 18 != 0 or count % 19 != 0 or count % 20 != 0:
            count = count + 20
    print('found the smallest multiple {}'.format(count))       
        
    pass #command doesn't do anything but makes the function complete

if __name__ == "__main__": main()
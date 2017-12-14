
#
# Solution to project Euler problem ID 13
#
# @author tidmmar
#

def main():
    infile = open('large_sum.txt')
    summation = 0
    for i in infile: # read in each line of the file
        num = i.strip() # remove newlines
        big_num = int(num) # convert string to int
        summation += big_num # summation
        
    summation = str(sum)    # convert sum back to a string
    print('The sum of all of the numbers in large_sum.txt is {}'.format(sum[:10])) # print only the first 10 digits
        
if __name__ == "__main__": main()
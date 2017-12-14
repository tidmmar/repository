
#
# Solution to Euler problem ID 2
# Solution prints out even and odd numbered fibonacci numbers
# for reference
#
# Solution uses a class for generating the fibonacci numbers
#
# @author tidmmar

class fibonacci():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def series(self):
        while (True):
            self.a, self.b = self.b, self.a + self.b
            yield(self.b)
                        

def main():
    f = fibonacci(0,1)
    sum_even = 0
    for num in f.series():
        if num > 4000000: break
        if num % 2 == 0: 
            print('even number {}'.format(num))
            sum_even += num
        else: 
            print('odd number {}'.format(num))
            continue
    print('sum of even numbered series is {}'.format(sum_even))
if __name__ == "__main__": main()
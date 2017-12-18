
#
# Solution to Euler problem ID 25
# Solution prints out the index of the first
# 1000 digit fibonacci number
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
    f = fibonacci(1,0)
    fib_length = 1
    index = 0
    for num in f.series():
        if fib_length == 1000: break
        fib_length = (len(str(num)))
        index += 1
        print('index {}'.format(index))
    print('Index of the first 1000 digit fibonacci number is {}'.format(index))
if __name__ == "__main__": main()
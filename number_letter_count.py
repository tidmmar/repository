
#
# Solution to project Euler problem ID 17
# using a class to convert the number into words
#
# @author tidmmar

class num_to_words():
    """
        return a number as words,
        e.g., 115 becomes "one hundred and fifteen"
    """
    _words = {
        'ones': (
            'oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
        ), 'tens': (
            '', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
        ), 'teens': (
            'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' 
        ), 'range': {
            'hundred': 'hundred', 'and': 'and', 'thousand': 'thousand'
        }
    }
    _err = 'Error'    # error

    def __init__(self, n):
        self.__number = n;

    def num_to_words(self, num = None):
        "Return the number as a word"
        n = self.__number if num is None else num
        s = ''
        if n < 10:          # ones
            s += self._words['ones'][n]  
        elif n < 20:        # teens
            s += self._words['teens'][n - 10]
        elif n < 100:       # tens
            m = n % 10
            t = n // 10
            s += self._words['tens'][t]
            if m: s += '-' + num_to_words(m).num_to_words()    # remainder
        elif n < 1000:      # range
            m = n % 100
            t = n // 100
            if m == 0: s += self._words['ones'][t] + ' ' + self._words['range']['hundred'] # an exact multiple of 100, therefore doesn't need the 'and'
            else: s += self._words['ones'][t] + ' ' + self._words['range']['hundred'] + ' ' + self._words['range']['and']
            if m: s += ' ' + num_to_words(m).num_to_words()    # remainder
        elif n == 1000:
            t = n // 1000
            s += self._words['ones'][t] + ' ' + self._words['range']['thousand']
        else:
            s += self._err
        return s


def main():
    count = 0
    for i in range(1,1001):
        str_count = 0
        txt = num_to_words(i)
        print(txt.num_to_words())
        for x in txt.num_to_words():
            if x == '-': continue
            elif x == ' ': continue
            else: str_count += 1
            print(str_count, end = ' ')
        count += str_count
        print()
    print('The total number of characters is {}'.format(count))        

if __name__ == "__main__": main()
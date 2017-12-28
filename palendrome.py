class Palindrome:

    @staticmethod
    def is_palindrome(word):
        forward = []
        count = 0
        for i in word:
            forward.append(i.lower())
        print(forward)
        for c in reversed(word.lower()):
            if c == forward[count]:
                count += 1
            else:
                return False
        return True

print(Palindrome.is_palindrome('Deleveled'))
print(Palindrome.is_palindrome('Mark'))
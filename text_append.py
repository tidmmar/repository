#
# Append space separated items inputted by the user
# into a comma separated file.
# If file comma.txt exists items are appended otherwise a
# new file is created and items put into new file

# @author tidmmar

def main():
    pass
    colon_file = open('colon.txt', 'a')
    txt = input('Please enter the text to be appended to the file')
    words = txt.split()
    count = (len(words))
    print(count)
    #colon_file.write('\n')
    for word in words:
        pass
        if count == 1: 
            colon_file.write(word)
            colon_file.write('\n')
        else: 
            colon_file.write(word)
            colon_file.write(':')
        count -= 1
    colon_file.close()
    
    colon_file = open('colon.txt', 'r')
    for line in colon_file: 
        line = line.strip()
        print(line.split(':'))
    print('Done')
if __name__ == "__main__": main()
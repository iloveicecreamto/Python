# prgm with function to find the "largest" which accepts a filename as a parameters and reports the longest line in the file.


# 1st create a file Line.txt in the same folder
# then run this code 

def findLarge(f):
    long = ""
    count = 0
    for line in f:
        count += 1
        print('Line-',count)
        print(line)
        print('No : of characters =', len(line))
        if len(line) > len(long):
            long = line
    print('Longest Line:', long, 'with characters =', len(long))

f = open("Line.txt", "r")
findLarge(f)


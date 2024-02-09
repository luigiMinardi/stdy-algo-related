# Palindrome with recursion

def swap(s: str)-> str:
    if len(s) == 0:
        return s
    return swap(s[1:]) + s[0]

def main ():
    with open("./palindromes") as f:
        file = f.readlines()
        for line in file:
            line = line.strip("\n")
            if line == "":
                print (True, line)
            elif len(line) % 2 != 0:
                middle = len(line)//2
                start = line[:middle]
                end = line[middle+1:]
                #print(start.lower(), swap(end), start.lower() == swap(end))
                if start.lower() == swap(end):
                    print(True, line)
                else:
                    print(False, line)
            else:
                middle = len(line)//2
                start = line[:middle]
                end = line[middle:]
                #print(start.lower(), swap(end))
                if start.lower() == swap(end):
                    print(True, line)
                else:
                    print(False, line)

if __name__ == "__main__":
    main()

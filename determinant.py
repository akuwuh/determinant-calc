from colorama import init, Fore

bigArray = []
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

#prompting for size
print(Fore.MAGENTA + "[-] " + Fore.WHITE + "What size?")
n = int(input(Fore.CYAN + ""))

i = 0
j = 0
len = n*n

print(Fore.MAGENTA + "[-] " + Fore.WHITE + "Enter your entries")


#entry input
while i < n:
    entry = None
    #Prints row #
   # if (i)%n == 0:
    #    print("Row", ((i)/n) +1)
    print('Row', i + 1)
    j = 0 
    while j < n: 
        try:    
            entry = int((input(Fore.CYAN + "")))
            bigArray.append(entry)
            j += 1
        except ValueError:
            print("pls enter int")
    i += 1

len = n*n
lol = [None] * n
for i in range(n):
    lol[i] = bigArray[((i+1)*n) - n:(i+1)*n]


print("Your Matrix: \n")
for k in range(n):
    print(lol[k])
    print("\n")
    
def minor(array, i):

    m = [None] * (n -1)
    r = [None] * (n -1)

    for r in range(n):
        if r == 0:
            continue
        else:
            for c in range(n):
                if c == i:
                    continue

                r.append(array[r][c])
            m.append(r)
    
    return m

print("Minor: \n")
print(minor(lol, 0))





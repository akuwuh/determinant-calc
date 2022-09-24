from tkinter import N
from colorama import init, Fore

bigArray = []
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

#returns the determinant of matrix m using first row expansion
def minor(m, i, j):
    r_new = m[:i] + m[i+1:]
    m_new = [row[:j] + row[j+1:] for row in r_new] 
    return m_new

#returns the determinant of arr with size n
def det(arr, n): #arr is the matrix and n is the size
    if n == 1: return arr[0][0] #returns the number inside of the matrix
    if n == 2: return arr[0][0] * arr[1][1] - arr[1][0] * arr[0][1]
    total = 0
    if n > 2:
        for i in range(0,n):
            m = minor(arr, 0, i)
            total += ((pow(-1, i) * arr[0][i]) * det(m, n-1))
    return total


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

#sorting into list of list based on size n
for i in range(n):
    lol[i] = bigArray[((i+1)*n) - n:(i+1)*n]


print("Your Matrix: \n")

for k in range(n):
    print(lol[k])
    print("\n")

determinant = det(lol, n)

print("Determinant: \n")

print(determinant)


            



        




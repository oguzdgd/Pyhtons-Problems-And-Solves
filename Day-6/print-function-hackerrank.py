"""The included code stub Will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
123 ...n
Note that l'.. represents the consecutive values in between.
Example
12345.
Print the string
Input Format
The first line contains an integer n."""

if __name__ == '__main__':
    n = int(input())
a=''
for i in range(1,n+1):
        a=a+str(i)

print(a)

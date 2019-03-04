# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    n=int(input())
    for i in range(n):
        s=str(input())
        even=""
        odd=""
        for i in range(len(s)):
            if i%2==0:
                even=even+s[i]
            else:
                odd=odd+s[i]
        print(even,odd)

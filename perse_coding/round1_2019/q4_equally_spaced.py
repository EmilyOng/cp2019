a=int(input())
b=int(input())
c=int(input())
d=int(input())
diff=b-a
for i in range(4):
    if c-b==diff and d-c==diff:
        continue
    else:
        print("NO")
        exit(0)
print(diff)

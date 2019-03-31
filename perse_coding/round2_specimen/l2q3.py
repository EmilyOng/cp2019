a=int(input())
start=1
end=100
track=1
while start<=end:
    mid=(end+start)//2
    if mid>a:
        end=mid-1
    elif mid<a:
        start=mid+1
    else:
        print(track)
        exit(0)
    track+=1

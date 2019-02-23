n=int(input())
timings=[]
cmp=0
for i in range(0,n):
    name,time=input().split()
    timing=int(time[0])+float(time[2]+time[3])/60+float(time[5]+time[6]+time[7]+time[8])/3600
    timings.append(timing)
    if name=='Percy':
        cmp=timing
timings.sort()
for i in range(n):
    if timings[i]==cmp:
        print(i+1)
        break

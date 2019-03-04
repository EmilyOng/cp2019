#2 (Summing series) q2_sum_series2.py
#Write a recursive function sum_series2(i) to compute series:

def sum_series2(i):
    if i==1:
        return 1/3
    if i>0:
        return sum_series2(i-1)+(i/((2*i)+1))

print(sum_series2(20))

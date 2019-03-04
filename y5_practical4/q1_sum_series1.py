#1 (Summing series) q1_sum_series1.py
#Write a recursive function sum_series1(i) to compute the
# series
def sum_series1(i):
    if i==1:
        return 1

    if i>0:
        return sum_series1(i-1)+1/i

print(sum_series1(20))

#m(1)=0.5
#m(2)=m(1)+..

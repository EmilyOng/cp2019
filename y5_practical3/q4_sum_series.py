#4 (Summing series) q4_sum_series.py
#Write a function m_series(i) to compute the following series:

#m(i)=1/2 + 2/3 + ... + i/(i+1)
def m_series(i):
    sum_series=0
    for i in range(20):
        sum_series+=(i+1)/(i+2)
        print(i+1,"\t","{:.4f}".format(sum_series))
        
m_series(1)
#m(1)=0.5
#m(2)=m(1)+..
#m(3)=m(2)+...

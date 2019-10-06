# Enter your code here. Read input from STDIN. Print output to STDOUT
returned = list(map(str,input().split()))
returned = [int(x) for x in returned]

expected = list(map(str,input().split()))
expected = [int(x) for x in expected]

if returned[2] > expected[2]:
    print(10000)
else:
    if returned[2] < expected[2]:
        print(0)
    else:
        # ry == ey
        if returned[1] > expected[1]:
            print((returned[1]-expected[1])*500)
        else:
            if returned[1] < expected[1]:
                print(0)
            else:
                # rm == em
                if returned[0] > expected[0]:
                    print((returned[0]-expected[0])*15)
                else:
                    print(0)

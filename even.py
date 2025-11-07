import math
start = int(input("start:"))
end = int(input("end:"))
for num in range(start,end + 1):
    if 1000 <= num <= 9999:
        if all(int(d)%2 == 0 for d in str(num))and math.isqrt(num)**2 == num:
            print(num)

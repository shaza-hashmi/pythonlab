class B:
    def __init__(s,b): s.b=b
    def d(s,a): s.b+=a
    def w(s,a): s.b-=a
b=B(int(input("Balance: ")))
b.d(int(input("Deposit: ")))
b.w(int(input("Withdraw: ")))
print("Final:",b.b)


class Bank:
    def __init__(self,n,b): self.n=n; self.b=b
    def deposit(self,a): self.b+=a
    def withdraw(self,a): self.b-=a
n=input("Name: "); b=int(input("Balance: "))
x=Bank(n,b)
x.deposit(int(input("Deposit: ")))
x.withdraw(int(input("Withdraw: ")))
print("Final Balance:",x.b)


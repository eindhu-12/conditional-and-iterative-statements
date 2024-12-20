print(True and False)
print(2 and 3) #print  right operand
print(1 or 2)
print(-1 or 5)  #print  left operand
print(5 or -1)
print("indhu" > "bindhu")
print("helo" >="hleo")  # based on character ascii value

# -------------------------conditional statements------------------
# 1.if(condition)
# 2.elif(condition)
# 3.else
print()
print("if ,elif, else")
n=-1
if(n<0):
    print(n,"is a Negative Number")
elif(n>0):
    print(n,"is a Positive Number")
else:
    print("It is Zero")

# ---------------------------Iterative Statements-----------------
# 1.for
# 2.while
print()
print("for loop")
for i in range(0,21):
    if(i%2==0):
        print(i,"is a even Number")
    else:
        print(i,"is a odd Number")
print()
print("while loop")

x=0
while(x<20):
    print(x)
    x+=1
# -------------------------Jump Statements--------------------
# 1.continue
# 2.break
# 3.pass
print()
print("Jump Statements")
print()
print("break")

for k in range(10):
    if(k>4):
        print("loop breaks at 5")
        break
    else:
        print(k)

print()
print("continue")
for m in range(1,11):
    if(m%5==0):
        print(m)
        continue
# ------------------------Piramind------------------
c=4
for i in range(5):
    pattern=""
    for j in range(5):
        if(j>c):
            pattern+="*"+" "
        else:
            pattern+=" "
    c-=1
    print(pattern)

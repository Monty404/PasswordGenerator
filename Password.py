import random
import string
import time as tm

x = 0
deno = 1
special_ch = ['!','$','%','&','(',')']#special character list
maxCH = int(input("""How many charcters do you need for your password?
\nThis is how many charcters I need: """))

start = tm.time()

f_pass = open(file="password.txt",mode="w+")
for i in range(maxCH):
    NumChk = random.randint(0,2)
    if NumChk == 0:
        letter = random.choice(string.ascii_letters)#52 letters 
        f_pass.write(letter)
        deno *= 52
    elif NumChk == 1:
        num = str(random.randint(0,9))#9 numbers
        f_pass.write(num)
        deno *= 9
    else:
        spec_ch = random.choice(special_ch)#common special characters
        f_pass.write(spec_ch)
        deno *= 7

end = tm.time()
deltatm = end-start

print("The process took "+str(deltatm)+"seconds\n")

f_pass.close()
readPG = open(file="password.txt",mode="r+").read()

print("Your password is: "+str(readPG))
poss = (maxCH/deno)*100
print('\nThe possiblity of your password being cracked is: %.10f percent' %poss)

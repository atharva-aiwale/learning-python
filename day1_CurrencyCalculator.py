#Calculate currency remaining in US dollers
a = int(input('How much do you have left in pesos? :')) #input a 
b = int(input('How much do you have left in soles? :')) #input b
c = int(input('How much do you have left in reais? :')) #input c
d = int(a*0.058)  #conversion of pesos to us doller
e = int(b*0.29 )  #conversion of soles to us doller
f = int(c*0.20 )  #conversion of reais to us doller
g = d+e+f    #total currency remaining in us doller

print('What do you have left in pesos?'),print(d)
print('What do you have left in soles?'),print(e)
print('What do you have left in reais?'),print(f)
print(g)

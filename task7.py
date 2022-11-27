x=int(input())
y=int(input())
z=int(input())
def election(x,y,z):

   count = 0

   for i in x,y,z:

       if i == 1:

           count += 1

   if count > 1:

       return 1

   else:

       return 0

a = election(x,y,z)
print(a)
#print(a,"("+str(a)+","+str(a)+","+str(a)+")")
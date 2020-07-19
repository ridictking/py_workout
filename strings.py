
x = lambda x,q : x[x.find(q)-18 : x.find(q)+18] if q in x else -1


words = """
or the Sync   you need to have network , 
subscription type=new or oneoff, partnerID 
which we need to check if active or not, and for AsynC , 
susbription type = renewal  and we need to check if 
they have callback url that is working
"""

print(x(words,'check'))

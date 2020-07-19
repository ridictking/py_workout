




#print(x(words,'check'))

class WordUtils:
    def pig_latin(self,sentence):
        collect = list()
        for word in sentence.split():
            if word[0] in 'aeiou':
                word = f'{word}way'
            else:
                word = f'{word[1:]}{word[0:1]}ay'
            collect.append(word)
        print(' '.join(collect))

 

test = WordUtils()
test.pig_latin('This life is not an easy place to live in')

x = lambda x,q : x[x.find(q)-18 : x.find(q)+18] if q in x else -1

words = """
or the Sync   you need to have network , 
subscription type=new or oneoff, partnerID 
which we need to check if active or not, and for AsynC , 
susbription type = renewal  and we need to check if 
they have callback url that is working
"""
print(x(words, 'check'))


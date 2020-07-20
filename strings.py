




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
        return ' '.join(collect)

    def pig_latin_v2(self,sentence):
        anot =' '.join(list(map(lambda word : f'{word}way' if word[0] in 'aeiouAEIOU' else f'{word[1:]}{word[0:1]}ay',sentence.split())))
        return anot

    def reverse_pig_latin(self,sentence):
        # s = list();
        # for word in sentence.split():
        #     if word[0] in 'aeiou' and word.endswith('way'):
        #         word = word[0:2]
        #     else:
        #         new_word = word[0:word.find('ay')]
        #         word = new_word[-1:]+new_word[0:-1]
        #    return ' '.join(s)

        reverse =' '.join(list(map(lambda word : word[0:word.find('way')] if word[0] in 'aeiouAEIOU' and word.endswith('way') and word[0:word.find('way')] not in 'eE' else word[0:word.find('ay')][-1:]+word[0:word.find('ay')][0:-1], sentence.split())))
        return reverse
 

# test = WordUtils()
# #test.pig_latin('This life is not an easy place to live in')
# words = """
# or the Sync   you need to have network , 
# subscription type=new or oneoff, partnerID 
# which we need to check if active or not, and for AsynC , 
# susbription type = renewal  and we need to check if 
# they have callback url that is working
# """
# res = test.pig_latin_v2(words)
# print(res)
# print(test.reverse_pig_latin(res))


# x = lambda x,q : x[x.find(q)-18 : x.find(q)+18] if q in x else -1


#print(x(words, 'check'))


import string 
def test(word):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    new_word =''
    for ch in word:
        if(ch in lower):
            index = lower.index(ch)
            new_word =new_word +lower[(index+2)%26]
        elif(ch in upper):
            index =upper.index(ch)
            new_word = new_word + upper[(index+3)%26] 
        else:
            new_word = new_word + ch
    return new_word
print(test('The Joy Of Compunding'))
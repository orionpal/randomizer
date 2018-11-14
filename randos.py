import uniqls

def isOdd(n):
    if n==0:
        return False
    elif n%2==0:
        return False
    return True

def stoa(string): #does not account for punctuation
    array = []
    i = 0
    s = 0
    while i<len(string):
        if i==len(string)-1:
            array.append(string[s:i+1])
        elif string[i]==" ":
            array.append(string[s:i])
            s = i+1
        i = i + 1
    return array

def wtoa(word):
    array = []
    for c in word:
        array.append(c)
    return array
def atow(worda):
    w = ""
    for c in worda:
        w = w+c
    return w

def wrap(half, ulsn):
    if half==0:
        return 0
    elif ulsn<half:
        return ulsn
    else:
        return ulsn%half
    
def eword(wid, word):
    uls = uniqls.uniqls(wtoa(word))
    n = len(uls)/2
    inc = wrap(n, (len(word)+wid))
    pwrap = n + inc
    nwrap = n - inc
    
    
    if isOdd(len(word)):
        if isOdd(wid):
            return atow(uls[pwrap])
        else:
            return atow(uls[nwrap])
    elif isOdd(wid):
        return atow(uls[nwrap])
    return atow(uls[pwrap])

def encode(letter):
    encoded = ""
    key = []
    words = stoa(letter)
    nwords = len(words)
    for word in words:
        l = len(word)
        key.append(l)
    i = 0
    while i<nwords:
        if i%2==1:
            wid = i
            encoded = encoded+eword(wid, words[wid])
        else:
            wid = nwords-1-i
            encoded = encoded+eword(wid, words[wid])
        i = i + 1

    return (key, encoded)



def etoa(key, letter):
    return 0
    
def decode(key, letter):
    nwords = len(key)
    decoded = ""
    #first ordered
    wid = 0
    i = 1
    while i<nwords:
        decoded = decoded + eword(wid, "")
        i = i + 2
    #second ordered
    line = 0
    return 0


#  0    1   2    3
#This will be encoded
#key=4427
#length=4      v ids v
#arrangement = 3 0 2 1
#               encoded this be will
#               len(uniqls)/2 + eword(id, word)
# OR
# 0 1 2 3 4 5 6 7
# 3 2 1 0 7 6 5 4

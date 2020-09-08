# <<<<< Playfair Cipher >>>>>
#######
# Initialization
#######
import numpy as np
alph = """ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"""
matrix_size = 6                                                               # Matrix size
matrix = [[0 for i in range(matrix_size)] for j in range(matrix_size)]                 # Creating null matrix of given size
r,ki,c = 0,0,0                                                          # row,column and key index
aind = 0                                                                # alphabet index
def keyip():
    kls = []
    bolst = []
    yek = input('Please enter the key>>> ').upper()
    if len(yek)<matrix_size:
        print ('Please Enter the key length >= {}'.format(matrix_size))
        keyip()
    
    # Checking for character repitition in key
    
    def kichck():
        for i in yek:
            if i in kls:
                bolst.append(False)
            else:
                kls.append(i)
                bolst.append(True)
        return all(bolst)
    bol = kichck()
    if len(yek)>=matrix_size and bol==True:       
        return yek
    #elif len(yek)<matrix_size and bol == False:
    #    print ('Please Enter the key length >= {} and without character repetition'.format(matrix_size))
    #    keyip()
    elif bol == False:
        print ('Please Enter key without character repitition')
        keyip()
#######
# Matrix Generation
#######
key = keyip()
while r<matrix_size and ki<=len(key):
    while c<matrix_size:
        if ki>=len(key):
            filr,filc = r,c
            break
        matrix[r][c] = key[ki]
        c+=1
        ki+=1
    if ki>=len(key):
        filr,filc = r,c
        break
    c = 0
    r+=1
#print (matrix)
print (filr,filc)
while filr<matrix_size:
    while filc<matrix_size:
        if alph[aind] not in key:
            matrix[filr][filc] = alph[aind]
            filc+=1
            aind+=1
        else:
            aind+=1
    filc = 0
    filr+=1
    #print (matrix)
mat = np.array(matrix)                                                         # Flat to matrix
print (mat)
#######
# Encrypt
#######
pltxt = input('Enter PlainText>>> ').upper()                                    # Plain text
orgpltxt = pltxt
i1,i2 = 0,1
###
# Checking for two same letters in a pair
###
while i2<len(pltxt):
    if pltxt[i1] == pltxt[i2]:
        fils = list(pltxt)
        fils.insert(i2,'?')
        pltxt = ''.join(fils)
        print ('Plain Text after filler>>> ',pltxt)
    i1+=2
    i2+=2
cils = []                                                                       # List for cipher text
###
# Matrix Traverse to encrypt
###
def enc(pltxt):
    id1,id2=0,1
    while id2<len(pltxt):
        for sub1 in matrix:
            if pltxt[id1] in sub1:
                l1p1 = matrix.index(sub1)                                          # letter1 position1 i.e row number 
                l1p2 = sub1.index(pltxt[id1])                                   # letter1 position2 i.e column number
    #print (p1,p2)
        for sub2 in matrix:
            if pltxt[id2] in sub2:
                l2p1 = matrix.index(sub2)                                          # letter2 pos1 i.e row number
                l2p2 = sub2.index(pltxt[id2])                                   # letter2 pos2 i.e column number
        
        # Checking if both letters are in same row
        
        if l1p1 == l2p1:                                                        
            cip1 = (l1p2+1)%matrix_size
            cip2 = (l2p2+1)%matrix_size
            cils.append(matrix[l1p1][cip1])
            cils.append(matrix[l2p1][cip2])

        # Checking if both letters are in same column    

        if l1p2 == l2p2:
            cip1 = (l1p1+1)%matrix_size
            cip2 = (l2p1+1)%matrix_size
            cils.append(matrix[cip1][l1p2])
            cils.append(matrix[cip2][l2p2])
        
        # If not above cases
        
        elif pltxt[id1]!=pltxt[id2] and l1p1!=l2p1 and l1p2!=l2p2:
            cip1 = l2p2
            cip2 = l1p2
            cils.append(matrix[l1p1][cip1])
            cils.append(matrix[l2p1][cip2])
        id1 +=2
        id2 +=2
    print ('Cipher Text>>> ',''.join(cils))
#######
# Checking for length of plaintext
#######
if len(pltxt)%2==0:
    enc(pltxt)
else:
    apls = list(pltxt)
    apls.append('B')
    pltxt = ''.join(apls)
    enc(pltxt)

#######
# Decrypt
#######
pnls = []                                                                   # Plaintext list
citxt = ''.join(cils)
#print ('Cipher text>>> ',citxt)
cid1,cid2 = 0,1
while cid2<len(citxt):
    for csub1 in matrix:
        if citxt[cid1] in csub1:
            c1p1 = matrix.index(csub1)
            c1p2 = csub1.index(citxt[cid1])
    for csub2 in matrix:
        if citxt[cid2] in csub2:
            c2p1 = matrix.index(csub2)
            c2p2 = csub2.index(citxt[cid2])
    
    # Checking if both cipher letters belong to same row

    if c1p1 == c2p1:
        pip1 = (c1p2-1)
        pip2 = (c2p2-1)
        if pip1<0:                                                              # Checking if cipher is in any column of 1st row
            pip1 = matrix_size-1                                                      # making cipher to go to last row
        if pip2<0:
            pip2 = matrix_size-1
        pnls.append(matrix[c1p1][pip1])
        pnls.append(matrix[c2p1][pip2])
    if c1p2 == c2p2:
        pip1 = (c1p1-1)
        pip2 = (c2p1-1)
        if pip1<0:                                                              # Checking if cipher is any row of 1st column
            pip1 = matrix_size-1                                                      # making cipher to go to last column
        if pip2<0:
            pip2 = matrix_size-1
        pnls.append(matrix[pip1][c1p2])
        pnls.append(matrix[pip2][c2p2])
    elif citxt[cid1]!=citxt[cid2] and c1p1!=c2p1 and c1p2!=c2p2:
        pip1 = c2p2
        pip2 = c1p2
        pnls.append(matrix[c1p1][pip1])
        pnls.append(matrix[c2p1][pip2])
    cid1 +=2
    cid2 +=2
decpntxt = ''.join(pnls)                                                    # Decrypted Plain text
did1,did2 = 0,1
while did2<len(decpntxt):
    if did2+1>=len(decpntxt):
        break
    if decpntxt[did1]==decpntxt[did2+1] and decpntxt[did2]=='?':            # Checking for filler '?'
        firmls = list(decpntxt)
        firmls.pop(did2)
        decpntxt=''.join(firmls)
    did1+=2
    did2+=2
#print ('Plain Text after Decrypt>>> ',decpntxt)
#print ('Original Plain txt>>> ',orgpltxt)
if len(decpntxt)!=len(orgpltxt):
    lcrls = list(decpntxt)
    lcrls.pop()
    decpntxt = ''.join(lcrls)
print ('Plain Text after check>>> ',decpntxt)

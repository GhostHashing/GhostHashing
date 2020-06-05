from math import gcd
import random
import os
import hashlib
import string
import requests

#Created by zbbsoomerush#6024 on Discord

def Hash(stringh, salt, sharounds):
    if len(str(stringh)) == 0:
        return
    if len(str(salt)) == 1:
        return
    if len(str(sharounds)) == 0:
        return
    if stringh == "--(({{[[GC[RANDOMSTRING]]]}}))--":
        letters = string.ascii_letters + "1234567890"
        stringh = ""
        for i in range(50):
            chosenletter = random.choice(letters)
            stringh += chosenletter
    def phi(n):
        amount = 0
        try:
            for k in range(1, n + 1):
                if gcd(n, k) == 1:
                    amount += 1
        except:
            pass
        return str(amount)


    def binary(stringh):
        Result = ''.join(format(ord(i), 'b') for i in stringh)
        return str(Result)

    Output = ""
    Binary = ""
    SizeBinary = ""
    PHIBinary = ""
    Block = ""
    Cell1 = ""
    Cell2 = ""
    Cell3 = ""
    Cell4 = ""
    Cell5 = ""
    Cell6 = ""
    Cell7 = ""
    Cell8 = ""
    Cell9 = ""
    Cell10 = ""
    Cell11 = ""
    Cell12 = ""
    Cell13 = ""
    Cell14 = ""
    Cell15 = ""
    Cell16 = ""
    Cell17 = ""
    Cell18 = ""
    Cell19 = ""
    Cell20 = ""
    Cell21 = ""
    Cell22 = ""
    Cell23 = ""
    Cell24 = ""
    Cell25 = ""
    InitalHash1 = ""
    InitalHash2 = ""
    InitalHash3 = ""
    InitalHash4 = ""
    InitalHash5 = ""
    InitalHash6 = ""
    InitalHash7 = ""
    InitalHash8 = ""
    InitalHash9 = ""
    InitalHash10 = ""
    InitalHash11 = ""
    InitalHash12 = ""
    InitalHash13 = ""
    InitalHash14 = ""
    InitalHash15 = ""
    InitalHash16 = ""
    KConstant1 = ""
    KConstant2 = ""
    KConstant3 = ""
    KConstant4 = ""
    KConstant5 = ""
    KConstant6 = ""
    KConstant7 = ""
    KConstant8 = ""
    KConstant9 = ""
    CharacterHash1 = ""
    CharacterHash2 = ""
    CharacterHash3 = ""
    CharacterHash4 = ""
    CharacterHash5 = ""
    CharacterHash6 = ""
    CharacterHash7 = ""
    CharacterHash8 = ""
    CharacterHash9 = ""
    CharacterHash10 = ""
    CharacterHash11 = ""
    CharacterHash12 = ""
    CharacterHash13 = ""
    CharacterHash14 = ""
    CharacterHash15 = ""
    CharacterHash16 = ""
    for i in range(16):
        try:
            if i == 1:
                CharacterHash1 = hex(str(ord(stringh[i])))
            if i == 2:
                CharacterHash2 = hex(str(ord(stringh[i])))
            if i == 3:
                CharacterHash3 = hex(str(ord(stringh[i])))
            if i == 4:
                CharacterHash4 = hex(str(ord(stringh[i])))
            if i == 5:
                CharacterHash5 = hex(str(ord(stringh[i])))
            if i == 6:
                CharacterHash6 = hex(str(ord(stringh[i])))
            if i == 7:
                CharacterHash7 = hex(str(ord(stringh[i])))
            if i == 8:
                CharacterHash8 = hex(str(ord(stringh[i])))
            if i == 9:
                CharacterHash9 = hex(str(ord(stringh[i])))
            if i == 10:
                CharacterHash10 = hex(str(ord(stringh[i])))
            if i == 11:
                CharacterHash11 = hex(str(ord(stringh[i])))
            if i == 12:
                CharacterHash12 = hex(str(ord(stringh[i])))
            if i == 13:
                CharacterHash13 = hex(str(ord(stringh[i])))
            if i == 14:
                CharacterHash14 = hex(str(ord(stringh[i])))
            if i == 15:
                CharacterHash15 = hex(str(ord(stringh[i])))
            if i == 16:
                CharacterHash16 = hex(str(ord(stringh[i])))
        except: pass

    for i in range(len(stringh)):
        letter = binary(stringh[i])
        Binary += letter

    SizeBinary = str(len(Binary))
    for i in range(len(SizeBinary)):
        num = binary(str(phi(ord(SizeBinary[i]))))
        PHIBinary += str(num)
    Block = str(PHIBinary)

    for i in range(512-len(str(PHIBinary))):
        Block += "0"

    for i in range(25):
        Amount = i*36
        Extra = binary(phi(int(Block[128:136])))
        if i == 1:
            Cell1 = Block[:Amount]
            InitalHash1 = binary(str(hex(int(Cell1))))
        if i == 2:
            Cell2 = Block[:Amount]
            InitalHash2 = binary(str(hex(int(Cell2))))
        if i == 3:
            Cell3 = Block[:Amount]
            InitalHash3 = binary(str(hex(int(Cell3))))
        if i == 4:
            Cell4 = Block[:Amount]
            InitalHash4 = binary(str(hex(int(Cell4))))
        if i == 5:
            Cell5 = Block[:Amount]
            InitalHash5 = binary(str(hex(int(Cell5))))
        if i == 6:
            Cell6 = Block[:Amount]
            InitalHash6 = binary(str(hex(int(Cell6))))
        if i == 7:
            Cell7 = Block[:Amount]
            InitalHash7 = binary(str(hex(int(Cell7))))
        if i == 8:
            Cell8 = Block[:Amount]
            InitalHash8 = binary(str(hex(int(Cell8))))
        if i == 9:
            Cell9 = Block[:Amount]
            InitalHash9 = binary(str(hex(int(Cell9))))
        if i == 10:
            Cell10 = Block[:Amount]
            InitalHash10 = binary(str(hex(int(Cell10))))
        if i == 11:
            Cell11 = Block[:Amount]
            InitalHash11 = binary(str(hex(int(Cell11))))
        if i == 12:
            Cell12 = Block[:Amount]
            InitalHash12 = binary(str(hex(int(Cell12))))
        if i == 13:
            Cell13 = Block[:Amount]
            InitalHash13 = binary(str(hex(int(Cell13))))
        if i == 14:
            Cell14 = Block[:Amount]
            InitalHash14 = binary(str(hex(int(Cell14))))
        if i == 15:
            Cell15 = Block[:Amount]
            InitalHash15 = binary(str(hex(int(Cell15))))
        if i == 16:
            Cell16 = Extra[:Amount]
            Extra = Cell16
            InitalHash16 = binary(str(hex(int(Extra))))
        if i == 17:
            Cell17 = Extra[:Amount]
            Extra = Cell17
            KConstant1 = binary(str(hex(int(Extra))))
        if i == 18:
            Cell18 = Extra[:Amount]
            Extra = Cell18
            Extra = Extra[:8]
            KConstant2 = binary(str(hex(int(Extra))))
        if i == 19:
            Cell19 = Extra[:Amount]
            Extra = Cell19
            Extra = Extra[:8]
            KConstant3 = binary(str(hex(int(Extra))))
        if i == 20:
            Cell20 = Extra[:Amount]
            Extra = Cell20
            Extra = Extra[:8]
            KConstant4 = binary(str(hex(int(Extra))))
        if i == 21:
            Cell21 = Extra[:Amount]
            Extra = Cell21
            Extra = Extra[:8]
            KConstant5 = binary(str(hex(int(Extra))))
        if i == 22:
            Cell22 = binary(str(Extra[:Amount]))
            Extra = Cell22
            Extra = Extra[:4]
            KConstant6 = binary(str(hex(int(Extra))))
        if i == 23:
            Cell23 = binary(str(Extra[:Amount]))
            Extra = Cell23
            Extra = Extra[:8]
            KConstant7 = binary(str(hex(int(Extra))))
        if i == 24:
            Cell24 = binary(str(Extra[:Amount]))
            Extra = Cell24
            Extra = Extra[:8]
            KConstant8 = binary(str(hex(int(Extra))))
        if i == 25:
            Cell25 = binary(str(Extra[:Amount]))
            Extra = Cell25

    B1 = InitalHash1
    B2 = InitalHash2
    B3 = InitalHash3
    B4 = InitalHash4
    B5 = InitalHash5
    B6 = InitalHash6
    B7 = InitalHash7
    B8 = InitalHash8
    B9 = InitalHash9
    B10 = InitalHash10
    B11 = InitalHash11
    B12 = InitalHash12
    B13 = InitalHash13
    B14 = InitalHash14
    B15 = InitalHash15
    B16 = Cell1
    B17 = Cell2
    B18 = Cell3
    B19 = Cell4
    B20 = Cell5
    B21 = Cell6
    B22 = Cell7
    B23 = Cell8
    B24 = Cell9
    B25 = Cell10
    B26 = Cell11
    B27 = Cell12
    B28 = Cell13
    B29 = Cell14
    B30 = Cell15
    B31 = Cell16
    B32 = Cell17
    B33 = Cell18
    B34 = Cell19
    B35 = Cell20
    B36 = Cell21
    B37 = Cell22
    B38 = Cell23
    B39 = Cell24
    B40 = Cell25
    B41 = KConstant1
    B42 = KConstant2
    B43 = KConstant3
    B44 = KConstant4
    B45 = KConstant5
    B46 = KConstant6
    B47 = KConstant7
    B48 = KConstant8
    B49 = KConstant9
    B50 = InitalHash16
    B51 = binary(CharacterHash1)
    B52 = binary(CharacterHash2)
    B53 = binary(CharacterHash3)
    B54 = binary(CharacterHash4)
    B55 = binary(CharacterHash5)
    B56 = binary(CharacterHash6)
    B57 = binary(CharacterHash7)
    B58 = binary(CharacterHash8)
    B59 = binary(CharacterHash9)
    B60 = binary(CharacterHash10)
    B61 = binary(CharacterHash11)
    B62 = binary(CharacterHash12)
    B63 = binary(CharacterHash13)
    B64 = binary(CharacterHash14)
    B65 = binary(CharacterHash15)
    B66 = binary(CharacterHash16)

    InitalHashes = B1 + B2 + B3 + B4 + B5 + B6 + B7 + B8 + B9 + B10 + B11 + B12 + B13 + B14 + B15 + B50 + B51 + B52 + B53 + B54 + B55 + B56 + B57 + B58 + B59 + B60 + B61 + B62 + B63 + B64 + B65 + B66
    KConstants = B41 + B42 + B43 + B44 + B45 + B46 + B47 + B48 + B49
    All = binary(InitalHashes + KConstants)
    Number1 = int(len(All))
    Number1 = hex(int(Number1))
    Number = ""
    Final = ""
    FinalOutput = salt
    A1 = str(hex(int(binary(str(hex(int(All)))))))
    A2 = str(Number1)
    A3 = salt
    A4 = hex(int(binary(str(len(stringh)))))
    O1 = hex(int(binary(A1 + A2 + A3 + A4)[128:192]))
    O2 = O1 + hex(int(binary(str(ord(str(stringh)[len(str(stringh))-1:])))))
    O3 = O2[len(O2)-6:]
    O4 = O2[5] + O3[0] + O2[8] + O3[1] + O2[10] + O3[2] + O2[19] + O3[3] + O2[28] + O3[4] + O2[3] + O3[5]
    m = hashlib.sha256()
    m.update(O4.encode())
    O5 = m.hexdigest()
    for i in range(sharounds):
        m = hashlib.sha256()
        m.update(O5.encode())
        O5 = m.hexdigest()
    O6 = hex(int(binary(O5)))

    return O6[128:256] + A3

#GET PROGRAM HASH WTIH THIS CODE:
#import hashlib

#def ProgramHash(FileName):
#   m = hashlib.sha256()
#   file = open(FileName,'rb')
#   chunk = 0
#   while chunk != b'':
#       chunk = file.read(1024)
#       m.update(chunk)
#   return str(m.hexdigest())
#
#print(ProgramHash("GhostHashing.py"))
#VERIFY ITS HASH AT: https://pastebin.com/raw/NSjVCDQJ
#REPORT BUGS TO THIS EMAIL ADDRESS: ghosthashing@protonmail.com

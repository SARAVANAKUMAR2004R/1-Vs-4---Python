import random
import emoji
List=[1,2,3,4,5]
VarA,VarB,VarC,VarD,VarE,Varq="A","B","C","D","E",":"
seq=[]
KeyList=[]
key=[]
d={"A":5,"B":5,"C":5,"D":5,"E":5}
Fin=[]
f=0
c=1
indA,indB,indC,indD,indE=0,0,0,0,0
count=0
while f!=1:

    l=len(List)-1

    if c==0:
        seq=[ListA[0]]

    ListA,ListB,ListC,ListD,ListE=[],[],[],[],[]

    print("\n-------Entering a New Play-------")
    print("-------Fight-------\n")

    while l:
        if any(val==0 for val in d.values()):

            for i,j in d.items():

                if j==0 and i not in key:
                    key.extend(i)

            if key not in KeyList and key!=[]:
                KeyList.extend(key)
                KeyList=list(set(KeyList))

            if "A" in KeyList:
                print("You Lost ")
                f=1
                break

            elif len(KeyList)==len(List)-1 and "A" not in KeyList:
                print("You Won Congrats But No Reward ",emoji.emojize(":winking_face_with_tongue:"))
                f=1
                break
        if (count >=12 and d[VarA]==5) or (count>=18 and d[VarA]==4):
            print("Sorry Bro For Privacy Concerns We Take Your Life")
            d[VarA]-=1
            print(VarA," A Lost 1 Life\n")
        count+=1
        A=input("Enter The Number To Smash:")

        if not A.isdigit() or int(A)>5 or int(A)==0:
            print("\nEnter Number From 1 to 5")
            continue

        else:

            A=int(A)
        if A in seq:
            print("\nDon't Start With The Number That Was Already Followed By Previous Play")
        if A not in ListA and A not in seq:
            ListA.append(A)

            if c==1:
                Fin.append([VarA,Varq,A])

            else:
                Fin[indA]=[VarA,Varq,A]
                seq=[]

        else:
            print("Enter Different Number - Which Was Not already Entered\n")
            continue

        while 1:

            B=random.choice(List)
            if B not in ListB:
                ListB.append(B)

                if c==1:
                    Fin.append([VarB,Varq,B])
                    break

                else:
                    Fin[indB]=[VarB,Varq,B]
                    break
        while 1:

            C=random.choice(List)
            if C not in ListC:
                ListC.append(C)

                if c==1:
                    Fin.append([VarC,Varq,C])
                    break

                else:
                    Fin[indC]=[VarC,Varq,C]
                    break

        while 1:

            D=random.choice(List)
            if D not in ListD:
                ListD.append(D)

                if c==1:
                    Fin.append([VarD,Varq,D])
                    break

                else:
                    Fin[indD]=[VarD,Varq,D]
                    break

        while 1:

            E=random.choice(List)
            if E not in ListE:
                ListE.append(E)

                if c==1:
                    Fin.append([VarE,Varq,E])
                    break

                else:
                    Fin[indE]=[VarE,Varq,E]
                    break

        c=0
        out=sorted(Fin,key=lambda x:(x[2],Fin.index(x)))

        if 'B' in KeyList:
            out=[i for i in out if i[0]!=VarB]
            out.insert(0,[VarB,Varq,B])

        if 'C' in KeyList:
            out=[i for i in out if i[0]!=VarC]
            out.insert(0,[VarC,Varq,C])

        if 'D' in KeyList:
            out=[i for i in out if i[0]!=VarD]
            out.insert(0,[VarD,Varq,D])

        if 'E' in KeyList:
            out=[i for i in out if i[0]!=VarE]
            out.insert(0,[VarE,Varq,E])

        LastIndex= out.pop(-1)
        out.insert(0,LastIndex)
        print(out)
        var=LastIndex[0]

        d[var]-=1
        print(d)
        print(var," "+"Lost 1 Life...\n")
        for index,item in enumerate(out):
            if item[0] in VarA:
                indA=index
            elif item[0] in VarB:
                indB=index
            elif item[0] in VarC:
                indC=index
            elif item[0] in VarD:
                indD=index
            elif item[0] in VarE:
                indE=index

        l-=1

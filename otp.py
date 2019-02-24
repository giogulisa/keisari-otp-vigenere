import random
def func3():
    todo=input(("tu gsurt \n dashipvra sheyvanet 1 \n ganshipvra sheiyvanet 2 \n --> " ))
    print("tqven airchiet: "+ str(todo))
    
    if todo=="1":
        text=input("sheiyvane dasashipri teqsti: \n --> ")
        
        rangge=int(input("sheiyvanet random rangeis areali 0-dan 26-mde \n --> "))
        
        if rangge>=26:
            while rangge>26:
                print("tqven arasworad sheiyvanet !!! \n cadet xelaxla \n --> ")
                rangge=int(input("sheiyvanet random rangeis areali 0-dan 26-mde \n --> "))
                
        newtext=""
        newkey=[]
        lettersInString=0
        key=0
        n=0
        
        for i in text:
            if ord(i) >64 and ord(i)<91 or ord(i)>96 and ord(i)<123: 
                    lettersInString+=1
        
        for j in range(lettersInString):
            key=random.randint(0,rangge)
            newkey.append(key)
        
        for i in text:
            if ord(i) >64 and ord(i)<91 or ord(i)>96 and ord(i)<123:
                asci=ord(i)
                dist=asci+newkey[n]
                ##didi asoa
                if asci <91:
                    if dist>=91:
                        dist-=26
                        char=chr(dist)
                        newtext+=char
                    else:
                        char=chr(dist)
                        newtext+=char
                ##patara asoa
                if asci >96:
                    if dist>=123:
                        dist-=26
                        char=chr(dist)
                        newtext+=char
                    else:
                        char=chr(dist)
                        newtext+=char
                n+=1
            else:
                newtext+=i
        print("DAIMAXSOVRET K E Y !!! : \n --> ")
        print(newkey)
        print("dashipruli teqstia :  \n --> ")
        
        
    elif todo=="2":
        text=input("sheiyvanet gansashipri teqsti:  \n --> ")
        
        newtext=""

        lettersInString=0
        key=0
        n=0 
        
        for i in text:
            if ord(i) >64 and ord(i)<91 or ord(i)>96 and ord(i)<123: 
                    lettersInString+=1
        print("sheiyvanet key e.g: 1 2 15 13 11... ert xazze gamotovebit \n -->  ")            
        key = list(map(int, input().split()))
        
        for i in text:
            if ord(i) >64 and ord(i)<91 or ord(i)>96 and ord(i)<123:
                asci=ord(i)
                dist=asci-key[n]
                ##didi asoa
                if asci <91:
                    if dist<=64:
                        dist+=26
                        char=chr(dist)
                        newtext+=char
                    else:
                        char=chr(dist)
                        newtext+=char
                ##patara asoa
                if asci >96:
                    if dist<=96:
                        dist+=26
                        char=chr(dist)
                        newtext+=char
                    else:
                        char=chr(dist)
                        newtext+=char
                n+=1
            else:
                newtext+=i
        print("ganshipruli teqstia :  \n --> ")
    
    print(newtext)        
    
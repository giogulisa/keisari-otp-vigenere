def func2():
    todo=input(("tu gsurt \n dashipvra sheyvanet 1 \n ganshipvra sheiyvanet 2 \n --> " ))

    print("tqven airchiet: "+ str(todo))
    
    if todo=="1":
        text=input("sheiyvane dasashipri teqsti: \n --> ")
        key=input("gasagebi \n --> ")
        newtext=""
        newkey=[]
        keylen=len(key)
        
        lettersInString=0
        k=0
        m=0
        n=0
        
        for i in text:
            if ord(i) >64 and ord(i)<91 or ord(i)>96 and ord(i)<123: 
                    lettersInString+=1
        for j in range(lettersInString):
            ascii=ord(key[k])
            ##keys konkretuli asos ascii kodi
            if ascii<91:
                m=ascii-65
            else:
                m=ascii-97
            newkey.append(m)
            k+=1
            if k==keylen:
                k=0
                
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
        
        print("dashipruli teqstia :  \n --> ")
    if todo=="2":
        text=input("sheiyvanet gansashipri teqsti:  \n --> ")
        key=input("gasagebi \n --> ")
        newtext=""
        newkey=[]
        keylen=len(key)
        
        lettersInString=0
        k=0
        m=0
        n=0
        
        for i in text:
            if ord(i) >64 and ord(i)<91 or ord(i)>96 and ord(i)<123: 
                    lettersInString+=1
        for j in range(lettersInString):
            ascii=ord(key[k])
            ##keys konkretuli asos ascii kodi
            if ascii<91:
                m=ascii-65
            else:
                m=ascii-97
            newkey.append(m)
            k+=1
            if k==keylen:
                k=0
        for i in text:
            if ord(i) >64 and ord(i)<91 or ord(i)>96 and ord(i)<123:
                asci=ord(i)
                dist=asci-newkey[n]
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
    
                    
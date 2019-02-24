def func1():
    
    todo=input(("tu gsurt \n dashipvra sheyvanet 1 \n ganshipvra sheiyvanet 2 \n --> " ))

    print("tqven airchiet: "+ str(todo))
    
    if todo=="1":
        text=input("sheiyvane dasashipri teqsti: \n --> ")
        length=int(input("shipris biji \n --> "))
        
        if length > 26:
            while length>26:
                length -= 26
        
        newtext=""
        
        for i in text:
            if ord(i) >64 and ord(i)<91 or ord(i)>96 and ord(i)<123:
                asci=ord(i)
                dist=asci+length
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
            else:
                newtext+=i
        print("dashipruli teqstia :  \n --> ")
    
    elif todo=="2":
        text=input("sheiyvanet gansashipri teqsti:  \n --> ")
        length=int(input("shipris biji \n --> "))
        
        if length > 26:
            while length>26:
                length -= 26
        
        newtext=""
        
        for i in text:
            if ord(i) >64 and ord(i)<91 or ord(i)>96 and ord(i)<123:
                asci=ord(i)
                dist=asci-length
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
                    
            else:
                newtext+=i
        print("ganshipruli teqstia: \n --> ")
    print(newtext)
    
    
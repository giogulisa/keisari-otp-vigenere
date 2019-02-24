import keisari
import otp
import vigenere

##savaraudod BUG-ebi ar gamparvia arsad :D vimedovneb

shipri=input("sheiyvanet  shesabamisi cipri: \n 1.keisari \n 2.vijeneri \n 3.otp \n --> " )

print("tqven airchiet: "+shipri)

if shipri=="1":
    keisari.func1()
elif shipri=="3":
    otp.func3()
elif shipri=="2":
    vigenere.func2()
else:    
    print("tqven arasworad airchiet")
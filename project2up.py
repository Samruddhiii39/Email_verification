import qrcode
email=input("Enter Email =")  
k=0
j=0
d=0
if len(email)>=6:
    if email[0].isalpha:
        if ("@" in email) and (email.count("@")==1):
            if (email[-3]==".") ^ (email[-4]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i==i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i==i.isdigit():
                        continue
                    elif i=="_" or i=="@" or i==".":
                        continue 
                    else:
                        d=1       
                if k==1 or j==1 or d==1:
                    print('The email either has a upper case letter or a space') 
                else:
                    img=qrcode.make(email)
                    img.save("emil.png")              
            else:
                print('The extention not recognized')
        else:
            print('There is no @ or more than one @')
    else:
        print('The first letter of Email should always be alphabet')
else:
    print('The email is short')
 
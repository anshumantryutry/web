name=input("Enter name: ")
school=input("School: ")
classs=int(input("Enter class: "))
address=input("Enter add1: ")
address2=input("Enter add2: ")
city=input("Enter City: ")
Pincode=input("Enter Pin code: ")
Parentcontact=input("Enter contact num:")
Rollno=input("Enter rollno:")
section=input("Enter section")
idcard=f'''                         {school}  
             
           Student name:{name}              rollno:{Rollno}
           Class:{classs}                       section:{section}

           Address:
                            {address}
                            {address2}
           City: {city}                     pin code:{Pincode}
           parent/guardian contact num: {Parentcontact}'''
           
 
print(idcard)
                                              
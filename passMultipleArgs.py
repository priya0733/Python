'''def my_function(Name,Num):
    print("Hello from", Name +', ' + Num)
my_function("Priya", "7449")'''

'''def Adhar_info(Name,DOB,Adhar_no,Gender,Age):
    print("Hello from", Name +', ' + DOB +  ', ' + Adhar_no + ', ' + Gender + ', ' + Age)
    
Adhar_info("priya","7/3/2003","1234 5677 7890","female","21")'''

#def Superstore(product_id,product_name,product_price,product_category,product_expirydate):
    #print("From superstore: ", product_id +', ' +product_name + ', ' +product_price + ', ' + product_category + ', ' + product_expirydate )
#Superstore("2","dairymilk","100","chocolate","26/7/24")

'''def Adhar_info(name,dob,aadharno,address,gender):
   print("Its ", name+" DOB is ",dob+" adharno= ",aadharno+" of resident ",address+" gender= ",gender)
Adhar_info("Shriya Gurunath Palkar","06-03-2003","98765443","Kudal","Female")'''

# provide a default value to an argument by using the assignment operator (=).   
'''def MF(name, num = "53"):
    print("Hello from", name + ', ' + num) 

MF("priya")
MF("priya","45")'''

'''def MF(name, num):#tuple
    print("hello from %s , %s" % (name, num))
MF("priya","4519")'''

'''def MF(name, num):#dictionary
    print("hello from %(n)s , %(s)s " % {'n' : name, 's' : num})
MF("priya","4519")'''

'''#string formatting
def MF(name, num):
    print("hello from {n} ,{r}".format(n=name, r=num))
MF("priya","4519")'''

'''def student_info(name,roll_no,marks):
    print("the info is : {a}, {b}, {c}".format(a=name,b=roll_no,c=marks))
student_info("priya", "53", "90")'''



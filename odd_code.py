def add_student(record):
    sid=int(input("Enter the Student ID :"))
    name=input("Enter the name :")
    cls=int(input("Enter the class :"))
    L=list()
    print("Enter the grade of 5 subjects :")
    for i in range(5):
        gd=int(input("Enter :"))
        L.append(gd);
    record[sid]=[name,cls,L]
    print("RECORD SUCCESSFULLY ADDED")

def display(record):
    for i in record:
        print(record[i])

def update_grade(record):
    sid=int(input("Enter the sid of the student :"))
    n=int(input("Enter the number of subject you want to change the grade of :"))
    kys=record.keys()
    if(n>0 and n<=5 and sid in kys):
       gd=int(input("Enter the new grade :"))
       record[sid][2][n-1]=gd
       print("Record UPDATED ")
       display(record)
       return
    print("INVALID INPUTS!!")

def calc_average(record):
    sid=int(input("Enter the sid of the student :"))
    kys=record.keys()
    if(sid in kys):
        sum=0
        for i in range(5):
            sum=sum+record[sid][2][i]
        avg=sum//5
        print("AVERAGE IS :",avg)
        return
    print("INVALID INPUTS!!")

def generate_repo(record):
    cls=int(input("Enter the class :"))
    kys=record.keys()
    repo=dict()
    max=0
    for i in record:
        if (record[i][1] == cls):
            avg=calc_average(i)
            repo[avg]=sid
            if(avg>max):
                max=avg
            
    print("TOP PERFORMING STUDENT IS :",record[repo[max]])


record=dict()
while True:
    print(""" Enter 1 to add record
2 to update grade
3 to calculate average
4 to generate report
5 to exit""")
    ch=int(input("Enter CHOICE :"))
    if(ch==1):
        add_student(record)
        display(record)
    elif (ch==2):
        update_grade(record)
    elif (ch==3):
        calc_average(record)
    elif(ch==4):
        generate_repo(record)
    elif(ch==5):
        break
    else:
        print("INVALID INPUT!!!")
        continue

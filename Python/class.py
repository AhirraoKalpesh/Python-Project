# class student:
#     s_name='Rohit'#class variable
#     s_no=101
#     age=20
#     city='pune'

# obj =student()
# obj1 =student()
# obj2 =student()
# print(f"{student.s_no}\n{student.s_name}\n{student.age}\n{student.city}")

# class bank:
#     b_name="HDFC"
#     bal=2000
#     def deposite(self):
#         self.amt=int(input("enter deposite amount: "))
#         bank.bal+=self.amt
    
#     def withdraw(self):
#         self.amt = int(input("enter amount to withdraw: "))
#         bank.bal-=self.amt

#     def get_cus_info(self):
#         self.cust_id,self.cust_name,self.cust_acctype = input("enter values").split(" ") 

#     def show_info(self):
#         print(f"{self.cust_id}\n{self.cust_name}\n{self.cust_acctype}\n{bank.bal}")

# cust1 = bank()
# cust2 = bank()
# ans = 'y'
# print("\n1.deposite amount\n2.withdraw amount\n3.add customer\n4.show information")
# while ans=='y':
#     choice=(int(input("enter choice to perform operation")))
#     if(choice==1):
#         cust1.deposite()
#     elif choice == 2:
#         cust1.withdraw()
#     elif choice == 3:
#         cust1.get_cus_info()
#     elif choice == 4:
#         cust1.show_info()
#     else:
#         print("enter valid choice")
#     ans = input("enter y to continue")

class student:
    n = int(input("enter number of students"))
    l1={}
    g={}
    def add(self):
        for i in range(1,student.n+1):
            self.rollno,self.name,self.m1,self.m2,self.m3 = input("enter values ").split(" ")
            self.total = int(self.m1)+int(self.m2)+int(self.m3)
            self.per = (int(self.total)/300)*100
            student.g = dict({self.rollno:{"Name":self.name,"m1":self.m1,"m2":self.m2,"m3":self.m3,"total":self.total,"percentage":self.per}})
            student.l1.update(student.g)
    def dist(self):
        c,c1,c2,c3 = 0,0,0,0
        
        for i,j in student.l1.items():
            for k,m in j.items():
                if k == 'percentage':
                    if m >= 75:
                        c+=1
                    elif m>=60 and m<75:
                        c1+=1
                    elif m>=35 and m<60:
                        c2+=1
                    elif m<35:
                        c3+=1
                    else:
                        pass
        print("distinction = ",c)
        print("first class = ",c1)
        print("pass class = ",c2)
        print("fail = ",c3)

    
    def show(self):
        print("rollno\t\tname\t\tm1\t\tm2\t\tm3\t\ttotal\t\tper\t\t")
        # for i in student.l1.items():
        #     print(f"{self.rollno}\t\t{self.name}\t\t{self.m1}\t\t{self.m2}\t\t{self.m3}\t\t{self.total}\t\t{self.per}")
        
        # print(student.l1)
        for i,j in student.l1.items():
            print(i,"\t\t",end=" ")
            for k,m in j.items():
                print(m,"\t\t",end = " ")
            print()
        self.dist()
    # def dist(self):
    #     if self.per>75:
    #         print("distinction")
    
obj1 = student()
ans = 'y'
print("1.add\n2.show")

while ans == 'y':
    ch = int(input("enter choice "))
    if ch == 1:
        obj1.add()
    elif ch == 2:
        obj1.show()
        # obj1.dist()
    else:
        print("wrong choice")
    ans = input("enter y to continue")
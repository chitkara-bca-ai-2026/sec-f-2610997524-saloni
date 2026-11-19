print("============================================================")
print("      S C H O O L   R E S U L T   P R O C E S S I N G       ")
print("============================================================")
name=input("Enter Student Name           : ")
roll=int(input("Enter Roll Number            : "))
print("-------------------------------------------------------------")
total= 0
i=1
grade = " "
result = "Pass"
remark = " "
print("------------Enter Marks For 5 Subjects (0-100)--------------")
while i <=5:
    mark=int(input(f"Enter Marks For Subject {i} : "))
    total += mark
    if mark < 0 or mark > 100:
        print("Error! Marks Not Applicable.")
        break
    if mark < 40:
        result = "FAIL"
        grade = "F"
        remark = "Failed in One or More Subjects"
    i +=1

perc = (total/500)*100
if result == "Pass":
    if perc > 90 and perc<100:
        grade = "A+"
        remark = "Outstanding"
    elif perc > 80 and perc <89:
        grade = "A"
        remark = "Excellent"
    elif perc > 70 and perc <79:
        grade = "B"
        remark = "Very Good"
    elif perc > 60 and perc <69:
        grade = "C"
        remark = "Good"
    elif perc > 50 and perc <59:
        grade = "D"
        remark = "Satisfactory"
    elif perc > 40 and perc <49:
        grade = "E"
        remark = "Pass"
    else:
        result = "Fail"
        grade = "F"
        remark = "Fail"
print("============================================================")
print("         S T U D E N T   R E P O R T   C A R D              ")
print("============================================================")
print(f" Student Name           : {name}")
print(f" Roll Number            : {roll}")
print("-------------------------------------------------------------")
print(" ")
print(f" Total Marks           : {total}/ 500.0")
print(f" Percentage            : {perc:.2f}%")
print(f" Result                : {result}")
print(f" Grade                 : {grade}")
print(f" Remarks               : {remark}")
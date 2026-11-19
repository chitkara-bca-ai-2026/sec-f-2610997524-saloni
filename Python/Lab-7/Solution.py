print("===============================================")
print("          CALENDAR VERIFICATION SYSTEM         ")
print("===============================================")
year =int(input("Enter year: "))
status = " "
reason = " "
if year<=0:
    print("Error! Year must be greater than 0.")
    status = "NA"
else:
    if year % 100 == 0:
        if year % 400 == 0:
            status = "LEAP YEAR"
            reason = "Is A Century Year and Is Divisible By 400."
        else:
            status = "Century Year"
            reason = "Is Divisible By 100."
    elif year % 100 != 0:
        if year % 4 == 0:
            status = "LEAP YEAR"
            reason = "Its A Non-Century Year And Is Divisible by 4"
        else:
            status = "Common Year"
            reason = "It Is Not Divisible By 100"
print("===============================================")
if status == "LEAP YEAR":
    print(f"Year                : {year}")
    print(f"Status              : {status}")
    print("Days in Year        : 366 Days")
    print("Days in February    : 29 Days")
    print(f"Reason              : {reason}")
elif status == "Century Year":
    print(f"Year                : {year}")
    print(f"Status              : {status}")
    print("Days in Year        : 365 Days")
    print("Days in February    : 28 Days")
    print(f"Reason              : {reason}")
elif status == "Common Year":
    print(f"Year                : {year}")
    print(f"Status              : {status}")
    print("Days in Year        : 365 Days")
    print("Days in February    : 28 Days")
    print(f"Reason              : {reason}")
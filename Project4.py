import json
import datetime
expences=[]

def save_data(expences):
    with open("expence.json","w") as file:
        json.dump(expences,file,indent=4)

def load_data():
    try:
        with open("expence.json","r") as file:
            return json.load(file)
    except:
        return[]
def menu():
    print("=============================== Menu ========================================")
    print("1.Add Expense \n2.View Expences \n3.Show Total Expences \n4.Category Wise Expence \n5.Delete Expence \n6.Exit")

def add_expence():
    expences=load_data()
    date1=datetime.datetime.now()
    date=date1.strftime("%Y-%m-%d")
    amount=int(input("Enter your Amount="))
    raw_category=input("Enter Category(Food/Travel/Other)=").strip()
    description=input("Give Description=").strip()
    category=raw_category.title()
    expences.append({
        "Date":date,
        "Amount":amount,
        "Category":category,
        "Description":description
    })
    save_data(expences)
    print("---------------------------------------------------------------------------")
    print("Expence Added!")
    return expences

def view_expence():
    expences=load_data()
    print(f"{'Date':<15}{'Amount':<10}{'Category':<10}{'Description'}")
    print("-"*65)
    for expence in expences:
        print(f"{expence['Date']:<15}{expence['Amount']:<10}{expence['Category']:<10}{expence['Description']}")
def total_expence():
    total=0
    expences=load_data()
    for add1 in expences:
        add=add1["Amount"]
        total=total+add
    print("----------------------------------------------------------------------------")
    print("Total Expences=",total)
def category_expences():
    expences=load_data()
    print("Categories=\nFood\nTravel\nOther")
    catchoice=input("Choose Category=")
    category_choice=catchoice.title()
    
    if category_choice not in ["Food","Travel","Other"]:
        print("-----------------------------------------------------------------------")
        print("Invalid Category!")
        return
    found=False
    print("--------------------------------------------------------------------------")
    print(f"{category_choice} Expence=")
    for category1 in expences:
        if category1["Category"]==category_choice:
            category2=category1["Amount"]
            print(category2)
            found=True
    if not found:
        print("-------------------------------------------------------------------------")
        print("No expence in this category!")
def delete_expence():
    expences=load_data()
    for index, value in enumerate(expences):
        print(f"{index+1} Expence={value}")
    delete=int(input("Enter list Number You Want to Delete in Your Expences="))
    if delete>0 and delete<=len(expences):
        delete=delete-1
        expences.pop(delete)
        print("-------------------------------------------------------------------------")
        print("Expence Delete Successfully!")
    else:
        print("--------------------------------------------------------------------------")
        print("Invalid number")
    save_data(expences)
    return expences






print("=========================== Expence Tracker =================================")
while True:
    menu()
    choice1=input("Enter Your Choice=")
    choice=choice1.title()
    if choice=="Add Expence" or choice=="1":
        add_expence()
    elif choice=="View Expence" or choice=="2":
        view_expence()
    elif choice=="Show Total Expences" or choice=="3":
        total_expence()
    elif choice=="Category Wise Expences" or choice=="4":
        category_expences()
    elif choice=="Delete Expence" or choice=="5":
        delete_expence()
    elif choice=="Exit" or choice=="6":
        print("Thanks You \nVisit Again")
        break
    else:
        print("Invalid Input ! \nPlease Correct Your Spelling")
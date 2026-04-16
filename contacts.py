import json

try:
    with open("contacts.json","r") as f:
        contacts = json.load(f)
except:
    contacts = []
    
def add_contact(contacts):
    while True:
        cname=input("Enter name: ").strip()
        cphone=input("Enter number: ").strip()
        
        if not cname or not cphone:
            print("Name/Number cannot be empty. Try again?(y/n)\n")
            choice=input(":-")
            if choice != 'y':
                break
            else:
                continue
            
        if not cphone.isdigit():
            print("Phone must contain only numbers!")
            choice=input("Do you wish to try again?(y/n)\n:-")
            if choice!='y':
                break
            else:
                continue
            
        duplicate=False    
        for c in contacts:
            if c['phone']==cphone:
                print("Contact already exists!")
                duplicate=True
                break
            
        if not duplicate:
            
            contacts.append({'name':cname,'phone':cphone})
            
            with open("contacts.json","w") as f:
                json.dump(contacts,f)
            
            print("Contact Added!")
            break
            
        else:
            break

def view_contact(contacts):
    if not contacts:
        print("No Contacts!")
        return
        
    for i,c in enumerate(contacts,start=1):
        print(f"{i}. Name: {c['name']} -- Number: {c['phone']}")

def find_contact(contacts):
    if not contacts:
        print("No Contacts!")
        return
        
    while True:
        try:
            find=int(input("Find by:\n1.Name\n2.Number\n:-"))
        except ValueError:
            print("Wrong input. Try again?(y/n)")
            choice=input(":-")
            if choice!='y':
                break
            else:
                continue
            
        if find==1:
            fname=input("Enter name: ").strip()
            if not fname:
                print("Field cannot be empty!")
                choice=input("Try again?(y/n)\n:-")
                if choice!='y':
                    break
                else:
                    continue
            found = False
            for c in contacts:
                if fname.lower() in c['name'].lower():
                    print(f"Found: {c['name']} -- {c['phone']}")
                    found=True
                        
                    
            if not found:
                print("Cannot find contact!")
                choice=input("Try again?(y/n)\n:-")
                if choice!='y':
                    break
                else:
                    continue
            break
                    
            
        elif find==2:
            fphone=input("Enter number: ").strip()
            if not fphone:
                print("Field cannot be empty!")
                choice=input("Try agian?(y/n)\n:-")
                if choice!='y':
                    break
                else:
                    continue
                
            if not fphone.isdigit():
                print("Invalid number!")
                choice=input("Try again?(y/n):-\n")
                if choice!='y':
                    break
                else:
                    continue
                    
                
            found=False
            for c in contacts:
                if fphone in c['phone']:
                    print(f"Found: {c['name']} -- {c['phone']}")
                    found=True
                        
            if not found:
                print("Cannot find contact!")
                choice=input("Try again?(y/n)\n:-")
                if choice!='y':
                    break
                else:
                    continue
            break
            
        else:
            print("Wrong input")
            choice=input("Try again?(y/n)\n:-")
            if choice!='y':
                break
            else:
                continue

def delete_contact(contacts):
    if not contacts:
        print("No contacts")
        return
        
    while True:
        try:
            dchoice=int(input("Enter contact you want to delete:- "))
        except ValueError:
            print("Wrong input! Try again(y/n)")
            choice = input(":-")
            if choice!='y':
                break
            else:
                continue
            
        if(1<=dchoice<=len(contacts)):
            contacts.pop(dchoice-1)
                
            with open("contacts.json","w") as f:
                json.dump(contacts,f)
                
            print("Contact Deleted")
            break
            
        else:
            print("Contact not found.")
            choice=input("Try again?(y/n)\n:-")
            if choice!='y':
                break
            else:
                continue

def delete_all_contact(contacts):
    if not contacts:
        print("No contacts!")
        return
        
    choice=input("Are you sure?(y/n)")
    if choice!='y':
        return
    else:
        contacts.clear()
            
        with open("contacts.json","w") as f:
            json.dump(contacts,f)
            
        print("All contacts deleted!")
        return

def update_contact(contacts):
    while True:
        if not contacts:
            print("No contacts!")
            break
            
        for i,c in enumerate(contacts,start=1):
            print(f"{i}. {c['name']} -- {c['phone']}")
                
        try:
            choice=int(input("Enter contact you want to update:-"))
        except ValueError:
            print("Wrong input!")
            choice=input("Try again?(y/n)\n:-")
            if choice!='y':
                break
            else:
                continue
            
        if(1<=choice<=len(contacts)):
            contact = contacts[choice-1]
            print(f"EDITING CONTACT:\nName: {contact['name']} / Number: {contact['phone']}")
                
            editn=input("Type new name value. Press enter for no changes:- ").strip()
            editp=input("Type new number value. Press enter for no changes:- ").strip()
                
            if editn:
                contact['name'] = editn
                
            if editp and not editp.isdigit():
                print("Number should contain only digits!")
                choice=input("Try again?(y/n)\n:-")
                if choice!='y':
                    break
                else:
                    continue
                
            if editp:
                contact['phone'] = editp
                
            with open("contacts.json","w") as f:
                json.dump(contacts,f)
                
            print(f"Updated Contact:-\n{contact}")
            break
             
        else:
            print("Invalid choice")
            choice=input("Try again?(y/n)\n:-")
            if choice!='y':
                break
            else:
                continue

def sort_contact(contacts):
    while True:
        try:
            sortc=int(input("1.Sort by name\n2.Sort by number\n:-"))
        except ValueError:
            print("Wrong input!")
            choice=input("Try again?(y/n)\n:-")
            if choice!='y':
                break
            else:
                continue
            
        if sortc==1:
            sorted_contacts=sorted(contacts, key=lambda x: x['name'].lower())
        elif sortc==2:
            sorted_contacts=sorted(contacts, key=lambda x: x['phone'])
            
        else:
            print("Invalid choice")
            choice=input("Try again?(y/n)\n:-")
            if choice!='y':
                break
            else:
                continue
            
        print("\n--SORTED CONTACTS--\n")
        for i,c in enumerate(sorted_contacts,start=1):
            print(f"{i}. {c['name']} / {c['phone']}")
                
        break


while True: #MENU
    try:
        menu=int(input("Welcome to Contacts! Choose one option:\n1.Add Contact\n2.View Contacts\n3.Find Contact\n4.Delete Contact\n5.Delete All Contacts\n6.Update Contact\n7.Sort Contacts\n8.Exit\n:-"))
    except ValueError:
        print("wrong input try again!")
        continue
    
    if menu==1: #ADD CONTACT
        add_contact(contacts)
            
    elif menu==2: #VIEW CONTACTS
        view_contact(contacts)
            
    elif menu==3: #FIND CONTACT
        find_contact(contacts)
    
    elif menu==4: #DELETE CONTACT
        delete_contact(contacts)
    
    elif menu==5: #DELETE ALL CONTACTS
        delete_all_contact(contacts)
        
    
    elif menu==6: #UPDATE CONTACT
        update_contact(contacts)
    
    elif menu==7: #SORT CONTACTS
        sort_contact(contacts)
        
    elif menu==8: #EXIT
        print("Goodbye!")
        break


from application import Application
from storage import load_data, save_data
from datetime import datetime

def view_applications():
    data = load_data()
    if not data:
        print("\nNo applications found!")
        return
    print("\n===== Your Applications =====")
    for index, application in enumerate(data, start=1):
        print(f"\nApplication #{index}")
        print(f"Company : {application['company']}")
        print(f"Position : {application['position']}")
        print(f"Location : {application['location']}")
        print(f"Date : {application['date']}")
        print(f"Status: {application['status']}")

def update_status():
    data = load_data()
    if not data:
        print("\nNo applications found!")
        return
    for index, application in enumerate(data, start=1):
        print(f"{index}. {application['company']} - {application['position']} - {application['status']}")
    choice = int(input("\nEnter application number: "))
    application = data[choice - 1]
    statuses = {
        "1" : "Applied",
        "2" : "Interview",
        "3" : "Rejected",
        "4" : "Accepted"
    }
    print("\nChoose new status:")
    print("1. Applied")
    print("2. Interview")
    print("3. Rejected")
    print("4. Accepted")

    status_choice = input("Choice: ")

    if status_choice in statuses:
        application["status"] = statuses[status_choice]
        save_data(data)
        print("\nStatus updated successfully!")
    else:
        print("\nInvalid status.")

def menu():
    print("\n==============================")
    print(" Job Application Tracker")
    print("==============================")
    print("1. Add Application")
    print("2. View Applications")
    print("3. Search Company")
    print("4. Update Status")
    print("5. Delete Application")
    print("6. Statistics")
    print("7. Exit")

def search_company():
    data = load_data()
    company_name = input("\nEnter company name: ").strip()
    found = False
    for application in data:
        if application['company'].lower() == company_name.lower():
            print("\nApplication found!")
            print(f"Company : {application['company']}")
            print(f"Position : {application['position']}")
            print(f"Location : {application['location']}")
            print(f"Date : {application['date']}")
            print(f"Status: {application['status']}")
            found = True
    if not found:
        print("\nNo applications found!")

while True:
    menu()
    choice = input("\nChoose an option: ")

    if choice == "1":
        company = input("Company: ")
        position = input("Position: ")
        location = input("Location: ")
        today = datetime.today().strftime("%d-%m-%Y")
        application = Application(
            company,
            position,
            location,
            today,
    'Applied'
        )

        data = load_data()
        data.append(application.to_dict())
        save_data(data)
        print("\nApplication saved!")

    elif choice == "2":
        view_applications()

    elif choice == "3":
        search_company()

    elif choice == "4":
        update_status()

    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Feature coming soon...")
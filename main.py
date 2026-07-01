
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

    # Show all applications
    for index, application in enumerate(data, start=1):
        print(f"{index}. {application['company']} - {application['position']} - {application['status']}")

    try:
        choice = int(input("\nEnter application number: "))

        if 1 <= choice <= len(data):
            application = data[choice - 1]

            statuses = {
                "1": "Applied",
                "2": "Interview",
                "3": "Rejected",
                "4": "Accepted"
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

        else:
            print("\nInvalid application number.")

    except ValueError:
        print("\nInvalid input. You can only enter numbers.")
        return

def delete_application():
    data = load_data()

    if not data:
        print("\nNo applications found!")
        return

    for index, application in enumerate(data, start=1):
        print(f"{index}. {application['company']} - {application['position']} - {application['status']}")
    try:
        choice = int(input("Enter application number: "))
        if 1 <= choice <= len(data):
            application = data[choice - 1]

            confirm = input(
            f"Are you sure you want to delete '{application['company']}'? (y/n): "
        ).lower()

            if confirm == "y":
                del data[choice - 1]
                save_data(data)
                print("\nApplication deleted successfully!")
            else:
                print("\nDeletion cancelled.")
        else:
            print("\nInvalid application number.")
    except ValueError:
            print("\nInvalid input. You can only enter numbers.")
            return

def statistics():
    data = load_data()

    applied = 0
    interview = 0
    accepted = 0
    rejected = 0

    if not data:
        print("\nNo applications found!")
        return

    total = len(data)

    for application in data:
        if application["status"] == "Applied":
            applied += 1
        elif application["status"] == "Interview":
            interview += 1
        elif application["status"] == "Rejected":
            rejected += 1
        elif application["status"] == "Accepted":
            accepted += 1
    print(f" ======== Statistics ======= \n")
    print(f"Total applications: {total}")
    print(f"Applied: {applied}")
    print(f"Interview: {interview}")
    print(f"Accepted: {accepted}")
    print(f"Rejected: {rejected}")

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

    elif choice == "5":
        delete_application()
    elif choice == "6":
        statistics()

    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Feature coming soon...")
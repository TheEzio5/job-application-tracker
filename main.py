
from application import Application
from storage import load_data, save_data
from datetime import datetime

def view_applications():
    data = load_data()
    if not data:
        print("\nNo applications found!")
        return
    print("\n===== Your Applications =====")
    for index, application in enumerate(data,start=1):
        print(f"\nApplication #{index}")
        print(f"Company : {application['company']}")
        print(f"Position : {application['position']}")
        print(f"Location : {application['location']}")
        print(f"Date : {application['date']}")
        print(f"Status: {application['status']}")



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
    'Applied')

        data = load_data()
        data.append(application.to_dict())
        save_data(data)
        print("\nApplication saved!")

    elif choice == "2":
        view_applications()

    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Feature coming soon...")
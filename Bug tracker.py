import json
import os

BUGS_FILE = 'bugs.json'

def load_bugs():
    if os.path.exists(BUGS_FILE):
        with open(BUGS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_bugs(bugs):
    with open(BUGS_FILE, 'w') as file:
        json.dump(bugs, file, indent=4)

def add_bug(bugs):
    title = input("Enter bug title: ")
    description = input("Enter bug description: ")
    status = "Open"
    bug_id = len(bugs) + 1
    bugs.append({"id": bug_id, "title": title, "description": description, "status": status})
    save_bugs(bugs)
    print(f"Bug #{bug_id} added.")

def view_bugs(bugs):
    if not bugs:
        print("No bugs found.")
        return
    for bug in bugs:
        print(f"ID: {bug['id']}, Title: {bug['title']}, Status: {bug['status']}\nDescription: {bug['description']}")

def edit_bug(bugs):
    view_bugs(bugs)
    bug_id = int(input("Enter the bug ID to edit: "))
    for bug in bugs:
        if bug['id'] == bug_id:
            title = input("Enter new title (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            if title:
                bug['title'] = title
            if description:
                bug['description'] = description
            save_bugs(bugs)
            print(f"Bug #{bug_id} updated.")
            return
    print("Bug ID not found.")

def change_status(bugs):
    view_bugs(bugs)
    bug_id = int(input("Enter the bug ID to change status: "))
    for bug in bugs:
        if bug['id'] == bug_id:
            new_status = input("Enter new status (Open, In Progress, Resolved, Closed): ")
            bug['status'] = new_status
            save_bugs(bugs)
            print(f"Bug #{bug_id} status changed to '{new_status}'.")
            return
    print("Bug ID not found.")

def delete_bug(bugs):
    view_bugs(bugs)
    bug_id = int(input("Enter the bug ID to delete: "))
    for i, bug in enumerate(bugs):
        if bug['id'] == bug_id:
            bugs.pop(i)
            save_bugs(bugs)
            print(f"Bug #{bug_id} deleted.")
            return
    print("Bug ID not found.")

def main():
    bugs = load_bugs()

    while True:
        print("\nBug Tracker Menu")
        print("1. Add Bug")
        print("2. View Bugs")
        print("3. Edit Bug")
        print("4. Change Bug Status")
        print("5. Delete Bug")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_bug(bugs)
        elif choice == '2':
            view_bugs(bugs)
        elif choice == '3':
            edit_bug(bugs)
        elif choice == '4':
            change_status(bugs)
        elif choice == '5':
            delete_bug(bugs)
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

if __name__== "__main__":
    main()
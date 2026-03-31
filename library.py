import csv
import os
filename = "library.csv"
if not os.path.exists(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["BookID", "Title", "Author", "Status"])
def line():
    print("-" * 50)
def display_books():
    with open(filename, 'r') as file:
        reader = list(csv.reader(file))
        if len(reader) <= 1:
            print("\nNo books available.\n")
            return
        line()
        print(f"{'ID':<10}{'Title':<15}{'Author':<15}{'Status':<10}")
        line()
        for row in reader[1:]:
            print(f"{row[0]:<10}{row[1]:<15}{row[2]:<15}{row[3]:<10}")
        line()
def book_exists(book_id):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == book_id:
                return True
    return False
def add_book():
    print("\n📘 Add New Book")
    book_id = input("Enter Book ID: ")
    if book_exists(book_id):
        print("❌ Book ID already exists!\n")
        return
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([book_id, title, author, "Available"])
    print("✅ Book added successfully!\n")
def search_book():
    book_id = input("\nEnter Book ID to search: ")
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == book_id:
                print("\n🔍 Book Found!")
                print(f"ID     : {row[0]}")
                print(f"Title  : {row[1]}")
                print(f"Author : {row[2]}")
                print(f"Status : {row[3]}\n")
                return
    print("❌ Book not found.\n")
def issue_book():
    book_id = input("\nEnter Book ID to issue: ")
    rows = []
    updated = False
    with open(filename, 'r') as file:
        rows = list(csv.reader(file))
    for row in rows:
        if row[0] == book_id:
            if row[3] == "Available":
                row[3] = "Issued"
                updated = True
            else:
                print("⚠️ Book already issued!\n")
                return
    if updated:
        with open(filename, 'w', newline='') as file:
            csv.writer(file).writerows(rows)
        print("✅ Book issued successfully!\n")
    else:
        print("❌ Book not found.\n")
def return_book():
    book_id = input("\nEnter Book ID to return: ")
    rows = []
    updated = False

    with open(filename, 'r') as file:
        rows = list(csv.reader(file))

    for row in rows:
        if row[0] == book_id:
            if row[3] == "Issued":
                row[3] = "Available"
                updated = True
            else:
                print("⚠️ Book already available!\n")
                return
    if updated:
        with open(filename, 'w', newline='') as file:
            csv.writer(file).writerows(rows)
        print("✅ Book returned successfully!\n")
    else:
        print("❌ Book not found.\n")
def delete_book():
    book_id = input("\nEnter Book ID to delete: ")
    
    with open(filename, 'r') as file:
        rows = list(csv.reader(file))

    new_rows = [row for row in rows if row[0] != book_id]

    if len(rows) == len(new_rows):
        print("❌ Book ID not found.\n")
    else:
        with open(filename, 'w', newline='') as file:
            csv.writer(file).writerows(new_rows)
        print("🗑️ Book deleted successfully!\n")
while True:
    print("\n📚 LIBRARY MANAGEMENT SYSTEM")
    line()
    print("1️⃣  Add Book")
    print("2️⃣  View Books")
    print("3️⃣  Search Book")
    print("4️⃣  Issue Book")
    print("5️⃣  Return Book")
    print("6️⃣  Delete Book")
    print("7️⃣  Exit")
    line()

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        delete_book()
    elif choice == "7":
        print("\n👋 Thank you! Exiting...")
        break
    else:
        print("❌ Invalid choice. Try again.\n")

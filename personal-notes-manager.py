
print("===== Personal Notes Manager =====")

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Search Notes")
    print("4. Delete All Notes")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        note = input("Enter your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note saved successfully!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                notes = file.read()

                if notes.strip():
                    print("\n===== Your Notes =====")
                    print(notes)
                else:
                    print("Your notes are empty!")

        except FileNotFoundError:
            print("No notes found!")

    elif choice == "3":
        keyword = input("Enter a word to search: ").lower()

        try:
            with open("notes.txt", "r") as file:
                found = False

                for note in file:
                    if keyword in note.lower():
                        print(note.strip())
                        found = True

                if not found:
                    print("No matching notes found!")

        except FileNotFoundError:
            print("No notes found!")

    elif choice == "4":
        confirm = input("Delete all notes? (yes/no): ")

        if confirm.lower() == "yes":
            with open("notes.txt", "w") as file:
                pass

            print("All notes deleted!")
        else:
            print("Deletion cancelled.")

    elif choice == "5":
        print("Thank you for using Personal Notes Manager!")
        break

    else:
        print("Invalid choice! Please try again.")

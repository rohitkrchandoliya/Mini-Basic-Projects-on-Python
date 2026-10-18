
print("............Student's Marks Management Sheet...............")

fees = 15000
subjects = ["Hindi", "English", "Math", "Computer", "Science"]

students = {
    "Rishabh": [[33, 89, 93, 75, 67], 8000, 67],
    "Pawan": [[90, 67, 88, 32, 94], 6000, 78],
    "Priya": [[87, 64, 98, 78, 34], 9000, 89],
    "Akash": [[90, 78, 76, 56, 45], 12000, 93],
    "Shravan": [[90, 88, 86, 30, 95], 10000, 85],
}

s_name = input("Enter your name: ").strip()

if s_name not in students:
    print("\nOops! No matching student found:", s_name)
else:
    print("\nYes! Student found in sheet.")
    print("Student Name:", s_name)

    marks = students[s_name][0]
    paid_fee = students[s_name][1]
    attendance = students[s_name][2]

    while True:
        print("\n----- Student Management Menu -----")
        print("1. Marks, Percentage, Grade and Result")
        print("2. Paid Fee, Add Fee and Remaining Fee")
        print("3. Attendance")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
        except ValueError:
            print("Invalid input! Please enter a number from 1 to 4.")
            continue

        if choice == 1:
            while True:
                print("\n----- Academic Record -----")
                print("i. View Marks")
                print("ii. View Percentage")
                print("iii. View Grade")
                print("iv. View Overall Result")
                print("v. Back to Main Menu")

                ch = input("Enter your choice (i/ii/iii/iv/v): ").strip().lower()

                total = sum(marks)
                percentage = total / len(subjects)

                if ch == "i":
                    print("\nSubject-wise Marks:")
                    for subject, mark in zip(subjects, marks):
                        print(f"{subject}: {mark}")

                elif ch == "ii":
                    print(f"\nYour Percentage: {percentage:.2f}%")

                elif ch == "iii":
                    if percentage >= 90:
                        grade = "A"
                    elif percentage >= 80:
                        grade = "B"
                    elif percentage >= 70:
                        grade = "C"
                    elif percentage >= 60:
                        grade = "D"
                    elif percentage >= 50:
                        grade = "E"
                    else:
                        grade = "Below E"

                    print(f"\nYour Grade: {grade}")

                elif ch == "iv":
                    failed_subjects = [
                        subjects[i]
                        for i, mark in enumerate(marks)
                        if mark < 33
                    ]

                    if failed_subjects:
                        print("\nOverall Result: FAIL")
                        print("Subjects below passing marks:",
                              ", ".join(failed_subjects))
                    else:
                        print("\nOverall Result: PASS")

                elif ch == "v":
                    break

                else:
                    print("Wrong choice! Please select i, ii, iii, iv or v.")

        elif choice == 2:
            while True:
                print("\n----- Fee Management -----")
                print("a. View Paid Fee")
                print("b. View Remaining Fee")
                print("c. Add Fee Payment")
                print("d. Back to Main Menu")

                ch = input("Enter your choice (a/b/c/d): ").strip().lower()

                if ch == "a":
                    print("\nYour Paid Fee:", paid_fee)

                elif ch == "b":
                    remaining_fee = max(0, fees - paid_fee)
                    print("\nYour Remaining Fee:", remaining_fee)

                    if paid_fee > fees:
                        print("Extra Fee Paid:", paid_fee - fees)

                elif ch == "c":
                    try:
                        amount = int(input("Enter fee amount to add: "))
                    except ValueError:
                        print("Invalid amount! Enter a whole number.")
                        continue

                    if amount <= 0:
                        print("Fee amount must be greater than zero.")
                        continue

                    paid_fee += amount
                    students[s_name][1] = paid_fee

                    print("\nSuccessfully Paid:", amount)
                    print("Updated Paid Fee:", paid_fee)
                    print("Remaining Fee:", max(0, fees - paid_fee))

                elif ch == "d":
                    break

                else:
                    print("Wrong choice! Please select a, b, c or d.")

        elif choice == 3:
            print("\nYour Attendance:", attendance, "%")

            if attendance >= 80:
                print("Attendance Level: High")
            elif attendance >= 70:
                print("Attendance Level: Medium")
            else:
                print("Attendance Level: Low")

        elif choice == 4:
            print("\nYou have exited the Student Management Sheet.")
            break

        else:
            print("Wrong choice! Please select an option from 1 to 4.")

import tkinter as tk

# 2nd task
# popup:
import tkinter as tk

def open_gpa_button():
    popup = tk.Toplevel(window)
    popup.title("GPA Calculator")
    popup.geometry("600x500")
    popup.configure(bg="#FFF1F3")

    subject_entries = []

    head_label = tk.Label(popup, text="How much will my GPA be?", font=("Times New Roman", 20), bg="#FFF1F3")
    head_label.pack(pady=10)

    sem_label = tk.Label(popup, text="Semester", font=("Times New Roman", 15), bg="#FFF1F3")
    sem_label.pack(pady=10)

    # Frame for table
    table_frame = tk.Frame(popup, bg="#FFF1F3")
    table_frame.pack()

    # Headers
    headers = ["Subject", "CIE Marks", "SEE Marks", "Credits"]
    for col, text in enumerate(headers):
        tk.Label(table_frame, text=text, font=("Arial", 12, "bold"), bg="#FFF1F3", fg="#4E2A40", padx=10).grid(row=0, column=col)

    # Entry rows
    for row in range(8):
        row_vars = []
        for col in range(4):
            var = tk.StringVar()
            entry = tk.Entry(table_frame, width=15, textvariable=var, bd=2)
            entry.grid(row=row+1, column=col, padx=5, pady=5)

            # Cursor focus shift
            def bind_focus(e, r=row, c=col):
                try:
                    if c < 3:
                        table_frame.grid_slaves(row=r+1, column=c+1)[0].focus_set()
                    elif r < 7:
                        table_frame.grid_slaves(row=r+2, column=0)[0].focus_set()
                except:
                    pass

            entry.bind("<Return>", bind_focus)
            row_vars.append(var)
        subject_entries.append(row_vars)

    # GPA Calculation Logic
    def calculate_gpa():
        total_credits = 0
        total_points = 0
        suspicious_entry = False

        for row in subject_entries:
            try:
                cie_str = row[1].get()
                see_str = row[2].get()
                credit_str = row[3].get()

                if not (cie_str and see_str and credit_str):
                    continue  # Skip incomplete rows

                cie = int(cie_str)
                see = int(see_str)
                credits = int(credit_str)

                if cie > 50 or see > 50:
                    suspicious_entry = True

                marks = cie + see

                if marks >= 90:
                    grade_point = 10
                elif marks >= 80:
                    grade_point = 9
                elif marks >= 70:
                    grade_point = 8
                elif marks >= 60:
                    grade_point = 7
                elif marks >= 50:
                    grade_point = 6
                elif marks >= 40:
                    grade_point = 5
                else:
                    grade_point = 0

                total_credits += credits
                total_points += grade_point * credits

            except ValueError:
                continue  # Skip invalid numbers

        if total_credits == 0:
            result_text = "Please enter valid marks and credits."
        elif suspicious_entry:
            result_text = "Marks exceed expected range (CIE/SEE > 50). Check again!"
        else:
            gpa = total_points / total_credits
            result_text = f"Your GPA is: {gpa:.2f}"

        result_label.config(text=result_text)
        popup.focus_set()

    # Button to calculate GPA
    calc_button = tk.Button(popup, text="Calculate GPA", command=calculate_gpa,
                            bg="#B497BD", fg="white", font=("Arial", 12, "bold"))
    calc_button.pack(pady=10)

    # Result Label
    result_label = tk.Label(popup, text="", font=("Arial", 14, "bold"), bg="#FFF1F3", fg="#4E2A40")
    result_label.pack(pady=10)

#see:
def open_see_button():
    popup = tk.Toplevel(window)
    popup.title("SEE Requirement for Target GPA")
    popup.geometry("700x550")
    popup.configure(bg="#FFF1F3")

    entries = []

    # Header
    tk.Label(popup, text="Target GPA Calculator", font=("times new roman", 20), bg="#FFF1F3").pack(pady=10)

    # Target GPA Entry
    target_gpa_frame = tk.Frame(popup, bg="#FFF1F3")
    target_gpa_frame.pack(pady=5)
    tk.Label(target_gpa_frame, text="Enter your target GPA:", font=("Arial", 12), bg="#FFF1F3").pack(side="left")
    target_gpa_var = tk.StringVar()
    tk.Entry(target_gpa_frame, textvariable=target_gpa_var, width=5).pack(side="left", padx=10)

    table_frame = tk.Frame(popup, bg="#FFF1F3")
    table_frame.pack()

    headers = ["Subject", "CIE Marks", "Credits"]
    for col, text in enumerate(headers):
        tk.Label(table_frame, text=text, font=("Arial", 12, "bold"),
                 bg="#FFF1F3", fg="#4E2A40", padx=10).grid(row=0, column=col)

    for row in range(8):
        row_entries = []
        for col in range(3):  # 3 columns
            var = tk.StringVar()
            entry = tk.Entry(table_frame, textvariable=var, width=15,
                             font=("Arial", 10), bd=2, relief="groove",
                             highlightthickness=1, highlightbackground="#A8A8A8", highlightcolor="#8B5E83")
            entry.grid(row=row+1, column=col, padx=5, pady=5)

            def bind_focus_shift_closure(r=row, c=col):
                def bind_focus_shift(event):
                    if c < 2:
                        next_widget = table_frame.grid_slaves(row=r+1, column=c+1)
                    elif r < 7:
                        next_widget = table_frame.grid_slaves(row=r+2, column=0)
                    else:
                        next_widget = None
                    if next_widget:
                        next_widget[0].focus_set()
                return bind_focus_shift

            entry.bind("<Return>", bind_focus_shift_closure())
            row_entries.append(var)
        entries.append(row_entries)

    result_label = tk.Label(popup, text="", font=("Arial", 12), bg="#FFF1F3", fg="#4E2A40", justify="left", anchor="w")
    result_label.pack(pady=10)

    def calculate_required_see():
        try:
            target_gpa = float(target_gpa_var.get())
            if not (0 <= target_gpa <= 10):
                raise ValueError
        except:
            result_label.config(text="Enter a valid target GPA (0–10).")
            return

        total_credits = 0
        for row in entries:
            try:
                credits = int(row[2].get())
                total_credits += credits
            except:
                continue

        if total_credits == 0:
            result_label.config(text="Please enter credits properly.")
            return

        required_total_points = target_gpa * total_credits
        results = []
        used_points = 0

        for row in entries:
            try:
                subject = row[0].get() or "Subject"
                cie = int(row[1].get())
                credits = int(row[2].get())

                # Distribute required points evenly per subject
                required_points = (target_gpa * credits)
                # Convert grade point to marks → approx:
                # GP 10 → 90, 9 → 80 ... GP 5 → 40
                # So 1 GP ≈ 10 marks (linear)
                total_marks_needed = required_points * 10 / credits  # So total marks
                see_needed = total_marks_needed - cie
                see_needed = max(0, min(see_needed, 50))

                results.append(f"{subject}: Need {see_needed:.1f} in SEE")
            except:
                continue

        if results:
            result_label.config(text="\n".join(results))
        else:
            result_label.config(text="Please enter valid subject data.")

    # Button
    tk.Button(popup, text="Calculate Required SEE Marks", command=calculate_required_see,
              bg="#B497BD", fg="white", font=("Arial", 12, "bold")).pack(pady=10)




# 1st task
# basic gui window:
window = tk.Tk()
window.title("GPA CALCULATOR")
window.geometry("400x300")
window.configure(bg="#FFF1F3")

# puts the thing in a box, easier to align
content_frame = tk.Frame(window, bg="#FFF1F3") #frame=container
content_frame.place(relx=0.5, rely=0.5, anchor="center")

# say welcome to the calculator:
heading_label = tk.Label(window, text="Welcome to GPA calculator",font=("times new roman",20),bg="#FFF1F3",fg="#8B5E83")
heading_label.pack(pady=40)

# two buttons:
gpa_button = tk.Button(window, text= "How much will my gpa be?",bg="#E8C0C8",fg="#4E2A40",command = open_gpa_button)
gpa_button.pack()

see_button = tk.Button(window, text="How much would I need to score in finals?",bg="#E8C0C8",fg="#4E2A40", command= open_see_button)
see_button.pack(pady = 10)

window.mainloop()

#end notes :
# re read and throughly revise everything inside popup fun of 2nd task and focus on the cursor thing which i have marked as cursor curse
# LOGIC OF SECOND BUTTON IS WRONG...
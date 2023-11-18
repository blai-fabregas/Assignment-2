import tkinter as tk
from tkinter import messagebox

def submit_data():
    if privacy_var.get()== "Agree":
        # Gathering User's Info
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        middle_initial = middle_initial_entry.get()
        age = age_spinbox.get()
        unit_number_val = unit_number_entry.get()
        street_name_val = street_name_entry.get()
        municipality_val = municipality_entry.get()
        city_val = city_entry.get()
        zip_code_val = zip_code_entry.get()

        # Reciept 
        info_text = (
            f"Name: {last_name}, {first_name} {middle_initial}\n"
            f"Age: {age}\n"
            f"Address: {unit_number_val} {street_name_val} {municipality_val} {city_val} {zip_code_val}"
        )
        messagebox.showinfo("Form Submission Result", info_text)
        window.destroy()  # Closing main wundow
    else:
        messagebox.showwarning(
            title="Error", message="Check the box if you confirm that you entered correct information."
        )
# Main Window
window = tk.Tk()
window.title("User Background")
window.geometry("800x1000")

# Window Background Photo
image_path = "C:\\Users\\uella blainne\\Downloads\\Background.gif"
photo = tk.PhotoImage(file=image_path)
background_label = tk.Label(window, image=photo)
background_label.place(relwidth=1, relheight=1)

text = tk.Label(
    window,
    text="Fill out this Form",
    font=("Times New Roman bold italic", 50),
    fg="#C8AE7D",
)
text.pack()

frame = tk.Frame(window)
frame.pack()

# Widgets
user_info_frame = tk.LabelFrame(window, 
    text="User Information", 
    font=("Poppins Italic", 15), 
    fg="#65451F")
user_info_frame.pack(padx=40, pady=40)

first_name_label = tk.Label(
    user_info_frame, 
    text="First Name", 
    font=("Times New Roman", 12), 
    fg="#65451F"
)
first_name_label.grid(row=0, column=0)

last_name_label = tk.Label(user_info_frame, 
    text="Last Name", 
    font=("Times New Roman", 12), 
    fg="#65451F")
last_name_label.grid(row=0, column=1)


middle_initial_label = tk.Label(user_info_frame, 
    text="Middle Initial", 
    font=("Times New Roman", 12), 
    fg="#65451F")
middle_initial_label.grid(row=0, column=2)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
middle_initial_entry = tk.Entry(user_info_frame)

first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)
middle_initial_entry.grid(row=1, column=2)

age_label = tk.Label(user_info_frame, 
    text="Age", 
    font=("Times New Roman", 12), 
    fg="#65451F")
age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=200)
age_label.grid(row=2, column=1)
age_spinbox.grid(row=3, column=1)

address_frame = tk.LabelFrame(window, 
    text="Address", 
    font=("Poppins Italic", 15), 
    fg="#65451F")
address_frame.pack(padx=50, pady=50)

unit_number = tk.Label(address_frame, 
    text="Unit/House Number", 
    font=("Times New Roman", 12), 
    fg="#65451F")
unit_number.grid(row=1, column=0)
street_name = tk.Label(address_frame, 
    text="Street", 
    font=("Times New Roman", 12), 
    fg="#65451F")
street_name.grid(row=1, column=1)
municipality = tk.Label(address_frame, 
    text="Municipality", 
    font=("Times New Roman", 12), 
    fg="#65451F")
municipality.grid(row=1, column=2)
city = tk.Label(address_frame, 
    text="City", 
    font=("Times New Roman", 12), 
    fg="#65451F")
city.grid(row=3, column=0)
zip_code = tk.Label(address_frame, 
    text="ZIP Code", 
    font=("Times New Roman", 12), 
    fg="#65451F")
zip_code.grid(row=3, column=1)

unit_number_entry = tk.Entry(address_frame)
street_name_entry = tk.Entry(address_frame)
municipality_entry = tk.Entry(address_frame)
city_entry = tk.Entry(address_frame)
zip_code_entry = tk.Entry(address_frame)

unit_number_entry.grid(row=2, column=0)
street_name_entry.grid(row=2, column=1)
municipality_entry.grid(row=2, column=2)
city_entry.grid(row=4, column=0)
zip_code_entry.grid(row=4, column=1)

privacy_frame = tk.LabelFrame(window, 
    text="Data Privacy", 
    font=("Times New Roman", 12), 
    fg="#65451F")
privacy_frame.pack()

privacy_var = tk.StringVar(value="Disagree")
privacy_check = tk.Checkbutton(
    privacy_frame,
    text="I agree that all the information I put are all correct.", 
    font=("Times New Roman bold italic", 15), 
    fg="#65451F",
    variable=privacy_var,
    onvalue="Agree", offvalue="Disagree",
)
privacy_check.grid(row=1, column=0)
 
 # Submit Button
submit_button = tk.Button(window, 
    text='SUBMIT', 
    font=("Times New Roman Bold", 18),
    fg="#65451F", 
    command=submit_data)
submit_button.pack()

window.mainloop()

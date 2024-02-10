from datetime import datetime
import tkinter as tk
from tkinter import ttk

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.appointments = []

class Appointment:
    def __init__(self, user, start_time, end_time):
        self.user = user
        self.start_time = start_time
        self.end_time = end_time

def create_appointment(user, start_time, end_time):
    appointment = Appointment(user, start_time, end_time)
    user.appointments.append(appointment)
    return appointment

def create_user():
    username = username_entry.get()
    password = password_entry.get()
    user = User(username, password)
    users.append(user)
    user_label["text"] = f"User '{username}' created successfully."
    display_users()

def create_appointment_gui():
    username = username_app_entry.get()
    user = next((u for u in users if u.username == username), None)
    if user:
        start_time_str = start_time_entry.get()
        end_time_str = end_time_entry.get()

        try:
            start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
            end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            appointment_label["text"] = "Invalid date format. Please use 'YYYY-MM-DD HH:MM:SS'."
            return

        appointment = create_appointment(user, start_time, end_time)
        appointment_label["text"] = f"Appointment for '{username}' created successfully."
        display_users()
    else:
        appointment_label["text"] = f"User '{username}' not found."

def display_users():
    table.delete(*table.get_children())
    for user in users:
        for appointment in user.appointments:
            table.insert("", "end", values=(user.username, appointment.start_time, appointment.end_time))

users = []

# Main window
root = tk.Tk()
root.title("Appointment Scheduling System")

# User Creation
frame_user = ttk.Frame(root, padding="10")
frame_user.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame_user, text="Create User").grid(row=0, column=0, columnspan=2, pady=(0, 10))

ttk.Label(frame_user, text="Username:").grid(row=1, column=0, sticky=tk.W)
username_entry = ttk.Entry(frame_user)
username_entry.grid(row=1, column=1, sticky=tk.W)

ttk.Label(frame_user, text="Password:").grid(row=2, column=0, sticky=tk.W)
password_entry = ttk.Entry(frame_user, show="*")
password_entry.grid(row=2, column=1, sticky=tk.W)

create_user_button = ttk.Button(frame_user, text="Create User", command=create_user)
create_user_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))

user_label = ttk.Label(frame_user, text="")
user_label.grid(row=4, column=0, columnspan=2, pady=(10, 0))

# Appointment Creation
frame_appointment = ttk.Frame(root, padding="10")
frame_appointment.grid(row=0, column=1, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame_appointment, text="Create Appointment").grid(row=0, column=0, columnspan=2, pady=(0, 10))

ttk.Label(frame_appointment, text="Username:").grid(row=1, column=0, sticky=tk.W)
username_app_entry = ttk.Entry(frame_appointment)
username_app_entry.grid(row=1, column=1, sticky=tk.W)

ttk.Label(frame_appointment, text="Start Time (YYYY-MM-DD HH:MM:SS):").grid(row=2, column=0, sticky=tk.W)
start_time_entry = ttk.Entry(frame_appointment)
start_time_entry.grid(row=2, column=1, sticky=tk.W)

ttk.Label(frame_appointment, text="End Time (YYYY-MM-DD HH:MM:SS):").grid(row=3, column=0, sticky=tk.W)
end_time_entry = ttk.Entry(frame_appointment)
end_time_entry.grid(row=3, column=1, sticky=tk.W)

create_appointment_button = ttk.Button(frame_appointment, text="Create Appointment", command=create_appointment_gui)
create_appointment_button.grid(row=4, column=0, columnspan=2, pady=(10, 0))

appointment_label = ttk.Label(frame_appointment, text="")
appointment_label.grid(row=5, column=0, columnspan=2, pady=(10, 0))

# User Display
frame_display = ttk.Frame(root, padding="10")
frame_display.grid(row=0, column=2, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

table = ttk.Treeview(frame_display, columns=("Username", "Start Time", "End Time"), show="headings")
table.heading("Username", text="Username")
table.heading("Start Time", text="Start Time")
table.heading("End Time", text="End Time")
table.grid(row=0, column=0, pady=(0, 10))

display_users_button = ttk.Button(frame_display, text="Display Users", command=display_users)
display_users_button.grid(row=1, column=0, pady=(10, 0))

root.mainloop()
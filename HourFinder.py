import datetime
import json
import tkinter as tk
from tkinter.ttk import Progressbar
from tkcalendar import DateEntry

# File to store work data
DATA_FILE = "work_hours.txt"

grad_date = datetime.datetime(2025, 4, 16)
grace_period_ends = datetime.datetime(2025, 10, 16)
hours_needed_for_pr = 1560

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"hours_worked": 607.78, "logs": {}}

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def calculate_remaining_hours(data):
    return max(hours_needed_for_pr - data["hours_worked"], 0)

def calculate_weeks_left():
    today = datetime.datetime.today()
    remaining_time = grace_period_ends - today
    return max(remaining_time.days // 7, 1)

def calculate_required_weekly_hours():
    remaining_hours = calculate_remaining_hours(load_data())
    weeks_left = calculate_weeks_left()
    return round(remaining_hours / weeks_left, 2)

def log_hours(date_str, hours, label, progress_bar):
    data = load_data()
    if date_str in data["logs"]:
        data["logs"][date_str] += hours
    else:
        data["logs"][date_str] = hours
    
    data["hours_worked"] += hours
    save_data(data)
    
    # Update the labels and progress bar
    label.config(text=f"Required Weekly Hours: {calculate_required_weekly_hours()}")
    total_hours_label.config(text=f"Total Hours Worked: {data['hours_worked']:.2f}")
    
    # Update progress bar
    progress = (data["hours_worked"] / hours_needed_for_pr) * 100
    progress_bar["value"] = progress

def bulk_log_week(start_date, total_hours, label, progress_bar):
    data = load_data()
    for i in range(7):
        day = (datetime.datetime.strptime(start_date, "%Y-%m-%d") + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        data["logs"][day] = total_hours / 7
    data["hours_worked"] += total_hours
    save_data(data)
    
    # Update the labels and progress bar
    label.config(text=f"Required Weekly Hours: {calculate_required_weekly_hours()}")
    total_hours_label.config(text=f"Total Hours Worked: {data['hours_worked']:.2f}")
    
    # Update progress bar
    progress = (data["hours_worked"] / hours_needed_for_pr) * 100
    progress_bar["value"] = progress

def create_gui():
    root = tk.Tk()
    root.title("Work Hours Tracker")
    root.geometry("400x400")
    root.config(bg="black")
    
    tk.Label(root, text="Enter Hours Worked", font=("Arial", 12), fg="white", bg="black").pack(pady=10)
    
    date_label = tk.Label(root, text="Select Date:", fg="white", bg="black")
    date_label.pack()
    date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
    date_entry.pack()
    
    hours_entry = tk.Entry(root, fg="white", bg="black", insertbackground="white")
    hours_entry.pack()
    
    required_hours_label = tk.Label(root, text=f"Required Weekly Hours: {calculate_required_weekly_hours()}", font=("Arial", 12), fg="white", bg="black")
    required_hours_label.pack(pady=10)
    
    # Display Total Hours Worked
    global total_hours_label
    total_hours_label = tk.Label(root, text=f"Total Hours Worked: {load_data()['hours_worked']:.2f}", font=("Arial", 12), fg="white", bg="black")
    total_hours_label.pack(pady=5)
    
    # Create a progress bar
    progress_bar = Progressbar(root, length=300, mode='determinate', maximum=100)
    progress_bar.pack(pady=10)
    
    # Initialize the progress bar value
    progress = (load_data()["hours_worked"] / hours_needed_for_pr) * 100
    progress_bar["value"] = progress
    
    def log_button_action():
        try:
            log_hours(date_entry.get_date().strftime("%Y-%m-%d"), float(hours_entry.get()), required_hours_label, progress_bar)
        except ValueError:
            total_hours_label.config(text="Invalid input. Please enter a valid number.")
    
    tk.Button(root, text="Log Hours", command=log_button_action, fg="white", bg="black").pack(pady=5)
    
    tk.Label(root, text="Bulk Log a Week", font=("Arial", 12), fg="white", bg="black").pack(pady=10)
    
    week_label = tk.Label(root, text="Select Start Date:", fg="white", bg="black")
    week_label.pack()
    week_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
    week_entry.pack()
    
    total_hours_entry = tk.Entry(root, fg="white", bg="black", insertbackground="white")
    total_hours_entry.pack()
    
    def bulk_button_action():
        try:
            bulk_log_week(week_entry.get_date().strftime("%Y-%m-%d"), float(total_hours_entry.get()), required_hours_label, progress_bar)
        except ValueError:
            total_hours_label.config(text="Invalid input. Please enter a valid number.")
    
    tk.Button(root, text="Bulk Log", command=bulk_button_action, fg="white", bg="black").pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()

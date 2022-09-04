from Admin import Admin
from Employee import Employee
from AttendanceSystem import AttendanceSystem

from tkinter import * 

main_window = Tk()
main_window.geometry("500x200")

Label(main_window, text = "Please enter the admin file name").grid(row = 0, column = 0)
admin_file_entry = Entry(main_window)
admin_file_entry.grid(row = 0, column = 1)
Label(main_window, text = "Please enter the employee file name").grid(row = 1, column = 0)
employee_file_entry = Entry(main_window)
employee_file_entry.grid(row = 1, column = 1)

def show_attendance_system():
    attendance_system = AttendanceSystem(admin_file_entry.get(), employee_file_entry.get())

Button(main_window, text = "Enter", command = show_attendance_system).grid(row = 2, column = 0)

mainloop()

















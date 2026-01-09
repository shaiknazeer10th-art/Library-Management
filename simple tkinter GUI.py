import tkinter as tk
def calculator_sum():
# get a value from text boxes
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    # try converting to integers and calculate sum
    try:
        total= int(num1) + int(num2)
        result_label.config(text=f"sum: {total}")
    except ValueError:
        result_label.config(text="Invalid input Please enter numbers.") 
# create the main window
root = tk.Tk()  
root.title("simple sum calculator")
# create and place labels and text boxes
label1 = tk.Label(root, text="Enter first number")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()
label2 = tk.Label(root, text="Enter second number")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()
# create and place calculate button
calc_button = tk.Button(root, text="calculator Sum", command= calculator_sum) 
calc_button.pack()
# create and place result label
result_label = tk.Label(root, text="Sum: ")
result_label.pack()
# run the application 
root.mainloop()

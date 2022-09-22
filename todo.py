import tkinter
import tkinter.messagebox
import pickle

# Create window
root = tkinter.Tk()
root.title("To-Do List")

def add_task():
	task = entry_task.get() # .get() method allows you to get the text of what you entered
	if task != "": # Check to make sure entry is NOT "" or nothing
		listbox_tasks.insert(tkinter.END, task) # Put "task" into listbox at the END
		entry_task.delete(0, tkinter.END) # Clears entry widget (clear from 0th element to the END)
	else: # If input is nothing, show warning
		tkinter.messagebox.showwarning(title="warning!", message= "Please enter a task")

def delete_task():
	try:
		tasks_index = listbox_tasks.curselection()[0] # curselection()[0] is current selection of tasks (Can select multiple items so [0] will be the first element)
		listbox_tasks.delete(tasks_index)
	except: # If tasks IS NOT selected and delete is pressed
		tkinter.messagebox.showwarning(title="warning!", message = "Please select a task")

def load_tasks():
	try:
		tasks = pickle.load(open("tasks.dat", "rb")) # Using pickle module, rb = reading binary for Load
		listbox_tasks.delete(0, tkinter.END) # Delete everything from 0 to END in the listbox before loading
		for task in tasks: # Use for loop to iterate through the tasks file that was loaded
			listbox_tasks.insert(tkinter.END, task) # Put "task" into Listbox at the END
	except:
		tkinter.messagebox.showwarning(title="warning!", message = "tasks.dat not found")
def save_tasks():
	tasks = listbox_tasks.get(0,listbox_tasks.size()) # This gets all the tasks that are currently in the list (0 to listbox task size)
	pickle.dump(tasks, open("tasks.dat", "wb")) # Using pickle module, wb = writing binary for Save

# Create GUI
# Create a frame to hold the scrollbar and the tasks
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50) # Listbox will have these dimensions and go into the frame_tasks directory
listbox_tasks.pack(side=tkinter.LEFT)

# Create scrollbar
scrollbar_tasks = tkinter.Scrollbar(frame_tasks) # Go into the frame_tasks directory
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# Make the scrollbar work PROPERLY
listbox_tasks.config(yscrollcommand=scrollbar_tasks.set) # When scrolling in the Y-direction, it will call the scrollbar_tasks.set method
scrollbar_tasks.config(command=listbox_tasks.yview) # View of Y-coordinates

# Create entry box for input
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

# Create add task button
button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

# Create delete task button
button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

# Create load task button
button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
button_load_tasks.pack()

# Create add task button
button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.pack()

# Keep program from stopping after it reaches the end of the code
root.mainloop()
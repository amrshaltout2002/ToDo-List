"""
Structure of the app
1. add tasks to a list
2. mark task as complete
3. view tasks
4. quit
"""

tasks = []

def add_task():
  # get task from user
  task = input("Enter task: ")
  # define task status
  task_info = {"task": task, "completed": False}
  # add task to the list of tasks
  tasks.append(task_info)
  print("Task added to the list successfuly")

def mark_task_complete():
  # get list of incomplete tasks
  incomplete_tasks = [task for task in tasks if task["completed"] is False]

  if not incomplete_tasks:
    print("No tasks to mark as complete")
    return
  # show them to the user
  for i, task in enumerate(incomplete_tasks):
    print(f"{i+1}- {task['task']}")
    print("-" * 21)

  # get the task from the user
  try:
    task_number = int(input("choose the completed task: "))

    if task_number < 1 or task_number > len(incomplete_tasks):
      print("Invalid task number")
      return
    # mark the task as completed
    incomplete_tasks[task_number - 1]["completed"] = True
    print("Task marked completed")
  except ValueError:
    print("Invalid input, Please enter a number")  

  #print a message to the user

def view_tasks(tasks):
  # if there are no tasks, print a message and return
  if not tasks: print("No tasks to view"); return

  for i, task in enumerate(tasks):
    status = "✔" if task["completed"] else "❌"
    print(f"{i+1}. {task['task']} {status}")

def main():
  message = """
  1. add tasks to a list
  2. mark task as complete
  3. view tasks
  4. quit
  """
  
  while True:
    print(message)
    choice = input("Enter your choise: ")
  
    if choice == "1":
      add_task()
    elif choice == "2":
      mark_task_complete()
    elif choice == "3":
      view_tasks(tasks)
    elif choice == "4":
      break
    else:
      print("Invalid choice, please enter a number between 1 and 4")

if __name__ == "__main__":
  main()
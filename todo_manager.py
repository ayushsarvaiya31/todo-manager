class TodoList:
    def __init__(self):
        self.todos = []
        self.menu()

    def menu(self):
        
        while True:
            print("\nMenu:")
            print("1. Add Todo")
            print("2. Save Todos to File")
            print("3. Load Todos from File")
            print("4. Mark Todo as Done")
            print("5. Display Todos")
            print("6. Delete Todos")
            print("7. Exit")
            
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.add_todo()
                elif choice == 2:
                    self.save_todo()
                elif choice == 3:
                    self.load_todo()
                elif choice == 4:
                    self.mark_todo()
                elif choice == 5:
                    self.display()
                elif choice==6:
                    self.delete_todo()
                elif choice == 7:
                    print("Exiting program.")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 7.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def add_todo(self):
        print("\nEnter your tasks. Type 'END' to stop.")
        while True:
            taskname = input("Task Name: ")
            if taskname.upper() == 'END':
                break
            if any(todo['Task'] == taskname for todo in self.todos):
                print("Task already exists. Please enter a different task.")
            else:
                self.todos.append({"Task": taskname, "Status": False})
                print("Task added successfully.")

    def save_todo(self):
        try:
            with open("list.txt", "w") as f:
                for todo in self.todos:
                    status = "Done" if todo["Status"] else "Not Done"
                    f.write(f"{todo['Task']} - {status}\n")
            print("Tasks saved successfully.")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_todo(self):
        try:
            with open("list.txt", "r") as f:
                self.todos = []
                for line in f:
                    task, status = line.strip().rsplit(" - ", 1)
                    self.todos.append({"Task": task, "Status": status == "Done"})
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("No saved todos found.")
        except Exception as e:
            print(f"Error loading tasks: {e}")

    def display(self):
        if not self.todos:
            print("No tasks to display.")
        else:
            for i, todo in enumerate(self.todos, start=1):
                status = "Done" if todo["Status"] else "Not Done"
                print(f"{i}. {todo['Task']} - {status}")

    def mark_todo(self):
        if not self.todos:
            print("No tasks to mark.")
            return
        self.display()
        try:
            index = int(input("Enter the task number to mark as done: "))
            if 1 <= index <= len(self.todos):
                self.todos[index - 1]["Status"] = True
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
            
    def delete_todo(self):
        if not self.todos:
            print("No tasks to delete.")
            return
        self.display()
        try:
            index = int(input("Enter the task number to delete: "))
            if 1 <= index <= len(self.todos):
                del self.todos[index - 1]
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    

TodoList()

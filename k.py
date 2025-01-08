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
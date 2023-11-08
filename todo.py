to_do_list = []

while True:
    task = input("Enter a task (or 'quit' to exit): ")
    if task == "quit":
        break
    to_do_list.append(task)

print("To-Do List:")
for i, task in enumerate(to_do_list, start=1):
    print(f"{i}. {task}")


# jhj?

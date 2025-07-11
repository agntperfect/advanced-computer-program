# Q.No.4: Write a program to simulate a basic stack and queue using a list.
# Provide options to push, pop (stack), enqueue, and dequeue (queue), using user-defined functions.

stack = []
queue = []

# Stack functions
def push_stack(val):
    stack.append(val)
    print(f"Pushed '{val}' into stack.")

def pop_stack():
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print(f"Popped '{stack.pop()}' from stack.")

# Queue functions
def enqueue(val):
    queue.append(val)
    print(f"Enqueued '{val}' into queue.")

def dequeue():
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print(f"Dequeued '{queue.pop(0)}' from queue.")

# Display function
def display():
    print(f"Current Stack: {stack}")
    print(f"Current Queue: {queue}")

# Menu loop
def main():
    while True:
        print("\nMenu:")
        print("1. Push (Stack)")
        print("2. Pop (Stack)")
        print("3. Enqueue (Queue)")
        print("4. Dequeue (Queue)")
        print("5. Display Stack and Queue")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            val = input("Enter value to push into stack: ")
            push_stack(val)

        elif choice == "2":
            pop_stack()

        elif choice == "3":
            val = input("Enter value to enqueue into queue: ")
            enqueue(val)

        elif choice == "4":
            dequeue()

        elif choice == "5":
            display()

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

main()

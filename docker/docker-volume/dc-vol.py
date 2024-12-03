# app.py
def main():
    print("Welcome to the Note-Taking App!")
    while True:
        user_input = input("Enter a note (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        with open("notes.txt", "a") as f:
            f.write(user_input + "\n")
            print("Note saved!")

if __name__ == "__main__":
    main()

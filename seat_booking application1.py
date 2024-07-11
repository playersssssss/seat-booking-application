# Function to display the menu options to the user
def show_menu():
    print("\nApache Airlines Seat Booking System")
    print("1. Check availability of seat")
    print("2. Book a seat")
    print("3. Show booking state")
    print("4. Exit program")


# Function to check the availability of a specific seat
def check_availability(seats):
    # Prompt the user to enter the seat number
    seat_number = input("Enter seat number to check availability (e.g., 1A): ")

    # Calculate the row and column index based on the seat number
    row = int(seat_number[:-1]) - 1
    col = ord(seat_number[-1]) - ord('A')

    # Check the seat status and print the result
    if seats[row][col] == 'F':
        print(f"Seat {seat_number} is available.")
    elif seats[row][col] == 'R':
        print(f"Seat {seat_number} is already booked.")
    else:
        print(f"Seat {seat_number} is not available for booking.")


# Function to book a specific seat if it is available
def book_seat(seats):
    # Prompt the user to enter the seat number
    seat_number = input("Enter seat number to book (e.g., 1A): ")

    # Calculate the row and column index based on the seat number
    row = int(seat_number[:-1]) - 1
    col = ord(seat_number[-1]) - ord('A')

    # Check if the seat is free, already booked, or unavailable and update accordingly
    if seats[row][col] == 'F':
        seats[row][col] = 'R'
        print(f"Seat {seat_number} has been booked.")
    elif seats[row][col] == 'R':
        print(f"Seat {seat_number} is already booked.")
    else:
        print(f"Seat {seat_number} is not available for booking.")


# Function to display the current booking state of all seats
def show_booking_state(seats):
    print("Current booking state:")
    # Loop through each seat and print its status
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            seat_label = f"{row + 1}{chr(ord('A') + col)}"
            print(f"{seat_label}: {seats[row][col]}", end='  ')
        print()


# Main function to run the seat booking application
def main():
    # Initialize the seats based on the Burak757 floor plan
    seats = [
        ['F' for _ in range(7)] for _ in range(80)
    ]
    # Set specific seats for aisle and storage area
    for i in range(80):
        seats[i][3] = 'X'  # Aisle
        seats[76][4] = 'S'
        seats[76][5] = 'S'
        seats[76][6] = 'S'
        seats[77][6] = 'S'
        seats[77][4] = 'S'  # Storage area
        seats[77][5] = 'S'  # Storage area


    while True:
        # Show the menu and prompt user for a choice
        show_menu()
        choice = input("Enter your choice: ")

        # Execute the corresponding function based on user choice
        if choice == '1':
            check_availability(seats)
        elif choice == '2':
            book_seat(seats)
        elif choice == '3':
            show_booking_state(seats)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Entry point of the program
if __name__ == "__main__":
    main()

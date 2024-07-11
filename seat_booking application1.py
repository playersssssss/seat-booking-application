import random
import string

# Dictionary to simulate a database table for storing passenger details
database = {}

# Set to store unique booking references
unique_references = set()


# Function to generate a unique booking reference
def generate_unique_booking_reference():
    while True:
        # Generate a random booking reference of 8 alphanumeric characters
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        # Check if the generated reference is unique
        if reference not in unique_references:
            unique_references.add(reference)
            return reference


# Function to display the menu options
def show_menu():
    print("\nApache Airlines Seat Booking System")
    print("1. Check availability of seat")
    print("2. Book a seat")
    print("3. Free a seat")
    print("4. Show booking state")
    print("5. Exit program")


# Function to check seat availability
def check_availability(seats):
    seat_number = input("Enter seat number to check availability (e.g., 1A): ")
    row = int(seat_number[:-1]) - 1  # Extract the row number from input
    col = ord(seat_number[-1]) - ord('A')  # Convert seat letter to column index
    if seats[row][col] == 'F':
        print(f"Seat {seat_number} is available.")
    elif seats[row][col] in unique_references:
        print(f"Seat {seat_number} is already booked with reference {seats[row][col]}.")
    else:
        print(f"Seat {seat_number} is not available for booking.")


# Function to book a seat
def book_seat(seats):
    seat_number = input("Enter seat number to book (e.g., 1A): ")
    row = int(seat_number[:-1]) - 1  # Extract the row number from input
    col = ord(seat_number[-1]) - ord('A')  # Convert seat letter to column index
    if seats[row][col] == 'F':
        # Generate a unique booking reference
        booking_reference = generate_unique_booking_reference()
        # Store passenger details
        passport_number = input("Enter passport number: ")
        name = input("Enter passenger name: ")
        database[booking_reference] = {
            'passport_number': passport_number,
            'name': name,
            'seat_row': row + 1,  # Store row number (1-indexed)
            'seat_col': chr(ord('A') + col)  # Store column letter (A, B, C, ...)
        }
        # Mark the seat as booked with the booking reference
        seats[row][col] = booking_reference
        print(f"Seat {seat_number} has been booked with reference {booking_reference}.")
    elif seats[row][col] in unique_references:
        print(f"Seat {seat_number} is already booked.")
    else:
        print(f"Seat {seat_number} is not available for booking.")


# Function to free a booked seat
def free_seat(seats):
    seat_number = input("Enter seat number to free (e.g., 1A): ")
    row = int(seat_number[:-1]) - 1  # Extract the row number from input
    col = ord(seat_number[-1]) - ord('A')  # Convert seat letter to column index
    booking_reference = seats[row][col]
    if booking_reference in unique_references:
        # Remove the booking reference from the set and database
        unique_references.remove(booking_reference)
        del database[booking_reference]
        # Mark the seat as free
        seats[row][col] = 'F'
        print(f"Seat {seat_number} has been freed.")
    else:
        print(f"Seat {seat_number} is already free or not available for booking.")


# Function to display the current booking state
def show_booking_state(seats):
    print("Current booking state:")
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            seat_label = f"{row + 1}{chr(ord('A') + col)}"  # Construct seat label (e.g., 1A, 1B, ...)
            print(f"{seat_label}: {seats[row][col]}", end='  ')
        print()


# Main function to run the seat booking system
def main():
    # Initialize the seats based on the Burak757 floor plan
    seats = [
        ['F' for _ in range(7)] for _ in range(80)
    ]
    for i in range(80):
        seats[i][3] = 'X'  # Aisle
        seats[76][4] = 'S'
        seats[76][5] = 'S'
        seats[76][6] = 'S'
        seats[77][6] = 'S'
        seats[77][4] = 'S'  # Storage area
        seats[77][5] = 'S'  # Storage area

    # Main loop to display menu and handle user input
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            check_availability(seats)
        elif choice == '2':
            book_seat(seats)
        elif choice == '3':
            free_seat(seats)
        elif choice == '4':
            show_booking_state(seats)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Entry point of the script
if __name__ == "__main__":
    main()

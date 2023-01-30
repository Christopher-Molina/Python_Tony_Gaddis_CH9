# Starting Out With Python 5th Edition: Chapter 9 - Exercise 1


def main():
    # Get dictionaries
    rooms, instructors, times = get_dictionaries()

    # Create a flag to control the program
    flag = True
    while flag:
        # Prompt the user for a course number
        course_number = input('Enter a course number (0 to exit): ').upper()
        if course_number == '0':
            flag = False
        else:
            # Display room, instructor, and time for the course number
            display_schedule(course_number, rooms, instructors, times)


# Function creates and returns three dictionaries
def get_dictionaries():
    rooms = {'CS101': 3004, 'CS102': 4501, 'CS103': 6755, 'NT110': 1244, 'CM241': 1411}

    instructors = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich',
                   'NT110': 'Burke', 'CM241': 'Lee'}

    times = {'CS101': '8:00 AM', 'CS102': '9:00 AM', 'CS103': '10:00 AM', 'NT110': '11:00 AM',
             'CM241': '1:00 PM'}

    return rooms, instructors, times


# Function displays the course number schedule
def display_schedule(course, rooms, instructors, times):
    valid = course in rooms
    if valid:
        print(f'Room: {rooms[course]}\nInstructor: {instructors[course]}\nTime: {times[course]}\n')
    else:
        print('ERROR: Course number not found.\n')


# Call the main function
if __name__ == '__main__':
    main()

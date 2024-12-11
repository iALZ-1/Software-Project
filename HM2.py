
class User:  #General class
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Student(User):  #inherits from user
    def __init__(self, name, email, student_id, college):
        super().__init__(name, email)
        self.student_id = student_id
        self.college = college

class Driver(User): #inherits from user
    def __init__(self, name, email, driver_id, location):
        super().__init__(name, email)
        self.driver_id = driver_id
        self.availability = True  # Default availability is True
        self.location = location

    def accept_request(self):
        print(f"Driver {self.name} accepted the request.")
        
    def reject_request(self):
        print(f"Driver {self.name} rejected the request.")
        self.availability = False


# Ride Class
class Ride:
    def __init__(self, student, driver, pickup, destination):
     
        self.student = student
        self.driver = driver
        self.pickup = pickup
        self.destination = destination
        self.status = "Pending"

    def start_trip(self):
        print("Ride  has started.")

    def complete_trip(self):
        for i in range(10):
            print("-")
        print("Ride has been completed.")
        exit()


# System Class
class System:
    def __init__(self):
        self.drivers = []
        self.rides = []

    def register_driver(self, driver):
        self.drivers.append(driver)

    def search_drivers(self):
        
        available_drivers = [driver for driver in self.drivers if driver.availability]
        
        if not available_drivers:
            print("No drivers available.")
            return None
        print(f"Found {len(available_drivers)} available driver(s).")
        
        # Iterate through Available drivers
        order = 0;
        for i in range(len(available_drivers)):
            order+=1
            print(f"Driver Details:\nDriverNumber: {order}\nName: {available_drivers[i].name}\nLocation: {available_drivers[i].location}")
            print("----------------")
        return available_drivers
            
        

    def book_ride(self, student, pickup, destination):
        while True:
            drivers = self.search_drivers()
            if not drivers:
                print("No Available drivers...")
                return None
            
            # Add try-except block around driver selection
            try:
                selected_driver = int(input("enter the driver number you prefer: "))
                if selected_driver < 1 or selected_driver > len(drivers):
                    print(f"Please enter a number between 1 and {len(drivers)}")
                    continue
                selected_driver = drivers[selected_driver - 1]
            except ValueError:
                print("Please enter a valid number")
                continue
            
            print(f"Driver Details:\nName: {selected_driver.name}\nLocation: {selected_driver.location}")

            # Ask driver for acceptance
            try:
                accept = input(f"Trip deatials:\n  pickup: {pickup}\n  destination: {destination}\nDoes the driver accept the ride? (yes/no): ").lower().strip()
                if accept in ['yes', 'y', 'Yes', 'YES', 'Y']:
                    selected_driver.accept_request()
                    new_ride = Ride(student, selected_driver, pickup, destination)
                    self.rides.append(new_ride)
                    print(f"Ride booked successfully with driver {selected_driver.name}.")
                    new_ride.start_trip()
                    return new_ride
                elif accept in ['no', 'n', 'No', 'NO', 'N']:
                    selected_driver.reject_request()
                    print("Searching for another driver...")
                    continue
                else:
                    raise ValueError("Please enter either 'yes' or 'no'")
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue



# Create a system
bookRide = System()

# Register drivers
driver1 = Driver(name="Mahmood", email="M@gmail.com", driver_id="1234", location="Library")
driver2 = Driver(name="Alazhar", email="A@gmail.com", driver_id="1235", location="Block E")
driver3 = Driver(name="Abdo", email="Abdo@gmail.com", driver_id="1236", location="EDU")
bookRide.register_driver(driver1)
bookRide.register_driver(driver2)
bookRide.register_driver(driver3)

# Add this new function:
def get_student_details():
    student_name = None
    student_email = None
    student_id = None
    college = None
    
    while True:
        try:
            if student_name is None:
                student_name = input("Enter student name: ")
                if not student_name.isalpha():
                    raise ValueError("Name should only contain letters")
                print("Debug: Name validated successfully")
            
            if student_email is None:
                student_email = input("Enter student email: ")
                # Check if email contains more than just dots and @ symbols
                if '@' not in student_email or '.' not in student_email or student_email.strip('@.') == '':
                    raise ValueError("Invalid email format")
                print("Debug: Email validated successfully")
            
            if student_id is None:
                student_id = input("Enter student ID: ")
                if not student_id.isdigit():
                    raise ValueError("Student ID should only contain numbers")
                print("Debug: ID validated successfully")
            
            if college is None:
                college = input("Enter college name: ")
                if not all(c.isalpha() or c.isspace() for c in college):
                    raise ValueError("College name should only contain letters and spaces")
                print("Debug: College validated successfully")
            
            return student_name, student_email, student_id, college
            
        except ValueError as e:
            print(f"Invalid input: {e}")
            print(f"Debug: Error occurred with message: {str(e)}")
            # Reset only the current invalid input
            if "Name" in str(e):
                student_name = None
            elif "email" in str(e):
                student_email = None
            elif "ID" in str(e):
                student_id = None
            elif "College" in str(e):
                college = None

# Replace the student creation line with:
student_name, student_email, student_id, college = get_student_details()
student = Student(name=student_name, email=student_email, student_id=student_id, college=college)

pickup = input("Enter pickup location: ")#strings
destination = input("Enter destination: ")#strings

# Book a ride
ride = bookRide.book_ride(student, pickup, destination)

# Complete the ride if booked
if ride:
    ride.complete_trip()
else:
    print("Ride booking failed. Please try again later.")

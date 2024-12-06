
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
        self.status = "Ongoing"
        print("Ride  has started.")

    def complete_trip(self):
        self.status = "Completed"
        print("Ride  has been completed.")


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
        for i in range(len(available_drivers)):
            print(f"Driver Details:\nName: {available_drivers[i].name}\nLocation: {available_drivers[i].location}")
            print("----------------")
        return available_drivers
            
        

    def book_ride(self, student, pickup, destination):
        while True:
            drivers = self.search_drivers()
            if not drivers:
                print("No Available drivers...")
                return None
            selected_driver = int(input("enter the driver you prefer: "))
            selected_driver=drivers[selected_driver]
            
            print(f"Driver Details:\nName: {selected_driver.name}\nLocation: {selected_driver.location}")

            # Ask driver for acceptance
            accept = input("Does the driver accept the ride? (yes/no): ").lower()
            if accept == "yes":
                selected_driver.accept_request()
                new_ride = Ride(student, selected_driver, pickup, destination)
                self.rides.append(new_ride)
                print(f"Ride booked successfully with driver {selected_driver.name}.")
                new_ride.start_trip()
                return new_ride
            else:
                selected_driver.reject_request()
                print("Searching for another driver...")
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


student_name = input("Enter student name: ")
student_email = input("Enter student email: ")
student_id = input("Enter student ID: ")
college = input("Enter college name: ")
student = Student(name=student_name, email=student_email, student_id=student_id, college=college)

pickup = input("Enter pickup location: ")
destination = input("Enter destination: ")

# Book a ride
ride = bookRide.book_ride(student, pickup, destination)

# Complete the ride if booked
ride.complete_trip()

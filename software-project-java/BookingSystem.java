import java.util.ArrayList;

public class BookingSystem {
    private ArrayList<Driver> drivers;
    private ArrayList<Ride> rides;

    public BookingSystem() {
        this.drivers = new ArrayList<Driver>();
        this.rides = new ArrayList<Ride>();
    }

    public void register_driver(Driver driver) {
        this.drivers.add(driver);
    }  

    public void search_drivers() {
        for (Driver driver : this.drivers) {
            if (driver.is_available()) {
                System.out.println(driver.getName());
            }
        }
    }

} 
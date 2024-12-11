import java.util.ArrayList;
public class SQUtaxi {
    private ArrayList<Driver> drivers;
    private ArrayList<Ride> rides;

    public SQUtaxi() {
        this.drivers = new ArrayList<>();
        this.rides = new ArrayList<>();
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

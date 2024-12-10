import java.lang.System;
public class Driver extends User {
    private String driver_id;
    private String location;
    private boolean availability = true;  // Default to true

    public Driver(String name, String email, String driver_id, String location) {
        super(name, email);
        this.driver_id = driver_id;
        this.location = location;
    }

    public boolean is_available() {
        return availability;
    }

    public void setAvailability(boolean availability) {
        this.availability = availability;
    }

    public String getName() {
        return name;
    }

    public void accept_request() {
        System.out.println("Driver " + getName() + " accepted the request.");
    }
    
    public void reject_request() {
        System.out.println("Driver " + getName() + " rejected the request.");
    }
}
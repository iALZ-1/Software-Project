import java.lang.System;
public class Ride {
    private Student student;
    private Driver driver;
    private String pickup;
    private String destination;
    private String status;

    public Ride(Student student, Driver driver, String pickup, String destination) {
        this.student = student;
        this.driver = driver;
        this.pickup = pickup;
        this.destination = destination;
        this.status = "Pending";
    }

    public void start_trip() {
        this.status = "Ongoing";
        System.out.println("Ride has started.");
    }

    public void complete_trip() {
        this.status = "Completed";
        System.out.println("Ride has been completed.");
    }
}

public class BookRide {
    private String pickup;
    private String destination;
    private String driver;

    public BookRide(String pickup, String destination, String driver) {
        this.pickup = pickup;
        this.destination = destination;
        this.driver = driver;
    }

    public void book_ride() {
        System.out.println("Ride booked successfully with driver " + driver + ".");
    }
}

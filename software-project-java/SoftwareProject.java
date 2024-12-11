public class SoftwareProject {
    public static void main(String[] args) {
        SQUtaxi system = new SQUtaxi();
        system.register_driver(new Driver("John Doe", "john.doe@example.com", "D123", "123 Main St"));
        system.search_drivers();
    }
}



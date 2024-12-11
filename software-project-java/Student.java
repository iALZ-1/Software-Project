public class Student extends User {
    private String student_id;
    private String college;

    public Student(String name, String email, String student_id, String college) {
        super(name, email);
        this.student_id = student_id;
        this.college = college;
    }
}

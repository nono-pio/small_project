public class Year {

    public String title;
    public String description;

    public double grade;

    public int[] partYearId;

    Year(String title, String desc, double grade, int[] partYearId) {
        this.title = title;
        this.description = desc;
        this.grade = grade;
        this.partYearId = partYearId;
    }
}
public class Test {

    public static void main(String[] args) {
        Database db = new Database();

        int[] partYearId = { 2, 1, 1 };
        Year year1 = new Year("year1", "jksbkjbdkjbk", 6.0d, partYearId);
        Year year2 = new Year("year2", "jksbkjbdkjbk", 5.0d, partYearId);
        Year year3 = new Year("year3", "jksbkjbdkjbk", 0.0d, partYearId);

        Year[] years = { year1, year2, year3 };

        db.year.clearAll();
        db.year.addAll(years);
        db.year.clear(2);
    }
}

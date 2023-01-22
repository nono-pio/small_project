import java.io.IOException;

public class YearManager {

    private final String fileName = "year.txt";

    private Year_db2 yearDb;

    YearManager() {
        yearDb = new Year_db2(fileName);
    }

    public void add(Year year) {
        try {
            yearDb.openFile('W');
            yearDb.write(year);
            yearDb.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void addAll(Year[] years) {
        try {
            yearDb.openFile('W');
            yearDb.writeAll(years);
            yearDb.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public Year[] getAll() {
        Year[] years;
        try {
            yearDb.openFile('R');
            years = yearDb.read();
            yearDb.close();

        } catch (IOException e) {
            e.printStackTrace();
            years = null;
        }
        return years;
    }

    public void replace(Year newYear, int idCurYear) {
        Year[] years = getAll();
        years[idCurYear] = newYear;
        clearAll();
        addAll(years);
    }

    public void clearAll() {
        try {
            yearDb.openFile('C');
            yearDb.clear();
            yearDb.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void clear(int idToClear){
        Year[] years = getAll();
        clearAll();
        
        Year[] newYears = new Year[years.length - 1];
        System.arraycopy(years, 0, newYears, 0, idToClear);
        if (years.length != idToClear) {
            System.arraycopy(years, idToClear + 1, newYears, idToClear, years.length - idToClear - 1);
        }

        addAll(newYears);
    }
}
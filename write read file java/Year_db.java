import java.io.*;
import java.util.ArrayList;

public class Year_db {
    private String fileName;

    private BufferedWriter fW;
    private BufferedReader fR;
    private BufferedWriter fC;
    private char mode;

    Year_db(String file) {
        fileName = file;
    };

    public void openFile(char m) throws IOException {
        mode = m;
        if (mode == 'R')
            fR = new BufferedReader(new FileReader(fileName));
        else if (mode == 'W')
            fW = new BufferedWriter(new FileWriter(fileName, true));
        else if (mode == 'C')
            fC = new BufferedWriter(new FileWriter(fileName));
    }

    public void clear() throws IOException {
        fC.write("");
    }

    public void write(Year year) throws IOException {
        String partYearIdString = "";
        for (int id : year.partYearId)
            partYearIdString += String.valueOf(id) + ';';

        fW.write(year.title + ';' + year.description + ';' + String.valueOf(year.grade)
                + '/' + partYearIdString.substring(0, partYearIdString.length() - 1));
        fW.newLine();
    }

    public void writeAll(Year[] years) throws IOException {
        String partYearIdString;
        for (Year year : years) {
            partYearIdString = "";
            for (int id : year.partYearId)
                partYearIdString += String.valueOf(id) + ';';

            fW.write(year.title + ';' + year.description + ';' + String.valueOf(year.grade)
                    + '/' + partYearIdString.substring(0, partYearIdString.length() - 1));
            fW.newLine();
        }
    }

    public Year[] read() throws IOException {
        ArrayList<Year> years = new ArrayList<>();
        Year year;

        String yearString;
        String[] yearAndPartYearId;
        String[] yearInfo;
        String[] partYearIdString;
        int[] partYearId;

        do {
            yearString = fR.readLine();
            if (yearString != null) {

                yearAndPartYearId = yearString.split("/");

                yearInfo = yearAndPartYearId[0].split(";");
                partYearIdString = yearAndPartYearId[1].split(";");

                partYearId = new int[partYearIdString.length];
                for (int i = 0; i < partYearIdString.length; i++)
                    partYearId[i] = Integer.valueOf(partYearIdString[i]);

                year = new Year(yearInfo[0], yearInfo[1], Double.valueOf(yearInfo[2]), partYearId);
                years.add(year);
            }
        } while (yearString != null);

        Year[] years2 = new Year[years.size()];
        return years.toArray(years2);
    }

    public void close() throws IOException {
        if (mode == 'R')
            fR.close();
        else if (mode == 'W')
            fW.close();
    }
}
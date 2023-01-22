import java.io.*;
import java.util.ArrayList;

public class Year_db2 {
    private String fileName;

    private FileOutputStream fosAppend;
    private FileOutputStream fos;

    private BufferedReader reader;

    private char mode;

    Year_db2(String file) {
        fileName = file;
    };

    public void openFile(char m) throws IOException {
        mode = m;
        if (mode == 'R')
            reader = new BufferedReader(new InputStreamReader( new FileInputStream(fileName)));
        else if (mode == 'W')
            fosAppend = new FileOutputStream(fileName, true);
        else if (mode == 'C')
            fos = new FileOutputStream(fileName);
    }

    public void clear() throws IOException {
        fos.write("".getBytes());
    }

    public void write(Year year) throws IOException {
        String partYearIdString = "";
        for (int id : year.partYearId) partYearIdString += String.valueOf(id) + ';';
        
        String text = year.title + ';' + year.description + ';' + String.valueOf(year.grade) + '/' + partYearIdString.substring(0, partYearIdString.length() - 1) + "\n";
        
        fosAppend.write(text.getBytes());
    }

    public void writeAll(Year[] years) throws IOException {
        String partYearIdString;
        for (Year year : years) {
            partYearIdString = "";
            for (int id : year.partYearId) partYearIdString += String.valueOf(id) + ';';

            String text = year.title + ';' + year.description + ';' + String.valueOf(year.grade) + '/' + partYearIdString.substring(0, partYearIdString.length() - 1) + "\n";
    
            fosAppend.write(text.getBytes());
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
            yearString = reader.readLine();
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
            reader.close();
        else if (mode == 'W') 
            fosAppend.close();
        else if (mode == 'C')
            fos.close();
    }
}
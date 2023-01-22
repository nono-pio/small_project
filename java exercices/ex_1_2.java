import java.util.*;
public class ex_1_2
{
    public static void main(String [] arg)
    {
        double a;
        Scanner lectureClavier = new Scanner(System.in);

        System.out.print("Entrer une valeur : ");
        a = lectureClavier.nextDouble();
        lectureClavier.close();

        System.out.println("Vous avez entrer : " + a);
    }
}
package AWT_interface;
import java.awt.*;
public class Fenetre {
    public final static int WIDTH = 500;
    public final static int HEIGTH = 500;

    public static void main(String [] arg)
    {
        Frame WIN = new Frame();
        WIN.setTitle("interface");
        WIN.setSize(WIDTH,HEIGTH);
        WIN.setBackground(Color.GRAY);

        Dessin page = new Dessin();
        WIN.add(page, "Center");
        WIN.add(new DesBoutons(page), "South");

        WIN.addWindowListener(new GestionWindow());

        WIN.setVisible(true);
    }
}

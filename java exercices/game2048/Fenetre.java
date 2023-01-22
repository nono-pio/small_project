package game2048;
import java.awt.*;

public class Fenetre{
    public static final int WIDTH = 300;
    public static final int HEIGTH = 300;

    public static void main(String [] arg)
    {
        Frame WIN = new Frame();
        WIN.setTitle("2048 Game");
        WIN.setSize(WIDTH, HEIGTH);
        WIN.setBackground(Color.GRAY);

        Game game = new Game();
        game.reset();

        Dessin page = new Dessin();
        WIN.add(page, "Center");
        //WIN.add(new DesBoutons(page), "South");

        WIN.addWindowListener(new GestionWindow());

        WIN.setVisible(true);
    }
}

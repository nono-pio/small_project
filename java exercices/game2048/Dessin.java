package game2048;
import java.awt.*;

public class Dessin extends Canvas {
    public final static Color couleurFond = Color.white;
    public final static int DX = (Fenetre.WIDTH-50)/Game.col;
    public final static int DY = (Fenetre.HEIGTH-50)/Game.row;
    public Dessin()
    {
        setBackground(couleurFond);
        //setForeground(couleur);
        setCursor(new Cursor(Cursor.CROSSHAIR_CURSOR));
    }

    public void paint(Graphics g)
    {
        for (int y = 0; y < Game.row; y++) {
            for (int x = 0; x < Game.col; x++) {
                if (Game.grid[y][x] != 0)
                {
                    new Square(DX * x,DY * y, g, Game.grid[y][x]);
                }
            }
        }
    }
}
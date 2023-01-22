package game2048;
import java.awt.*;

public class Square {
    public Square(int x, int y, Graphics g, int n )
    {
        Color c = getColorByNumber(n);
        g.setColor(c);
        g.fillRect(x, y, Dessin.DX, Dessin.DY);
        g.setColor(Color.black);
        g.setFont(null);
        g.drawString(""+n, x + Dessin.DX/2, y + Dessin.DY/2);
    }

    
    private Color getColorByNumber(int n)
    {
        Color color;
        switch (n)
        {
            case 2:
                color = new Color(255, 200, 0);
                break;
            case 4:
                color = new Color(255, 175, 0);
                break;
            case 8:
                color = new Color(255, 150, 0);
                break;
            case 16:
                color = new Color(255, 125, 0);
                break;
            case 32:
                color = new Color(255, 100, 0);
                break;
            case 64:
                color = new Color(255, 75, 0);
                break;
            case 128:
                color = new Color(255, 50, 0);
                break;
            case 256:
                color = new Color(255, 50, 0);
                break;
            case 512:
                color = new Color(225, 0, 0);
                break;
            case 1024:
                color = new Color(150, 0, 0);
                break;
            default:
                color = Color.black;
                break;
        }
        return color;
    }
}

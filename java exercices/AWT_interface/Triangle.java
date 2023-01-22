package AWT_interface;
import java.awt.*;
public class Triangle {
    private int centreX = Fenetre.WIDTH/2-50;
    private int centreY = Fenetre.HEIGTH/2-50;
    private int [] xPoints = {0, 10, -10};
    private int [] yPoints = {-10, 10, 10};
    int nPoints = 3;

    public Triangle(int lig, int col, Graphics g, Color c)
    {
        for (int i = 0; i < nPoints; i++) {
            xPoints[i] = xPoints[i] + (5*col) + centreX;
            yPoints[i] = yPoints[i] + (15*lig) + centreY;
        }
        g.setColor(c);
        g.fillPolygon(xPoints,yPoints,nPoints);
    }
}

package game2048;
import java.awt.event.*;
public class GestionWindow extends WindowAdapter {
    public void windowClosing(WindowEvent e)
    {
        System.exit(0);
    }
}
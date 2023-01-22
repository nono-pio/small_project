package AWT_interface;
//import java.awt.*;
import java.awt.event.*;
public class GestionAction implements ActionListener {
    private int n;
    private Dessin d;
    public GestionAction(int n, Dessin d)
    {
        this.n = n;
        this.d = d;
    }

    public void actionPerformed(ActionEvent e)
    {
        switch (n)
        {
            case 1:
                d.nouveau();
                break;
            case 2:
                System.exit(0);
                break;
        }
    }
}

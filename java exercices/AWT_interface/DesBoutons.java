package AWT_interface;
import java.awt.*;
//import java.awt.event.*;
public class DesBoutons extends Panel {
    public DesBoutons(Dessin d)
    {
        setBackground(Color.lightGray);

        Button bNouveau = new Button("Nouveau");
        Button bQuitter = new Button("Quitter");
        bNouveau.addActionListener(new GestionAction(1,d));
        this.add(bNouveau);
        bQuitter.addActionListener(new GestionAction(2,d));
        this.add(bQuitter);
    }
}

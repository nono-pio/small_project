package game2048;

public class Game {
    public static int [][] grid;
    public static int col = 4;
    public static int row = 4;

    public Game()
    {
        grid = new int[row][col];
    }

    public void reset()
    {
        for (int y = 0; y < grid.length; y++) {
            for (int x = 0; x < grid.length; x++) {
                grid[y][x] = 0;
            }
        }
        placeNewSquare();
    }

    private void placeNewSquare()
    {
        int x = (int) Math.floor(Math.random() * col);
        int y = (int) Math.floor(Math.random() * row);
        if (grid[y][x] != 0)
        {
            placeNewSquare();
        } else {
            grid[y][x] = 2;
        }
    }
}

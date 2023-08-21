using System.Collections.Generic;

public static class CurrentBestNeuralNetwork
{
    public static List<int> generations = new List<int>();
    public static bool saveBest { get; set; } = false;
    public static bool auto { get; set; } = false;
    public static NeuralNetwork bestNet { get; set; }
}

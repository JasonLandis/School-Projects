using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using TMPro;
using Unity.VisualScripting;
using UnityEditor;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.Tilemaps;

public class NetManager : MonoBehaviour
{
    public GameObject victoryScreen;
    public TextMeshProUGUI putText;

    private bool finishedTraining = false;
    public int finishedNets = 0;
    public int generation = 0;

    public float bestFitness = 0;
    public float worstFitness = 0;

    private float holeInOneThreshold = 67f;
    private int population = 50;
    public int maxHitAttempts = 1;
    public float maxPower = 1000f;
    public float maxAngle = 180.0f;

    private int[] layers = {484, 484, 10, 2};

    public GameObject netBall;

    public List<NeuralNetwork> nets = new List<NeuralNetwork>();
    public List<GameObject> netBalls = new List<GameObject>();

    private Tilemap _tilemap;

    private int[] worldState = new int[482];
    public float goalPosX;
    public float goalPosY;

    private void Awake()
    {
        _tilemap = GameObject.Find("Tilemap").GetComponent<Tilemap>();
    }
    // Start is called before the first frame update
    void Start()
    {
        if(population%2 != 0)
        {
            population = 20;
            Debug.Log("Population must be divisible by 2, it was set to 20 by default otherwise");
        }

        parseWorld();


        for(int i = 0; i < population; i++)
        {
            
            if (CurrentBestNeuralNetwork.bestNet != null)
            {
                NeuralNetwork net = new NeuralNetwork(CurrentBestNeuralNetwork.bestNet, worldState);
                if (i != 0)
                {
                    net.Mutate();
                }
                nets.Add(net);
            }
            else
            {
                NeuralNetwork net = new NeuralNetwork(layers, worldState);
                net.Mutate();
                nets.Add(net);
            }
            GameObject newNetBall = Instantiate(netBall, new Vector3(-14.75f, -7.75f, 0), new Quaternion(0, 0, 0, 1));
            newNetBall.GetComponent<NetGolfBallController>().Init(nets[i], this);
            netBalls.Add(newNetBall);
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (!finishedTraining)
        {
            // These buttons control timescale of the evolution since the balls can take a long time to stop sometimes
            // Subject to change but shorthand is the following
            // MegaSpeed = m
            // SuperSpeed = d
            // SpeedUp = s
            // NormalSpeed = a
            // SlowDown = f
            if (Input.GetButtonDown("MegaSpeed"))
            {
                Time.timeScale = 100;
            }
            if (Input.GetButtonDown("SuperSpeed"))
            {
                Time.timeScale = 20;
            }
            if (Input.GetButtonDown("SpeedUp"))
            {
                Time.timeScale = 5;
            }
            if (Input.GetButtonDown("NormalSpeed"))
            {
                Time.timeScale = 0.5f;
            }
            if (Input.GetButtonDown("SlowDown"))
            {
                Time.timeScale = 0.5f;
            }

            if (finishedNets >= population)
            {
                // Finished nets is set to 0 so that we know none of the next generation have finished
                finishedNets = 0;

                int maxFitnessIndex = 0;
                float maxFitness = Mathf.NegativeInfinity;
                for (int i = 0; i < nets.Count; i++)
                {
                    if (nets[i].GetFitness() >= maxFitness)
                    {
                        maxFitnessIndex = i;
                        maxFitness = nets[i].GetFitness();
                    }
                }

                // Sort nets in ascending order so that nets[0] is worst fitness and nets[population - 1] is best
                nets.Sort();

                // Get fitnesses and times hit for display
                bestFitness = nets[population - 1].GetFitness();
                worstFitness = nets[0].GetFitness();

                if (bestFitness > holeInOneThreshold && CurrentBestNeuralNetwork.auto == false && CurrentBestNeuralNetwork.saveBest == true)
                {
                    ManualTrainSaveBest();
                    finishedTraining = true;
                    return;
                }
                else if (bestFitness > holeInOneThreshold && CurrentBestNeuralNetwork.auto == true && CurrentBestNeuralNetwork.saveBest == true)
                {
                    AutoTrainAllSaveBest();
                    finishedTraining = true;
                    return;
                }
                else if (bestFitness > holeInOneThreshold && CurrentBestNeuralNetwork.auto == true && CurrentBestNeuralNetwork.saveBest == false)
                {
                    AutoTrainAllForgetBest();
                    finishedTraining = true;
                    return;
                }
                else if (bestFitness > holeInOneThreshold && CurrentBestNeuralNetwork.auto == false && CurrentBestNeuralNetwork.saveBest == false)
                {
                    AutoTrainForgetBest();
                    finishedTraining = true;
                    return;
                }

                // Generate next generation
                for (int i = 0; i < population / 2; i++)
                {
                    // Mutate the best half from the last generation
                    nets[i] = new NeuralNetwork(nets[i + ((population) / 2)], worldState);
                    nets[i].Mutate();

                    // Copy the best half from the last generation
                    nets[i + ((population) / 2)] = new NeuralNetwork(nets[i + ((population) / 2)], worldState);
                }

                // Set all fitnesses to 0 since we copied some networks
                for (int i = 0; i < population; i++)
                {
                    nets[i].SetFitness(0f);
                }

                // Destroy golf balls from old generation and create new generation of balls
                CreateNetBalls();

                generation += 1;
            }
        }
    }

    // This function destroys old balls and creates new balls
    private void CreateNetBalls()
    {
        if (netBalls != null)
        {
            for (int i = 0; i < netBalls.Count; i++)
            {
                Destroy(netBalls[i].gameObject);
            }

        }

        netBalls = new List<GameObject>();

        for (int i = 0; i < population; i++)
        {
            GameObject newNetBall = Instantiate(netBall, new Vector3(-14.75f, -7.75f, 0), new Quaternion(0, 0, 0, 1));
            newNetBall.GetComponent<NetGolfBallController>().Init(nets[i], this);
            netBalls.Add(newNetBall);
        }

        netBalls[population-1].GetComponent<SpriteRenderer>().color = Color.red;
        netBalls[population - 1].GetComponent<SpriteRenderer>().sortingOrder = 3;
        netBalls[population - 1].AddComponent<LineRenderer>();
        LineRenderer _lr = netBalls[population - 1].GetComponent<LineRenderer>();
        netBalls[population - 1].AddComponent<TracePath>();

    }

    // This function looks at the tilemap and parses the tile information into a one dimensional array to input into the neural network. It gets information
    // about where the blocks are as well as the goal since that information is static for each level.
    public void parseWorld()
    {
        BoundsInt bounds = _tilemap.cellBounds;
        TileBase[] allTiles = _tilemap.GetTilesBlock(bounds);

        for (int x = 0; x < 30; x++)
        {
            for (int y = 0; y < bounds.size.y; y++)
            {
                TileBase tile = allTiles[x + y * bounds.size.x];
                if (tile != null && tile.name == "BlackSquare")
                {
                    worldState[(x * 16) + y + 2] = 1;
                }
                else if (tile != null && tile.name == "Goal")
                {
                    worldState[0] = x;
                    worldState[1] = y;

                    worldState[(x * 16) + y + 2] = 0;
                }
                else
                {
                    worldState[(x * 16) + y + 2] = 0;
                }
            }
        }

        Vector3 goalInLocal = _tilemap.GetCellCenterWorld(new Vector3Int(worldState[0], worldState[1], 0));
        Vector3 goalInWorld = goalInLocal + _tilemap.origin;

        goalPosX = goalInWorld.x;
        goalPosY = goalInWorld.y;
    }

    public void ManualTrainSaveBest()
    {
        CurrentBestNeuralNetwork.bestNet = new NeuralNetwork(nets[population - 1], worldState);
        putText.text = "Best Fitness: " + bestFitness.ToString();
        victoryScreen.SetActive(true);
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;
        Time.timeScale = 0f;
    }

    public void AutoTrainAllSaveBest()
    {
        CurrentBestNeuralNetwork.generations.Add(generation);

        if (CurrentBestNeuralNetwork.generations.Count % 18 == 0)
        {
            string path = "Assets/Resources/test.txt";
            File.WriteAllText(path, string.Empty);

            StreamWriter writer = new StreamWriter(path, true);
            for (int j = 0; j < CurrentBestNeuralNetwork.generations.Count / 18; j++)
            {
                string line = string.Empty;
                for (int k = 0; k < 18; k++)
                {
                    line += CurrentBestNeuralNetwork.generations[k + 18 * j].ToString() + ",";
                }
                writer.WriteLine(line.Substring(0, line.Length - 1));
            }
            writer.Close();
        }

        CurrentBestNeuralNetwork.bestNet = new NeuralNetwork(nets[population - 1], worldState);
        string fullName = SceneManager.GetActiveScene().name;
        int length = fullName.Length;

        char _char = fullName[length - 1];
        int i = 1;
        while (_char != ' ')
        {
            i++;
            _char = fullName[length - i];
        }
        string levelIndex = fullName.Substring(length - i + 1);


        if (levelIndex == "18")
        {
            levelIndex = "1";
        }

        string sceneName = "Neural Network Level " + (Int32.Parse(levelIndex)+1).ToString();

        if (Application.CanStreamedLevelBeLoaded(sceneName))
        {
            SceneManager.LoadSceneAsync(sceneName);
        }
        else
        {
            SceneManager.LoadSceneAsync("Empty Level");
        }
    }

    public void AutoTrainAllForgetBest()
    {
        CurrentBestNeuralNetwork.generations.Add(generation);

        if (CurrentBestNeuralNetwork.generations.Count % 18 == 0)
        {
            string path = "Assets/Resources/test.txt";
            File.WriteAllText(path, string.Empty);

            StreamWriter writer = new StreamWriter(path, true);
            for (int j = 0; j < CurrentBestNeuralNetwork.generations.Count/18; j++)
            {
                string line = string.Empty;
                for (int k = 0; k < 18; k++)
                {
                    line += CurrentBestNeuralNetwork.generations[k+18*j].ToString() + ",";
                }
                writer.WriteLine(line.Substring(0, line.Length - 1));
            }
            writer.Close();
        }

        string fullName = SceneManager.GetActiveScene().name;
        int length = fullName.Length;

        char _char = fullName[length - 1];
        int i = 1;
        while (_char != ' ')
        {
            i++;
            _char = fullName[length - i];
        }
        string levelIndex = fullName.Substring(length - i + 1);


        if (levelIndex == "18")
        {
            levelIndex = "1";
        }

        string sceneName = "Neural Network Level " + (Int32.Parse(levelIndex) + 1).ToString();

        if (Application.CanStreamedLevelBeLoaded(sceneName))
        {
            SceneManager.LoadSceneAsync(sceneName);
        }
        else
        {
            SceneManager.LoadSceneAsync("Empty Level");
        }
    }
    public void AutoTrainForgetBest()
    {
        CurrentBestNeuralNetwork.generations.Add(generation);

        string path = "Assets/Resources/test.txt";
        File.WriteAllText(path, string.Empty);

        StreamWriter writer = new StreamWriter(path, true);

        for(int i = 0; i < CurrentBestNeuralNetwork.generations.Count; i++)
        {
            writer.WriteLine(CurrentBestNeuralNetwork.generations[i]);
        }
        writer.Close();

        if (Application.CanStreamedLevelBeLoaded(SceneManager.GetActiveScene().name))
        {
            SceneManager.LoadSceneAsync(SceneManager.GetActiveScene().name);
        }
        else
        {
            SceneManager.LoadSceneAsync("Empty Level");
        }
    }
}

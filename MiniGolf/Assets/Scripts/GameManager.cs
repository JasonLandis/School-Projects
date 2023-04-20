using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using UnityEngine.Tilemaps;

public class GameManager : MonoBehaviour
{
    [Header("Victory Screen Information")]
    public TextMeshProUGUI timesHitText; // Text to display the number of times the player has hit the ball
    public TextMeshProUGUI victoryText; // Text to display the victory message on the victory screen
    public TextMeshProUGUI putText; // Text to display the number of puts on the victory screen
    public GameObject victoryScreen; // The victory screen object
    [Space(10)]

    [Header("Game Information")]
    public GolfBallController golfBallController; // Reference to the golf ball controller
    public GameObject golfBall; // Reference to the golf ball
    public Tilemap tilemap; // Reference to the tilemap
    public TileBase holeTile; // Reference to the hole tile

    void Start() 
    {
        Cursor.visible = false; // Hide the cursor
    }

    void Update() // called once per frame
    {
        // Updates the times hit text every time the player hits the ball
        timesHitText.text = "Puts: " + golfBallController.timesHit.ToString();

        // Check if the ball is in the hole
        if (tilemap.GetTile(tilemap.WorldToCell(golfBall.transform.position)) == holeTile)
        {
            // Check if the golf ball is not moving
            if (golfBall.GetComponent<Rigidbody2D>().velocity.magnitude < 0.1f)
            {
                // Show the victory screen
                victoryScreen.SetActive(true);
                Cursor.lockState = CursorLockMode.None;
                Cursor.visible = true;
                if (golfBallController.timesHit == 1) 
                {
                    victoryText.text = "Hole in one!"; // If player got hole in one
                } else 
                {
                    victoryText.text = "Victory!"; // else
                }

                // Creates variable to display the number of puts
                putText.text = "Puts: " + golfBallController.timesHit.ToString();
                golfBallController.enabled = false; // Disable the golf ball controller
            }
        }
    }
}
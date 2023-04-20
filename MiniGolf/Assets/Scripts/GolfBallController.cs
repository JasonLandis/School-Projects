using UnityEngine;
using System.Collections;

public class GolfBallController : MonoBehaviour
{
    [Header("Ball Information")]
    public float angle = 90.0f; // The angle of the ball
    float radianAngle; // The angle of the ball in radians
    public float power = 1.0f; // The power of the ball
    float powerIncrement = 0.1f; // The amount to increment the power by
    float angleIncrement = 0.1f; // The amount to increment the angle by
    float maxAngle = 180.0f;
    float minAngle = 0.0f;
    float maxPower = 1000.0f;
    float minPower = 0.0f;
    public float linearDrag = 0.3f; // The linear drag of the ball
    public int timesHit = 0; // The number of times the ball has been hit
    LineRenderer lr; // Reference to the line renderer
    public int resolution = 10; // The resolution of the line renderer
    float g; // The gravity of the ball

    private void Awake()
    {
        lr = GetComponent<LineRenderer>(); // Get the line renderer
        g = Mathf.Abs(Physics2D.gravity.y); // Get the gravity
    }

    void RenderArc() // Renders the arc of the ball
    {
        lr.positionCount = resolution + 1; // Set the position count of the line renderer
        lr.SetPositions(CalculateArcArray()); // Set the positions of the line renderer
    }

    Vector3[] CalculateArcArray() // Calculate arc of the ball
    {
        Vector3[] arcArray = new Vector3[resolution + 1]; // Create an array of vectors

        radianAngle = Mathf.Deg2Rad * angle; // Convert the angle to radians
        
        float velocity = power * (1 - linearDrag); // apply the linear drag to the power

        float maxDistance = (velocity * velocity * Mathf.Sin(2 * radianAngle)) / g; // calculate the maxDistance of the ball

        for (int i = 0; i <= resolution; i++) // Loop through the resolution
        {
            float t = (float)i / (float)resolution; // Calculate the time
            arcArray[i] = CalculateArcPoint(t, maxDistance); // Calculate the arc point
        }

        for (int i = 0; i < arcArray.Length; i++) // Loop through the arc array
        {
            arcArray[i] = new Vector3(arcArray[i].x + transform.position.x, arcArray[i].y + transform.position.y, 0); // Set the position of the arc array
        }

        // remove the last 10 points of the arc from the array
        Vector3[] arcArray2 = new Vector3[arcArray.Length - 10];

        for (int i = 0; i < arcArray2.Length; i++) // Loop through arc array 
        {
            arcArray2[i] = arcArray[i];
        }

        lr.positionCount = resolution - 10; // Set the position count of the line renderer
        return arcArray2; // Return the arc array
    }

    Vector3 CalculateArcPoint(float t, float maxDistance) // Calculate the arc point
    {
        float x = t * maxDistance; // Calculate the x position
        float y = x * Mathf.Tan(radianAngle) - ((g * x * x) / (2 * power * power * Mathf.Cos(radianAngle) * Mathf.Cos(radianAngle))); // Calculate the y position
        return new Vector3(x, y); // Return the position
    }

    void Update()
    {
        if (GetComponent<Rigidbody2D>() != null) {
            if (GetComponent<Rigidbody2D>().velocity.magnitude == 0) // if ball is not moving
            {
                RenderArc();
            }
            else
            {
                lr.positionCount = 0;
            }
        }

        if (Input.GetKey(KeyCode.RightArrow))
        {
            // change the angle of the ball to the left
            if (angle > minAngle)
            {                
                angle -= angleIncrement;
            }
        }

        if (Input.GetKey(KeyCode.LeftArrow))
        {
            // change the angle of the ball to the right
            if (angle < maxAngle)
            {
                angle += angleIncrement;
            }            
        }

        if (Input.GetKey(KeyCode.UpArrow))
        {
            // increase the power to be applied to the ball
            if (power < maxPower)
            {
                power += powerIncrement;
            }            
        }
        
        if (Input.GetKey(KeyCode.DownArrow))
        {
            // decrease the power to be applied to the ball
            if (power > minPower)
            {
                power -= powerIncrement;
            }          
        }

        // if - is pressed slow down time
        if (Input.GetKeyDown(KeyCode.J))
        {
            Time.timeScale = Time.timeScale / 2;
        }

        // if = is pressed speed up time
        if (Input.GetKeyDown(KeyCode.L))
        {
            Time.timeScale = Time.timeScale * 2;
        }

        if (Input.GetKeyDown(KeyCode.Space))
        {
            timesHit++;
            
            Time.timeScale = 1.0f;
            // apply a force to the ball that is equal to the angle and power
            if (GetComponent<Rigidbody2D>() != null)
            {                
                radianAngle = Mathf.Deg2Rad * angle;
                GetComponent<Rigidbody2D>().AddForce(new Vector2(Mathf.Cos(radianAngle), Mathf.Sin(radianAngle)) * power, ForceMode2D.Impulse);
            }
        }
    }
}

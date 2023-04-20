using UnityEngine;

public class RandomGolfBall : MonoBehaviour
{
    public Camera Camera;

    void Update()
    {
        if (Time.time % 0.81632653f < 0.01f) // play audio to beat of audio
        {
            Vector2 direction = new Vector2(Random.Range(-1.0f, 1.0f), Random.Range(-1.0f, 1.0f));
            GetComponent<Rigidbody2D>().AddForce(direction * 5000);
        }
    }
}
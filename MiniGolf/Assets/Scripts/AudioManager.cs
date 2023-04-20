using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class AudioManager : MonoBehaviour
{
    public AudioSource audioSource;

    void Awake()
    {
        audioSource.Play(); // play audio
        DontDestroyOnLoad(audioSource); // dont destroy audio
    }

    void Update()
    {
        // if the scene name is MainMenu, destroy the audio
        if (SceneManager.GetActiveScene().name == "MainMenu")
        {
            Destroy(audioSource);
        }
    }  
}

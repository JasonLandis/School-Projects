using System.Collections;
using System.Collections.Generic;
using TMPro;
using TMPro.EditorUtilities;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UIElements;

public class Level : MonoBehaviour
{
    public TMP_Text _text;
    public string fullName;
    public string levelIndex;
    void Awake()
    {
        fullName = SceneManager.GetActiveScene().name;
        int length = fullName.Length;
        
        char _char = fullName[length - 1];
        int i = 1;
        while (_char != ' ')
        {
            i++;
            _char = fullName[length - i];
        }
        levelIndex = fullName.Substring(length - i);

        _text = GetComponent<TMP_Text>();
    }

    private void Update()
    {
        _text.text = "Level " + levelIndex;
    }




}

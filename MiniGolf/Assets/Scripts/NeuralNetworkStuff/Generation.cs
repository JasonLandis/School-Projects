using System.Collections;
using System.Collections.Generic;
using TMPro;
using TMPro.EditorUtilities;
using UnityEngine;

public class Generation : MonoBehaviour
{
    public GameObject _netManagerObject;
    public NetManager _netManager;
    public TMP_Text _text;
    void Awake()
    {
        _netManagerObject = GameObject.Find("NetManager");
        _netManager = _netManagerObject.GetComponent<NetManager>(); 
        _text = GetComponent<TMP_Text>();   
    }

    private void Update()
    {
        _text.text = "Generation: " + _netManager.generation.ToString();
    }




}

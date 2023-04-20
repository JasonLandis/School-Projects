using System.Collections;
using System.Collections.Generic;
using TMPro;
using TMPro.EditorUtilities;
using UnityEngine;

public class Fitness : MonoBehaviour
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
        _text.text = "Best Fitness: " + _netManager.bestFitness.ToString() + "\nWorst Fitness: " 
            + _netManager.worstFitness.ToString();
    }




}

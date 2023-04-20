using Newtonsoft.Json.Bson;
using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.Tilemaps;

[ExecuteInEditMode]
public class CompressBounds : MonoBehaviour
{
    public Tilemap _tilemap;

    private void Awake()
    {
        _tilemap = GetComponent<Tilemap>();
    }
    void Update()
    {
        _tilemap.CompressBounds();
    }
}



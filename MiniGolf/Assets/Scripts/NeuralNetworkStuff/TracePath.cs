using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

public class TracePath : MonoBehaviour
{
    public LineRenderer _lr;
    public int maxLength = 1500;
    public Queue<Vector3> points;
    

    // Start is called before the first frame update
    private void Awake()
    {
        _lr = GetComponent<LineRenderer>();
        _lr.positionCount = maxLength;
        _lr.startColor = Color.red;
        _lr.endColor = Color.red;
        _lr.startWidth = 0.1f;
        _lr.endWidth = 0.1f;
        _lr.sortingOrder = 3;
        _lr.material = (Material)Resources.Load("ArcLine");
        points = new Queue<Vector3>(Enumerable.Repeat(transform.position, 1500).ToArray());
        _lr.SetPositions(Enumerable.Repeat(transform.position, 1500).ToArray());
    }

    // Update is called once per frame
    void Update()
    {
        if(points.Count >= maxLength)
        {
            points.Dequeue();
        }
        points.Enqueue(transform.position);
        _lr.SetPositions(points.ToArray());
    }
}

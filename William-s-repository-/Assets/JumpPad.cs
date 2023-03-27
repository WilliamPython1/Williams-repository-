using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class JumpPad : MonoBehaviour
{
    PlayerMovement playerMovement;
    public GameObject player;

    void Awake()
    {
        playerMovement = GameObject.Find("Player").GetComponent<PlayerMovement>();
    }
    void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "JumpPad")
        {
            playerMovement.jumpHeight = 48f;
        }
    }

    void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "JumpPad")
        {
            playerMovement.jumpHeight = 16f;
        }
    }
}
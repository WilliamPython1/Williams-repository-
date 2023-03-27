using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class PlayerMovement : MonoBehaviour
{
    public Rigidbody2D rb2D;
    public float moveSpeed;
    public float jumpHeight;
    public bool midJump;
    public float moveHorizontal;
    public float moveVertical;

    void Start()
    {
        rb2D = gameObject.GetComponent<Rigidbody2D>();
        moveSpeed = 1f;
        jumpHeight = 16f;
        midJump = false;
    }

    void Update()
    {
        moveHorizontal = Input.GetAxisRaw("Horizontal");
        moveVertical = Input.GetAxisRaw("Vertical");
    }

    void FixedUpdate()
    {

        if (moveHorizontal > 0.1f || moveHorizontal < -0.1f)
        {
            rb2D.AddForce(new Vector2(moveHorizontal*moveSpeed, 0f), ForceMode2D.Impulse);
        }
        
        if (!midJump && moveVertical > 0.1f)
        {
            rb2D.AddForce(new Vector2(0f, moveVertical*jumpHeight), ForceMode2D.Impulse);
        }
    }
    
    void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "Ground")
        {
            midJump = false;
        }
    }

    void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "Ground")
        {
            midJump = true;
        }
    }




}

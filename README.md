# Battling Knights

There	are	four	knights	who	are	about	to	do	battle.

    RED (R)
    BLUE (B)
    GREEN (G)
    YELLOW (Y)

<br/>

**Each	knight	starts	in	one	corner	of	the	board.**
    
    R (0,0) (top left)
    B (7,0) (bottom left)
    G (7,7) (bottom right)
    Y (0,7) (top right)

### Items

<br/>Around the board are the following four Items and Positons:

`Axe         (A) (2,2):  +2 Attack`  
`Dagger      (D) (2,5):  +1 Attack`  
`Helmet      (H) (5,2):  +1 Defense`  
`MagicStaff  (M) (5,5):  +1 Attack, +1 Defense`  


### Movement

<br/>Each Knight moves one tile at a time in one of four directions.<br/>

`North (N)  (UP)`  
`East  (E)  (RIGHT)`  
`South (S)  (DOWN)`  
`West  (W)  (LEFT)`  


### Fighting

<br/>Each Knight has a base attack and defense score of 1:

`Attack  (1)`  
`Defense (1)`  


# Usage

To run the app:

    python app.py

To run the test:

    python test.py

Instructions are read in from `movements.txt`.

Final result of arena is written to `result.json`.

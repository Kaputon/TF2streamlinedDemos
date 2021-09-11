# TF2streamlinedDemos


The purpose of this program is to parse your events.txt file, gather your bookmarked events, and sort them under their respective demo.

When ran, the program will gather the demo file names and bookmarked timestamps as it progresses, sorting them, and eventually placing them into a new file.
Along with this, it will place a new timestamp beside the original with 3000 ticks reduced, to provide for easier demo viewing.


# File Format: 
Below is an example of what a block in a new Demo file might look like.

```
-----------]]

2021-09-02_17-20-38 - Demo filename

-TICKS
50669 ; 47669  (Original tick and modified one)
68343 ; 65343
...etc

-----------]]
```

# AI-search-algorithms

## Descreption:

The program receives two points as the origin and destination and can display the route leading from origin to destination in three ways [DFS](https://github.com/abbaspouramini/AI-search-algorithms/edit/main/README.md#depth-first-search), bFS, and A*.

The interface is designed using PyQt5.



## Depth First Search:
The algorithm moves in any node with this priority.
#### 1.Up
#### 2.Right
#### 3.Down
#### 4.Left

in each node first we check the up of node . if the direction up is not an obstacle, we will move in this direction.if there was an obstacle, it would review the next priority and continue to do so.


```python
def DFS(self,Current,Goal):
        Neighbors=FindNeighbor(Current,"Without From")


        current=FindButton(Current)
        current.status="visited"
        up = FindButton(Neighbors[0])
        right = FindButton(Neighbors[1])
        bottom = FindButton(Neighbors[2])
        left = FindButton(Neighbors[3])
        w.NodeCount+=1
        if Goal==Current:
            return 1
        if current.color!="red":
            ColorizeButton(current,"Pink")
            sleep_program()
        if up!=0 :
            if up.color!= "black" and up.status!= "visited":
                NextNode=[Current[0]-1,Current[1]]

                if self.DFS(NextNode,Goal) :
                    if current.color != "red":
                        self.stack.Push(current)
                    return 1

        if right!=0 :
            if right.color!= "black" and right.status!= "visited":
                NextNode=[Current[0],Current[1]+1]

                if self.DFS(NextNode,Goal) :
                    if current.color != "red":
                        self.stack.Push(current)
                    return 1
                            if bottom!=0 :
            if bottom.color!= "black" and bottom.status!= "visited":
                NextNode=[Current[0]+1,Current[1]]

                if self.DFS(NextNode,Goal) :
                    if current.color != "red":
                        self.stack.Push(current)
                    return 1
        if left!=0 :
            if left.color!= "black" and left.status!= "visited":
                NextNode=[Current[0],Current[1]-1]

                if self.DFS(NextNode,Goal) :
                    if current.color!="red":
                        self.stack.Push(current)
                    return 1
        if current.color!="red":
            ColorizeButton(current,"Pink")
            sleep_program()
```


## Bredth First Search:


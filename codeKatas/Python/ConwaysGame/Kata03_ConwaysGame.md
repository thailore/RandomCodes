## The Exercise
#### Focus: to practice the TDD, red green refactor flow.

#### The red green refactor steps:
* Write a unit test that fails.
* Update code to make tests pass.
* Clean up, refactor.

#### Hints:
Unlike in the string calculator exercise, the steps are not clearly set out for you here. Nonetheless, break your problem into the smallest, simplest steps and always keep in mind the focus of the red-green-refactor. A possible set of starting steps, as well as some examples can be found below

## The Problem
The world of the Game of Life is grid of cells (2d array). Each cell can be either 'dead' or 'alive'. Each cell has up to eight neighbors as seen below (each cell O is a neighbor of cell X):  
	
~~~~
   O O O
   O X O
   O O O
~~~~

The initial setup of the grid (which cells are dead and alive) can be hardcoded at first for testing purposes. Going forward this can be generated on a seed.

After the board is generated you iterate over x generations, simultaneously applying the following rules to each cell on the grid for each generation:

 * Any live cell with fewer than two live neighbours dies, as if caused by under-population.
 * Any live cell with two or three live neighbours lives on to the next generation.
 * Any live cell with more than three live neighbours dies, as if by overcrowding.
 * Any dead cell with exactly three live neighbours becomes a live cell.

### A potential breakdown of steps:
1. create world of defined dimensions with `world = World.create(width=5, height=10)`
2. set and report on cell state in the world with `world.bringToLife(x,y):void` and `world.areYouAlive(x,y):boolean`
3. get the number of living neighbors for a cell with `numberOfLivingNeighbors(x,y):int`
4. create simple 2 generation steps for a small grid (e.g see that the living and dead cells change as expected for simple test cases)
5. ... 

### Some test cases
~~~~
  O = dead
  X = alive
 
   O O O      O O O
   O X O  =>  O O O         (cell dies as it had no living neighbors)
   O O O      O O O

   O X O      O X X
   O X X  =>  O X X         (corner cell had enough neighbors to spawn)
   O O O      O O O

   O X O      X X X
   X X X  =>  X O X         (middle cell died from overcrowding)
   O X O      X X X
~~~~

## References
 * https://bitstorm.org/gameoflife/

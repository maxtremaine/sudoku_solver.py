# sudoku_solver
Solves Sudoku puzzles so I don't have to.

## To-Do
- [ ] Add a to_file method to Puzzle.
- [x] Parallelize working_conditions level.
- [x] Make the initializer generic.
- [x] Make the generator take file input.
- [x] Create a Cell class.
- [x] Create a freedom generation method and add to instantiation.
- [x] Create a sorting mechanism by freedom.
- [x] Create a filtering mechanism by blanks.

## Scripts

### Test and Type Check

```sh
python3 -m mypy . && python3 -m unittest
```

### Run

```sh
python3 .
```
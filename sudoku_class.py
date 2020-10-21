import numpy as np
import pandas as pd
import os

class Sudoku:
    def __init__(self, csvfile):
        puzzle_folder="puzzle_csvs"
        self.csvfile=csvfile
        thepath=os.path.join(puzzle_folder, self.csvfile)
        puzzle_csv_df=pd.read_csv(thepath)

        # Replace zeros with np.nan because zeros act as placeholders.
        puzzle_np=puzzle_csv_df.to_numpy()
        

        print(puzzle_np)
        self.puzzle_np =puzzle_np
        return 

    def make_blocks2d(self):
        puzzle_np=self.puzzle_np
        chunks=[np.vsplit(sub, 3) for sub in np.hsplit(puzzle_np, 3)]

        return chunks



theSudoku=Sudoku("s1.csv")

chunks=theSudoku.make_blocks2d()
for x in range (0, 3):
    for y in range (0, 3):
        print(chunks[x][y])




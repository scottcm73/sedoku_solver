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
        puzzle_np=puzzle_np.astype("float")
        puzzle_np[puzzle_np == 0] = np.nan

        print(puzzle_np)

        return 




theSudoku=Sudoku("s1.csv")


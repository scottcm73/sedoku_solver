import numpy as np
import pandas as pd
import os

class Sudoku:
    def __init__(self, csvfile):
        puzzle_folder="puzzle_csvs"
        self.csvfile=csvfile
        thepath=os.path.join(puzzle_folder, self.csvfile)
        puzzle_csv_df=pd.read_csv(thepath)
        puzzle_np=puzzle_csv_df.to_numpy()
        print(puzzle_np)
        self.puzzle_np =puzzle_np
        return 

    def make_blocks2d(self):
        puzzle_np=self.puzzle_np
        chunks=[np.vsplit(sub, 3) for sub in np.hsplit(puzzle_np, 3)]
        self.chunks=chunks
        return chunks

    def make_rows(self):
        puzzle_np=self.puzzle_np
        the_rows=np.vsplit(puzzle_np, 9)
        self.the_rows=the_rows
        return the_rows # list of 9 rows

    def make_cols(self):
        puzzle_np=self.puzzle_np
        the_cols=np.hsplit(puzzle_np, 9)
        self.the_cols=the_cols
        return the_cols # list of 9 cols


    def check_solved(self):
        puzzle_np=self.puzzle_np
        solved=True

        
        # if 0 in puzzle_np:
        #     solved=False
        #     return solved

        the_base_list=[1,2,3,4,5,6,7,8,9]
        # chunks=self.make_blocks2d()
        # for x in range (0, 3):
        #     for y in range (0, 3):
        #         flattened_chunk=chunks[x][y].flatten()
        #         # To be true, each flattened_chunk must contain all elements in the base array in any order.
        #         result =  all(elem in flattened_chunk for elem in the_base_list)
        #         if result == False:
        #             solved = False
        #             return solved
        
        
        the_cols=self.make_cols()
        
        for single_col in the_cols:
           
            
            print("single")
            print(single_col)
            # result =  all(elem in single_col for elem in the_base_list)
            # if result == False:
            #     solved = False
            #     return solved



        the_rows=self.make_rows()



       

        self.solved=solved
        return self.solved


theSudoku=Sudoku("s1.csv")


solved=theSudoku.check_solved()
print(solved)





import numpy as np
import pandas as pd
import os
import copy

class Sudoku:
    def __init__(self, csvfile):
        puzzle_folder="puzzle_csvs"
        self.csvfile=csvfile
        thepath=os.path.join(puzzle_folder, self.csvfile)
        puzzle_csv_df=pd.read_csv(thepath)
        puzzle_np=puzzle_csv_df.to_numpy()
        print(puzzle_np)
        self.puzzle_np =puzzle_np
        #Make copy of puzzle that can be changed.
        self.puzzle_copy=puzzle_np
        self.check_solved()
        return 

    def make_blocks2d(self):
        puzzle_copy=self.puzzle_copy
        chunks=[np.vsplit(sub, 3) for sub in np.hsplit(puzzle_copy, 3)]
        self.chunks=chunks
        return chunks

    def make_rows(self):
        puzzle_copy=self.puzzle_copy
        the_rows=np.vsplit(puzzle_copy, 9)
        self.the_rows=the_rows
        return the_rows # list of 9 rows

    def make_cols(self):
        puzzle_copy=self.puzzle_copy
        the_cols=np.hsplit(puzzle_copy, 9)
        self.the_cols=the_cols
        return the_cols # list of 9 cols


    def check_solved(self):
        puzzle_copy=self.puzzle_copy
        solved=True
        self.solved=solved
        
        if 0 in puzzle_copy:
            solved=False
            self.solved=solved


        the_base_list=[1,2,3,4,5,6,7,8,9]
        self.the_base_list=the_base_list
        chunks=self.make_blocks2d()
        for x in range (0, 3):
            for y in range (0, 3):
                flattened_chunk=chunks[x][y].flatten()
                # To be true, each flattened_chunk must contain all elements in the base array in any order.
                result =  all(elem in flattened_chunk for elem in the_base_list)
                if result == False:
                    solved = False
                    self.solved=solved

        
        the_cols=self.make_cols()
        for single_col in the_cols:         
            print("single")
            print(single_col)
            # Check if all 1-9 in a column without repeats.
            result =  all(elem in single_col for elem in the_base_list)
            if result == False:
                solved = False
                self.solved=solved


        the_rows=self.make_rows()
        for single_row in the_rows:
            print("single")
            print(single_row)
            # Check if all 1-9 in a row without repeats.
            result =  all(elem in single_row for elem in the_base_list)
            if result == False:
                solved = False
                self.solved=solved


        self.solved=solved
        if self.solved==False:
            self.solver()
        else:
            return self.solved

    def solver(self):
       
        #Make copy of the original puzzle that can be changed.
        puzzle_copy=self.puzzle_copy
        the_base_list=self.the_base_list
        the_rows=self.the_rows
        the_cols=self.the_cols
        chunks=self.chunks
        rows=[l.tolist() for l in the_rows]
        
        rows_copy=rows

        for row in rows_copy:
            # Removes 1 set of brackets to return a simple list
            the_row=row[0]
            new_row=list(filter(lambda a: a != 0, the_row))
         
      
        
            
     
            remaining_nums=[x for x in the_base_list if x not in new_row]
            print("remaining")
            print(remaining_nums)






        return


theSudoku=Sudoku("s1.csv")

print(theSudoku.solved)







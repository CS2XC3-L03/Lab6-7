import rbt as r
import bst as b
import random


# ------------------------- Helper Funcs --------------------------------
def create_random_list(length, max_val):
    return [random.randint(0, max_val) for _ in range(length)]


# ------------------------- Experiment 1 -------------------------------
def expt1(list_size, max_value):
    rbt_heights = []
    bst_heights = []
    trial_num = 80
    
    for _ in range(trial_num):
        lst = create_random_list(list_size, max_value)
        rbt = r.RBTree()
        bst = b.BSTree()
        
        for i in lst:
            rbt.insert(i)
            bst.insert(i)
        
        rbt_heights.append(rbt.get_height())
        bst_heights.append(bst.get_height())
    
    avg_rbt_height = sum(rbt_heights) / trial_num
    avg_bst_height = sum(bst_heights) / trial_num
    
    print(f"Average RBT height: {avg_rbt_height}")
    print(f"Average BST height: {avg_bst_height}")
    print(f"Average difference (avg_bst_height - avg_rbt_height): {avg_bst_height - avg_rbt_height}")


# ---------------------------  Tests ----------------------------------

expt1(10000, 10000) #large size with unique values
expt1(10000, 30) #large size with similar values
expt1(10, 10000) #small size with unique values
expt1(10, 2) #small size with unique values

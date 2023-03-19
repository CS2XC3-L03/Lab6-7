import rbt as r
import bst as b
import random
import matplotlib.pyplot as plot


# ------------------------- Helper Funcs --------------------------------
def create_random_list(length, max_val):
    return [random.randint(0, max_val) for _ in range(length)]

def create_near_sorted_list(length, max_val, swaps_num):
    lst = create_random_list(length, max_val)
    lst.sort()

    near_sorted_list = random_swap(lst, swaps_num)

    return near_sorted_list

def random_swap(lst, swaps_num):
    for _ in range(swaps_num):
        random_index_1 = random.randint(0, len(lst) - 1)
        random_index_2 = random.randint(0, len(lst) - 1)
        lst[random_index_1], lst[random_index_2] = lst[random_index_2], lst[random_index_1]
    return lst



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
    
# ------------------------- Experiment 2 -------------------------------
def expt2_dataCollection(list_size, max_val):
    DATASET = []

    BST_RBT_avg_height_dataset = [[], []]
    avg_height_diff_dataset = []

    max_swaps = list_size * 4
    trial_num = 20

    for swaps_num in range(max_swaps):
        rbt_heights = []
        bst_heights = []
        for _ in range(trial_num):
            lst = create_near_sorted_list(list_size, max_val, swaps_num)
            rbt = r.RBTree()
            bst = b.BSTree()
            
            for i in lst:
                rbt.insert(i)
                bst.insert(i)
        
        rbt_heights.append(rbt.get_height())
        bst_heights.append(bst.get_height())
    
        avg_rbt_height = sum(rbt_heights) / trial_num
        avg_bst_height = sum(bst_heights) / trial_num

        BST_RBT_avg_height_dataset[0].append(avg_rbt_height)
        BST_RBT_avg_height_dataset[1].append(avg_bst_height)

        avg_height_diff = avg_bst_height - avg_rbt_height

        avg_height_diff_dataset.append(avg_height_diff)

    DATASET = [BST_RBT_avg_height_dataset, avg_height_diff_dataset]

    return DATASET


def expt2_graphing(dataset):
    BST_RBT_avg_height_dataset = dataset[0]

    plot.plot(BST_RBT_avg_height_dataset[0], label = "RBT")
    plot.plot(BST_RBT_avg_height_dataset[1], label = "BST")
    plot.legend()
    plot.title("Number of Swaps vs Average Height of RBT & BST")
    plot.xlabel("Number of Swaps")
    plot.ylabel("Average Height")
    plot.show()

    avg_height_diff_dataset = dataset[1]

    plot.plot(avg_height_diff_dataset)
    plot.legend()
    plot.title("Number of Swaps vs Difference in Avg Height of RBT & BST")
    plot.xlabel("Number of Swaps")
    plot.ylabel("Difference in Avg Height (BST - RBT)")
    plot.show()


# ---------------------------  Expt1 Tests ----------------------------------

# I think I'd prefer a BST over an RBT with experiment of small sized lists. For example: expt1(10, 100)
print("-----------------expt1(10000, 10000)---------------------")
expt1(10000, 10000) #large size with unique values
print("---------------------------------------------------------")
print()
print("-----------------expt1(10000, 30)------------------------")
expt1(10000, 30) #large size with similar values
print("---------------------------------------------------------")
print()
print("-----------------expt1(10, 10000)------------------------")
expt1(10, 10000) #small size with unique values
print("---------------------------------------------------------")
print()
print("-----------------expt1(10, 2)----------------------------")
expt1(10, 2) #small size with unique values
print("---------------------------------------------------------")
print()

# ---------------------------  Expt2 Tests ------------------------------------

dataset = expt2_dataCollection(100, 100)
expt2_graphing(dataset)

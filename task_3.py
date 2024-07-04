import numpy as np
import random
import multiprocessing
import math
import time

def random_init(queen_nums, board, queen_pos):
    nums = 0
    while True:
        if nums == queen_nums:
            break
        r = random.randint(0,queen_nums-1)
        c = random.randint(0,queen_nums-1)
        if board[r][c] != 1:
            board[r][c] = 1
            queen_pos.append([r,c])
            nums += 1
        else:
            continue
    return queen_pos

def if_confict(queen_1, queen_2):
    if queen_1[0] == queen_2[0] or queen_1[1] == queen_2[1]:
        return True
    elif abs(queen_1[0]-queen_2[0]) == abs(queen_1[1]-queen_2[1]):
        return True
    else:
        return False

def compute_confict(queen_pos):
    conflict_socre = 0
    pos = queen_pos[:]
    while len(pos) != 0:
        queen = pos.pop()
        for item in pos:
            if if_confict(item,queen):
                conflict_socre += 1
            else:
                continue
    return conflict_socre

def repeat_detected(lst, value):
    repeated = False
    for i in range(len(lst)):
        if value == lst[i]:
            repeated = True
    return repeated

def next_state(queen_pos):
    state_list = []
    for i in range(len(queen_pos)):
        for j in range(len(queen_pos)):
            for k in range(len(queen_pos)):
                pos = queen_pos[:]
                if repeat_detected(pos, [j,k]):
                    continue
                else:
                    # print(pos)
                    pos[i]=[j,k]
                    state_list.append(pos)
    return state_list

def probability_function(score):
    prob = math.exp(-score)
    return prob

def random_beam_search(k_head,queen_nums):
    init_state = []
    steps = 0
    for i in range(queen_nums):
        queen_pos = []
        board = np.zeros((queen_nums,queen_nums),dtype=int)
        queen_pos = random_init(queen_nums,board,queen_pos)
        init_state.append(queen_pos)
    while True:
        print(steps)
        with multiprocessing.Pool(processes=k_head) as pool:
            results = [pool.apply_async(next_state,args=(init_state[i],)) for i in range(queen_nums)]
            all_next_state = []
            probabilities = []
            pool.close()
            pool.join()
            for result in results:
                for state in result.get():
                    all_next_state.append((compute_confict(state),state))
                    probabilities.append(probability_function(compute_confict(state)))
                    # print(probabilities)
            states = random.choices(all_next_state,probabilities,k=k_head)
            for item in states:
                if item[0] == 0:
                    return item[0], item[1]
            init_state = [states[i][1] for i in range(queen_nums)]
            if steps <= 100:
                steps += 1
            else:
                print(states[0][0],states[0][1])
                return None, None
            
def random_reboot_algorithm(k_head,queen_nums):
    min_score = None
    while True:
        min_score, queen_pos = random_beam_search(k_head,queen_nums)
        if min_score != 0:
            queen_pos = []
            continue
        else:
            break
    return min_score, queen_pos  
            
def main():
    k = 8
    queen_nums = 8
    min_score, queen_pos = random_reboot_algorithm(k,queen_nums)
    board = np.zeros((queen_nums,queen_nums),dtype=int)
    for queen in queen_pos:
        board[queen[0]][queen[1]] = 1
    print(board)
    print(min_score)


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"程序运行时间: {elapsed_time} 秒")            
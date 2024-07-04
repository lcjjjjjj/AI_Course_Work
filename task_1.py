import numpy as np
import random
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
                    pos[i]=[j,k]
                    state_list.append(pos)
    return state_list


def climb_algorithm(queen_nums, queen_pos):
    pos = queen_pos[:]
    steps = 0
    while True:
        print(steps)
        state_list = next_state(pos)
        state_metrics = []
        for i in range(len(state_list)):
            state_metrics.append((compute_confict(state_list[i]),state_list[i]))
        state_metrics = sorted(state_metrics, key = lambda x: x[0])
        if state_metrics[0][0] == 0:
            return state_metrics[0][0], state_metrics[0][1]
        pos = state_metrics[0][1]
        if steps <= 50:
            steps+=1
        else:
            print(state_metrics[0][0], state_metrics[0][1])
            return None, None
    
                    
def random_restart_algorithm(queen_nums,queen_pos):
    min_score = None
    while True:
        board = np.zeros((queen_nums,queen_nums),dtype=int)
        queen_pos = random_init(queen_nums,board,queen_pos)
        min_score, queen_pos = climb_algorithm(queen_nums,queen_pos)
        if min_score != 0:
            queen_pos = []
            continue
        else:
            break
    return min_score, queen_pos
        
def main():
    queen_nums = 8 
    queen_pos = []
    min_score, queen_pos = random_restart_algorithm(queen_nums,queen_pos)
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
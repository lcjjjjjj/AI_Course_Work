import multiprocessing
import random
import math

def task(name):
    print(f'{name} is complete!')
    return 'hello','world'

def test_random_choice():
    elements = ['a', 'b', 'c', 'd']
    probabilities = [0.9, 0.8, 0.2, 0.1]
    results = random.choices(elements, probabilities, k=5)
    print(results)

def probability_function(score):
    prob = math.exp(-score)
    return prob

def main():
    # with multiprocessing.Pool(processes=8) as pool:
    #     results = [pool.apply_async(task, args=(f"{i+1}")) for i in range(8)]
    #     pool.close()
    #     pool.join()
    #     for result in results:
    #         print(result.get())
    # test_random_choice()
    print(probability_function(1))

if __name__ == '__main__':
    main()
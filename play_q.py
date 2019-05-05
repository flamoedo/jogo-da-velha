import sys

import numpy as np

from oxo_q import play_game, check_game


def eps_greedy_q_learning_with_table(num_episodes=500):
    q_table = np.zeros((3,3,3,3,3,3,3,3,3,9))
    y = 0.95
    eps = 0.5
    lr = 0.8
    decay_factor = 0.999
    for i in range(num_episodes):
        s = np.zeros(9).astype(int)
        eps *= decay_factor
        done = False
        chute = 0
        action = 0
        while not done:
            new_s = s.copy()
            for mark in (2,1):
                # select the action with highest cummulative reward
                if np.random.random() < eps or np.sum(q_table[s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], :]) == 0:
                    a = play_game(new_s, mark)
                    new_s[a] = mark    
                    chute += 1    
                else:
                    a = np.argmax(q_table[s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], :])
                    if new_s[a] != 0:
                        print('COLISÃO')
                    new_s[a] = mark
                    action += 1
                r = check_game(new_s)
                done =  r > 0
              
                q_table[s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], a] += \
                    r + lr * (y * np.max(q_table[new_s[0], new_s[1], new_s[2], new_s[3], new_s[4], new_s[5], new_s[6], new_s[7], new_s[8], :]) \
                    - q_table[s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], a])
                s = new_s

                if done:

                    print( 100 * action/chute,'%')

                    action = 0
                    chute = 0

                    break
    return q_table

if __name__ == "__main__":    

    if len(sys.argv) > 1:
        q_table = eps_greedy_q_learning_with_table(int(sys.argv[1]))
    else:
        q_table = eps_greedy_q_learning_with_table()

    np.save('q_table', q_table)




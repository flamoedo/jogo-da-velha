# -*- coding: utf-8 -*-
"""OXO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bC5i9gsNFomLKhaPHNKsyls8uTfpNT5j
"""

import numpy as np
import random
import pandas as pd

def check_lin(game):
  game = game.reshape(3,3)
  for mark in ['O','X']:
    for lin in range(3):  
      if (game == mark)[lin,].sum() == 3:
        return 2
    
  return 0

def check_col(game):
  game = game.reshape(3,3)
  for mark in ['O','X']:
    for col in range(3):  
      if (game == mark)[:,col].sum() == 3:
        return 2
    
  return 0

def check_diag1(game):  
  game = game.reshape(3,3)
  for mark in ('O','X'):
    s = 0
    for lin in range(3):  
      s += (game == mark)[lin,lin]
  if s == 3:
      return 2
  else:
      return 0

def check_diag2(game):
  game = game.reshape(3,3)
  for mark in ['O','X']:
    s = 0
    for lin in range(3):  
      s += (game == mark)[2-lin,lin]
  if s == 3:
      return 2
  else:
      return 0

def check_tied(game):
  game = game.reshape(3,3)
  if (game != '').sum() == 9:
    return 1
  else:
    return 0

def check_game(game):
  a = check_lin(game)
  b = check_col(game)
  c = check_diag1(game)
  d = check_diag2(game)
  e = check_tied(game)
  
  if a == 2:
    return a
  
  if b == 2:
    return b
  
  if c == 2:
    return c
  
  if d == 2:
    return d
  
  if e == 1:
    return e
  
  return 0

def play_game(game, mark):
  
  while(True):
  
    col = random.randint(0,8)

    if game[col] == '':      
      game[col] = mark
      return col

def iteration_bk(inumber):
  OXO = np.array(['','','','','','','','',''])

  q_table = np.zeros((3,3,3,3,3,3,3,3,3,2,9))

  data_game = []

  r = False

  while(not r):
    for mark in ('X', 'O'):
      OXOc = OXO.copy()
      y = play_game(OXO, mark)
      c = check_game(OXO)
      r = c > 0
      
      a = np.append(OXOc, [mark, y, c, inumber])

      data_game.append(a)

      OXOc[OXOc == ''] = 0
      OXOc[OXOc == 'X'] = 2
      OXOc[OXOc == 'O'] = 1

      a0 = OXOc[0].astype(int)
      a1 = OXOc[1].astype(int)
      a2 = OXOc[2].astype(int)
      a3 = OXOc[3].astype(int)
      a4 = OXOc[4].astype(int)
      a5 = OXOc[5].astype(int)
      a6 = OXOc[6].astype(int)
      a7 = OXOc[7].astype(int)
      a8 = OXOc[8].astype(int)

      if mark == 'X':
        m = 1
      else:
        m = 0

      q_table[a0, a1, a2, a3, a4, a5, a6, a7, a8, m, y] = c
      
      # data_game.append(a)
      if r:
        if c == 2:
          q_table[ :, :, :, :, :, :, :, :, :, m, :] = q_table[ :, :, :, :, :, :, :, :, :, m, :] + c
        else:
          if c == 1:
            q_table[ :, :, :, :, :, :, :, :, :, :, :] = q_table[ :, :, :, :, :, :, :, :, :, :, :] + c

        Q = np.append(Q, q_table)


        break        
        

  return data_game



def iteration(inumber):
  OXO = np.array(['','','','','','','','',''])

  data_game = []

  r = False

  while(not r):
    for mark in ('X', 'O'):
      OXOc = OXO.copy()
      y = play_game(OXO, mark)
      c = check_game(OXO)
      r = c > 0
      
      a = np.append(OXOc, [mark, y, c, inumber])
      
      data_game.append(a)
      if r:
        break        
        
  for q in data_game:
    if q[9] == mark or c == 1 :
      q[11] = c

  return data_game

if __name__ == "__main__":    

  # Q = []

  q_table = np.zeros((3,3,3,3,3,3,3,3,3,2,9))


  for i in range(10):
    data_game = iteration(i)  
          
    for g in data_game:

      g[g == ''] = 0
      g[g == 'X'] = 2
      g[g == 'O'] = 1

      a0 = g[0].astype(int)
      a1 = g[1].astype(int)
      a2 = g[2].astype(int)
      a3 = g[3].astype(int)
      a4 = g[4].astype(int)
      a5 = g[5].astype(int)
      a6 = g[6].astype(int)
      a7 = g[7].astype(int)
      a8 = g[8].astype(int)

      m = g[9].astype(int) - 1

      y = g[10].astype(int)

      c = g[11].astype(int)

      q_table[a0, a1, a2, a3, a4, a5, a6, a7, a8, m, y] = q_table[a0, a1, a2, a3, a4, a5, a6, a7, a8, m, y] + c

np.save('q_table', q_table)



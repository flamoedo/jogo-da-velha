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
  for mark in [1,2]:
    for lin in range(3):  
      if (game == mark)[lin,].sum() == 3:
        return 2
    
  return 0

def check_col(game):
  game = game.reshape(3,3)
  for mark in [1,2]:
    for col in range(3):  
      if (game == mark)[:,col].sum() == 3:
        return 2
    
  return 0

def check_diag1(game):  
  game = game.reshape(3,3)
  for mark in (1,2):
    s = 0
    for lin in range(3):  
      s += (game == mark)[lin,lin]
    if s == 3:
        return 2
  return 0

def check_diag2(game):
  game = game.reshape(3,3)
  for mark in [1,2]:
    s = 0
    for lin in range(3):  
      s += (game == mark)[2-lin,lin]
    if s == 3:
        return 2
  return 0

def check_tied(game):
  game = game.reshape(3,3)
  if (game != 0).sum() == 9:
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

    if game[col] == 0:      
      game[col] = mark
      return col


def iteration(inumber):
  OXO = np.zeros(9)

  data_game = []

  p = False

  while(not p):
    for mark in (1, 2):
      OXOc = OXO.copy()

      y = play_game(OXO, mark)
      r = check_game(OXO)
      p = r > 0
      
      a = np.append(OXOc, [mark, y, c])
      
      data_game.append(a)
      if p:
        break        
        
  for q in data_game:
    if q[9] == mark or c == 1 :
      q[-1] = c

  return data_game





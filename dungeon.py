#!/usr/bin/env python3
import skilstak.colors as c
import random
import time

def clear():
  print(c.clear,end='')

def build_dungeon():
  dungeon = [[c.red + '#' for x in range(25)] for y in range(25)]
  path_tiles = [[12,12]]
  branches = [[12,12,None]]
  dead_ends = []
  colors = [c.yellow, c.orange, c.red, c.magenta, c.violet, c.blue, c.cyan, c.green]
  
  while True:
    branch = random.choice(branches)
    branches.remove(branch)
    directions = [1,2,3,4]
    expanded = False
    trials = 0
    while True:
      trials += 1
      dir = random.choice(directions)
      directions.remove(dir)
      if dir == 1: # up
        if branch[0] == 0 or [branch[0]-2,branch[1]] in path_tiles or branch[2] == 'up':
          pass
        elif branch[0] == 1 or [branch[0]-3,branch[1]] in path_tiles:
          path_tiles.append([branch[0]-1,branch[1]])
          dead_ends.append([branch[0]-1,branch[1]])
          expanded = True
        else:
          path_tiles.append([branch[0]-1,branch[1]])
          path_tiles.append([branch[0]-2,branch[1]])
          branches.append([branch[0]-2,branch[1],'up'])
          expanded = True
          
      elif dir == 2: # right
        if branch[1] == 24 or [branch[0],branch[1]+2] in path_tiles or branch[2] == 'right':
          pass
        elif branch[1] == 23 or [branch[0],branch[1]+3] in path_tiles:
          path_tiles.append([branch[0],branch[1]+1])
          dead_ends.append([branch[0],branch[1]+1])
          expanded = True
        else:
          path_tiles.append([branch[0],branch[1]+1])
          path_tiles.append([branch[0],branch[1]+2])
          branches.append([branch[0],branch[1]+2,'right'])
          expanded = True
            
      elif dir == 3: # down
        if branch[0] == 24 or [branch[0]+2,branch[1]] in path_tiles or branch[2] == 'down':
          pass
        elif branch[0] == 23 or [branch[0]+3,branch[1]] in path_tiles:
          path_tiles.append([branch[0]+1,branch[1]])
          dead_ends.append([branch[0]+1,branch[1]])
          expanded = True
        else:
          path_tiles.append([branch[0]+1,branch[1]])
          path_tiles.append([branch[0]+2,branch[1]])
          branches.append([branch[0]+2,branch[1],'down'])
          expanded = True
          
      elif dir == 4: # left
        if branch[1] == 0 or [branch[0],branch[1]-2] in path_tiles or branch[2] == 'left':
          pass
        elif branch[1] == 1 or [branch[0],branch[1]-3] in path_tiles:
          path_tiles.append([branch[0],branch[1]-1])
          dead_ends.append([branch[0],branch[1]-1])
          expanded = True
        else:
          path_tiles.append([branch[0],branch[1]-1])
          path_tiles.append([branch[0],branch[1]-2])
          branches.append([branch[0],branch[1]-2,'left'])
          expanded = True
      if directions == []:
        break
    if branches == []:
      break

  for tile in path_tiles:
    dungeon[tile[0]][tile[1]] = c.base3 + ' '
  
  exit = random.choice(path_tiles)
  dungeon[exit[0]][exit[1]] = c.green + '$'
  while True:
    start = random.choice(path_tiles)
    if start != exit:
      break
  dungeon[start[0]][start[1]] = c.blue + '@'
  return dungeon
  
def moving(dungeon):
  last_tile_rep = c.base03 + '$'
  for y_find in range(25):
    for x_find in range(25):
      if '@' in dungeon[y_find][x_find]:
        p_y = y_find
        p_x = x_find
          
  while True:
    clear()
    if p_x >= 1:
      dungeon[p_y][p_x-1] = dungeon[p_y][p_x-1].split(c.base02).pop() # left
      
    if p_x >= 1 and p_y >= 1:
      dungeon[p_y-1][p_x-1] = dungeon[p_y-1][p_x-1].split(c.base02).pop() # upper left
      
    if p_y >= 1:
      dungeon[p_y-1][p_x] = dungeon[p_y-1][p_x].split(c.base02).pop() # up  
      
    if p_x <= 23 and p_y >= 1:
      dungeon[p_y-1][p_x+1] = dungeon[p_y-1][p_x+1].split(c.base02).pop() # upper right
      
    if p_x <= 23:
      dungeon[p_y][p_x+1] = dungeon[p_y][p_x+1].split(c.base02).pop() # right
      
    if p_x <= 23 and p_y <= 23:
      dungeon[p_y+1][p_x+1] = dungeon[p_y+1][p_x+1].split(c.base02).pop() # lower right
      
    if p_y <= 23:
      dungeon[p_y+1][p_x] = dungeon[p_y+1][p_x].split(c.base02).pop() # down
    
    if p_x >= 1 and p_y <= 23:
      dungeon[p_y+1][p_x-1] = dungeon[p_y+1][p_x-1].split(c.base02).pop() # lower left
  
    print(c.base3 + '┌─────────────────────────┐')
    for pr_y in dungeon:
      print(c.base3 + '│',end='')
      for pr_x in pr_y:
        if c.base02 in pr_x:
          print(' ',end='')
        else:
          print(pr_x,end='')
      print(c.base3 + '│')
    print(c.base3 + '└─────────────────────────┘')

    try:
      mv = input('>>> ')
    except EOFError:
      build_dungeon()
      continue
    if mv == 'w':
      try:
        if '#' not in dungeon[p_y-1][p_x] and p_y-1 >= 0:
          last_tile = dungeon[p_y-1][p_x]
          dungeon[p_y][p_x] = last_tile_rep
          last_tile_rep = last_tile
          p_y -= 1
          dungeon[p_y][p_x] = c.blue + '@'
      except IndexError:
        pass
    elif mv == 'a':
      try:
        if '#' not in dungeon[p_y][p_x-1] and p_x-1 >= 0:
          last_tile = dungeon[p_y][p_x-1]
          dungeon[p_y][p_x] = last_tile_rep
          last_tile_rep = last_tile
          p_x -= 1
          dungeon[p_y][p_x] = c.blue + '@'
      except IndexError:
        pass
    elif mv == 's':
      try:
        if '#' not in dungeon[p_y+1][p_x]:
          last_tile = dungeon[p_y+1][p_x]
          dungeon[p_y][p_x] = last_tile_rep
          last_tile_rep = last_tile
          p_y += 1
          dungeon[p_y][p_x] = c.blue + '@'
      except IndexError:
        pass
    elif mv == 'd':
      try:
        if '#' not in dungeon[p_y][p_x+1]:
          last_tile = dungeon[p_y][p_x+1]
          dungeon[p_y][p_x] = last_tile_rep
          last_tile_rep = last_tile
          p_x += 1
          dungeon[p_y][p_x] = c.blue + '@'
      except IndexError:
        pass
    if c.green + '$' in last_tile_rep:
      clear()
      input('Fin.')
      break

  
while True:
  dungeon = build_dungeon()
  try:
    moving(dungeon)
  except KeyboardInterrupt:
    break
clear()
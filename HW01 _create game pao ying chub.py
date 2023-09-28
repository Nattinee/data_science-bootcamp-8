#HW01 - create game pao ying chub
import random
from tabulate import tabulate
import numpy as np
import pandas as pd
def play_game():

  # Create dataframe of result
  table_result = [['rock', 'rock', 'Tie.'],
            ['rock', 'paper', 'You lose.'],
            ['rock', 'scissors', 'You win.'],
            ['paper' ,'rock','You win.'],
            ['paper' ,'paper','Tie.'],
            ['paper' ,'scissors','You lose.'],
            ['scissors' ,'rock','You lose.'],
            ['scissors' ,'paper','You win.'],
            ['scissors' ,'scissors','Tie.']]

  # Create a DataFrame from the list of result
  df_result = pd.DataFrame(table_result, columns=['you', 'bot', 'result'])

  # Create a DataFrame from the list of hand
  hand_name = ['rock', 'paper', 'scissors']
  hand = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

  # create data frame
  game_list = []
  game = pd.DataFrame(game_list, columns=['round_no', 'you', 'bot', 'result'])

  # Sample 2 rows from the DataFrame with replacement
  def play():
    com = random.choice(hand_name)
    return(com)

  def sum_result():
    grouped_result = game.groupby('result')
    count_result = grouped_result.agg(count=('result', 'count'))
    table = tabulate(count_result, headers='keys', tablefmt='psql')
    print(f"Total result of {round-1} rounds.")
    print(table)
    print(game)

  # start game
  round = 0
  print("Welcome to Pao Ying Chub game!")
  print("Let start by enter below key\nr = rock\np = paper\ns = scissors\nq = quit")

  while True:
    round = round + 1
    your_turn = input(f"Round {round} one two shoot!: ")
    if round == 1 and your_turn == 'q':
      print("You quit!")
      break
    elif your_turn == 'q':
      sum_result()
      break
    elif your_turn == 'r' or your_turn == 'p' or your_turn == 's':
      game.loc[round, 'round_no'] = round
      game.loc[round, 'bot'] = play()
      game.loc[round, 'you'] = hand[your_turn]
      round_result = np.where((df_result['bot'] == game.loc[round, 'bot']) & (df_result['you'] == game.loc[round, 'you']))[0][0]
      game.loc[round, 'result'] = df_result.loc[round_result, 'result']
      print(f"You : {game.loc[round, 'you']}")
      print(f"Bot : {game.loc[round, 'bot']}")
      print(f"{game.loc[round, 'result']} !")
    else:
      round = round - 1
      print("You enter wrong key ,please try again!")

play_game()

from enum import Enum
from collections import Counter

class CellState(Enum):
  DEAD = 0
  ALIVE = 1

THREE_LIVE_NEIGHBORS = 3
TWO_LIVE_NEIGHBORS = 2


def next_state(current_state, number_of_live_neighbors):
  return CellState.ALIVE if number_of_live_neighbors == THREE_LIVE_NEIGHBORS or \
    number_of_live_neighbors == TWO_LIVE_NEIGHBORS and current_state == CellState.ALIVE else CellState.DEAD


def generate_signals_for_one_position(x, y):
  return [(x - 1 + i, y - 1 + j) for i in range(3) for j in range(3) if (x - 1 + i) != x or (y - 1 + j) != y]
  

def generate_signals_for_multiple_positions(positions):
  return [signal for position in positions for signal in generate_signals_for_one_position(position[0], position[1])]


def count_signals(signals):
  return Counter(signals) 


def next_generation(positions):
  return set([position for position, signals_count in dict(count_signals(generate_signals_for_multiple_positions(positions))).items()
   if CellState.ALIVE == next_state(
     CellState.ALIVE if position in positions else CellState.DEAD,
     signals_count)])

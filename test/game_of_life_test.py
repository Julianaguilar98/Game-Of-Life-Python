import unittest
import sys
sys.path.insert(0, 'assign1/src')
import game_of_life as game

class GameOfLifeTests(unittest.TestCase):
  def test_Canary(self):
    self.assertTrue(True)

  def test_dead_cell_with_zero_neighbors_stays_dead(self):
    self.assertEqual(game.CellState.DEAD, game.next_state(game.CellState.DEAD, 0))

  def test_dead_cell_with_one_neighbors_stays_dead(self):
    self.assertEqual(game.CellState.DEAD, game.next_state(game.CellState.DEAD, 1))

  def test_dead_cell_with_two_neighbors_stays_dead(self):
    self.assertEqual(game.CellState.DEAD, game.next_state(game.CellState.DEAD, 2))

  def test_dead_cell_with_five_neighbors_stays_dead(self):
    self.assertEqual(game.CellState.DEAD, game.next_state(game.CellState.DEAD, 5))

  def test_dead_cell_with_eight_neighbors_stays_dead(self):
    self.assertEqual(game.CellState.DEAD, game.next_state(game.CellState.DEAD, 8))

  def test_dead_cell_with_three_neighbors_comes_to_life(self):
    self.assertEqual(game.CellState.ALIVE, game.next_state(game.CellState.DEAD, 3))
  
  def test_live_cell_with_one_neighbors_dies(self):
    self.assertEqual(game.CellState.DEAD, game.next_state(game.CellState.ALIVE, 1))

  def test_live_cell_with_four_neighbors_dies(self):
    self.assertEqual(game.CellState.DEAD, game.next_state(game.CellState.ALIVE, 4))
  
  def test_live_cell_with_eight_neighbors_dies(self):
    self.assertEqual(game.CellState.DEAD, game.next_state(game.CellState.ALIVE, 8))

  def test_live_cell_with_two_neighbors_lives(self):
    self.assertEqual(game.CellState.ALIVE, game.next_state(game.CellState.ALIVE, 2))

  def test_live_cell_with_three_neighbors_lives(self):
    self.assertEqual(game.CellState.ALIVE, game.next_state(game.CellState.ALIVE, 3))

  def test_generating_signals_one_position_2_3(self):
    test_set = set([(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)])
    self.assertEqual(test_set, set(game.generate_signals_for_one_position(2, 3)))
    
  def test_generating_signals_one_position_3_3(self):
    test_set = set([(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)])
    self.assertEqual(test_set, set(game.generate_signals_for_one_position(3, 3)))

  def test_generating_signals_one_position_2_4(self):
    test_set = set([(1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)])
    self.assertEqual(test_set, set(game.generate_signals_for_one_position(2, 4)))

  def test_generating_signals_one_position_0_0(self):
    test_set = set([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
    self.assertEqual(test_set, set(game.generate_signals_for_one_position(0, 0)))

  def test_generating_signals_0_position_for_0_position(self):
    self.assertEqual(set(), set(game.generate_signals_for_multiple_positions([])))
    
  def test_generating_signals_8_positions_for_1_position(self):
    test_set = set([(1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)])
    self.assertEqual(test_set, set(game.generate_signals_for_multiple_positions([(2, 4)])))

  def test_generating_signals_16_positions_for_2_position(self):
    test_set = set([(1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5),
                    (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
    self.assertEqual(test_set, set(game.generate_signals_for_multiple_positions([(2, 4), (0, 0)])))
    
  def test_generating_signals_multiple_position_three_positions(self):
    test_set = set([(5, 5), (3, 4), (4, 3), (5, 4), (4, 5), (3, 3), (5, 3), (3, 5),
                    (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1),
                    (-5, -3), (-4, -3), (-3, -3), (-5, -4), (-3, -4), (-5, -5), (-4, -5), (-3, -5)])
    self.assertEqual(test_set, set(game.generate_signals_for_multiple_positions([(4, 4), (0, 0), (-4, -4)])))    
    
  def test_count_signals_no_positions(self):
    self.assertEqual({}, game.count_signals([]))

  def test_count_signals_one_positions(self):
    self.assertEqual({(1, 1): 1}, game.count_signals([(1, 1)]))

  def test_count_signals_two_positions_two_same_positions(self):
    self.assertEqual({(1, 1): 2}, game.count_signals([(1, 1), (1, 1)]))

  def test_count_signals_three_positions_two_same_positions(self):
    self.assertEqual({(1, 1): 2, (2, 2): 1}, game.count_signals([(1, 1), (2, 2), (1, 1)]))

  def test_next_generation_no_positions(self):
    self.assertEqual(set(), game.next_generation(set())) 

  def test_next_generation_one_positions(self):
    self.assertEqual(set(), game.next_generation(set([(0, 1)]))) 

  def test_next_generation_positions_2_3_and_2_4(self):
    self.assertEqual(set(), game.next_generation(set([(2, 3), (2, 4)])))

  def test_next_generation_positions_1_1_and_1_2_and_3_0(self):
    self.assertEqual(set([(2, 1)]), game.next_generation(set([(1, 1), (1, 2), (3, 0)])))

  def test_next_generation_positions_1_1_and_1_2_and_2_1_and_2_2(self):
    self.assertEqual(set([(1, 1), (1, 2), (2, 1), (2, 2)]), game.next_generation(set([(1, 1), (1, 2), (2, 2)])))

  def test_next_generation_block_returns_block(self):
    self.assertEqual(set([(1, 1), (1, 2), (2, 1), (2, 2)]), game.next_generation(set([(1, 1), (1, 2), (2, 1), (2, 2)])))

  def test_next_generation_beehive_returns_beehive(self):
    self.assertEqual(set([(0, 0), (1, 1), (2, 1), (3, 0), (2, -1), (1, -1)]), game.next_generation(set([(0, 0), (1, 1), (2, 1), (3, 0), (2, -1), (1, -1)])))

  def test_next_generation_vertical_line_returns_horizontal_line(self):
    self.assertEqual(set([(0, 2), (1, 2), (2, 2)]), game.next_generation(set([(1, 1), (1, 2), (1, 3)])))

  def test_next_generation_horizontal_line_returns_vertical_line(self):
    self.assertEqual(set([(1, 1), (1, 2), (1, 3)]), game.next_generation(set([(0, 2), (1, 2), (2, 2)])))

  def test_next_generation_glider_with_cell_at_top_returns_glider_cell_now_right_side(self):
    self.assertEqual(set([(1, 0), (2, 0), (2, 1), (3, 1), (1, 2)]), game.next_generation(set([(0, 1), (1, 0), (2, 0), (2, 1), (2, 2)])))

if __name__ == '__main__':
  unittest.main()

import unittest
from grb_calci import levels


class TestGRB(unittest.TestCase):
    
    def test_levels_1(self):
        print('normal test')
        # prev_open,prev_high,prev_low,prev_close,cur_high,cur_low=[33050.0,33099.95,32750,32805,33099,32838.8]
        input_levels=[33050.0,33099.95,32750,32805,33099,32838.8]
        expected_result=[33182.07,33016.16,32427.93,32590.07]
        result = levels(*input_levels)
        self.assertEqual(list(map(int,result)), list(map(int,expected_result)))
    def test_gap(self):
        print('gap test')
        # prev_open,prev_high,prev_low,prev_close,cur_high,cur_low=[33050.0,33099.95,32750,32805,33099,32838.8]
        input_levels=[33050.0,33099.95,32750,32805,34000,32838.8]
        expected_result=[34000,33830,32838.8,33002.99]
        result = levels(*input_levels)
        self.assertEqual(list(map(int,result)), list(map(int,expected_result)))
    

if __name__ == '__main__':
    unittest.main()
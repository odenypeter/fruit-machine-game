import unittest

from main_oop import FruitMachineGame


class TestFruitMachineGame(unittest.TestCase):
    def test_get_slots(self):
        """
        return  4 slots being a subset of colors
        :return:
        """
        fruit_machine_game = FruitMachineGame(
            slots=4, balance=100, credits=2, cost_per_game=5
        )
        slots = fruit_machine_game.get_slots()
        self.assertEqual(len(slots), 4)

        # check that all items are valid
        self.assertEqual(
            set(slots).intersection(set(fruit_machine_game.colors)),
            set(slots)
        )

    def test_get_prize(self):
        fruit_machine_game = FruitMachineGame(
            slots=4, balance=100, credits=2, cost_per_game=5
        )
        # no similar adjacent slots, slots not unique
        result = ['green', 'black', 'yellow', 'black']
        prize, award = fruit_machine_game.get_prize(result)

        # award is 0, prize is 0
        self.assertEqual(prize, 0.0)
        self.assertEqual(award, 0.0)

        #  similar adjacent slots (yellow), slots not unique
        fruit_machine_game = FruitMachineGame(
            slots=4, balance=100, credits=2, cost_per_game=5
        )
        result2 = ['green', 'yellow', 'yellow', 'black']
        prize, award = fruit_machine_game.get_prize(result2)

        self.assertEqual(prize, 25.0)
        self.assertEqual(award, 0.0)

        #  all the same
        fruit_machine_game = FruitMachineGame(
            slots=4, balance=100, credits=2, cost_per_game=5
        )
        result3 = ['green', 'green', 'green', 'green']
        prize, award = fruit_machine_game.get_prize(result3)

        self.assertEqual(prize, 100.0)
        self.assertEqual(award, 0.0)

        #  all unique
        fruit_machine_game = FruitMachineGame(
            slots=4, balance=100, credits=2, cost_per_game=5
        )
        result4 = ['green', 'yellow', 'white', 'black']
        prize, award = fruit_machine_game.get_prize(result4)

        self.assertEqual(prize, 50.0)
        self.assertEqual(award, 0.0)


if __name__ == '__main__':
    unittest.main()

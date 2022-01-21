import random


class FruitMachineGame:
    def __init__(self, slots, balance, credits, cost_per_game):
        self.machine_balance = balance
        self.game_slots = slots
        self.total_prize = 0.0
        self.colors = ('black', 'white', 'green', 'yellow')
        self.single_play_cost = cost_per_game
        self.play_credits = credits

    def main(self):
        print('*****WELCOME TO FRUIT MACHINE GAME****')
        print(f'**You have {self.play_credits} rounds to play***')

        while self.play_credits > 0:
            self.play_credits -= 1
            print(f'{self.play_credits} rounds left')

            # generate and initialize slots
            slots = self.get_slots()
            print('SLOTS::: ->', slots)

            # call play_game method
            won, award = self.get_prize(slots)
            print(f'Prize:: {won} <> Award:: {award}')
            # update prize if a play won
            self.total_prize += won

            # update award if a user won an award
            self.play_credits += award

        # output the results
        print('***Game complete***')
        print('Result: ', self.total_prize)

    def get_prize(self, result) -> tuple:
        """
        compute prize based on the slots outcome
        :param result:
        :return: tuple
        """
        award = 0.0
        prize = 0.0

        # check if all slots are of the same color
        if all(x == result[0] for x in result):
            prize = self.machine_balance

        else:
            # check if all slots are unique
            if len(set(result)) == len(result):
                prize = self.machine_balance / 2

            else:
                previous = result[0]
                same_adj = 0

                for item in result[1:]:
                    if previous == item:
                        same_adj += 1

                    # assign previous to current item
                    previous = item

                # check if there are any 2 similar adjacent slots and award player
                if same_adj > 0:
                    prize = self.single_play_cost * 5

                    if prize > self.machine_balance:
                        award = prize - self.machine_balance
                        prize = 0

        return prize, award

    def get_slots(self) -> list:
        """
        generates and return random slots
        :return list:
        """
        return random.choices(self.colors, k=4)


# run the game
fruit_machine_game = FruitMachineGame(4, 200, 3, 10)
fruit_machine_game.main()

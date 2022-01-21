# Pseudocode

# colors = ['black', 'white', 'green', 'yellow']
# function main()
#     machine_balance = x
#     play_credits = 3
#     play_cost = 10
#     prize = 0.0

#     while credits > 0:
#       // reduce credits by 1
#       credits -= 1

#       // play game
#       result = play_game(4)

#       //get prize
#       prize,award = get_prize(machine_balance, play_cost, result, prize)

#       // update machine balance
#       machine_balance -= prize

#       // update prize
#       prize += prize

#       // update credits
#       credits += award

#     // do something with the prize
#       print('Prize:::', prize)

# play the game
# function play_game(num_slots)
#     result = []
#     for i in range(num_slots):
#       slot = random.randint(0, 3)
#       result.append(colors[slot)
#     return result
#           OR
#     return random.choices(COLORS, k=4)
# calculate the player prize
# function get_prize(machine_balance, single_play_cost, result, prize)
#     award = 0
#     if all(x==slot[0] for x in result)
#         prize = machine_balance
#      else
#         // Check if all elements are unique
#         if len(set(result)) == 4
#                 prize = machine_balance / 2
#         else:
#             # check 2 adjacent slots for similarity
#             adjacent = 0
#             previous = None
#             for item in result
#               if previous == item
#                   adjacent += 1
#                previous = item

#             if adjacent > 0:
#                prize = single_play_cost * 5
#                if prize > machine_balance:
#                   award = prize - machine_balance
#                   prize = 0
#     return prize, award


import random

COLORS = ('black', 'white', 'green', 'yellow')


def main():
    """
    entry method to the fruit machine challenge
    """
    # initialize variables
    machine_balance = 200
    single_play_cost = 10
    prize = 0
    play_credits = 3

    print('*****WELCOME TO FRUIT MACHINE GAME****')
    print(f'**You have {play_credits} rounds to play***')

    while play_credits > 0:
        play_credits -= 1
        print(f'{play_credits} rounds left')

        # generate and initialize slots
        slots = play_game(4)
        print('SLOTS::: ->', slots)

        # call play_game method
        won, award = get_prize(machine_balance, single_play_cost, slots)
        print(f'Prize:: {won} <> Award:: {award}')
        # update prize if a play won
        prize += won

        # update award if a user won an award
        play_credits += award

    # output the results
    print('***Game complete***')
    print('Result: ', prize)


def get_prize(machine_balance, single_play_cost, result) -> tuple:
    """
    generates the slots and awards the user based on the outcome
    :param machine_balance:
    :param single_play_cost: const per game round
    :param result: slots from the player
    :param prize: current prize
    :return:
    """
    award = 0.0
    prize = 0.0

    # check if all slots are of the same color
    if all(x == result[0] for x in result):
        prize = machine_balance

    else:
        # check if all slots are unique
        if len(set(result)) == len(result):
            prize = machine_balance / 2

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
                prize = single_play_cost * 5

                if prize > machine_balance:
                    award = prize - machine_balance
                    prize = 0

    return prize, award


def play_game(num_slots):
    """
    generates the slots
    :param num_slots: number of slots to generate
    :return: slots
    """
    # option one
    # result = []
    # for i in range(num_slots-1):
    #     slot = random.randint(0, 3)
    #     result.append(COLORS[slot])
    # return result

    # option 2
    return random.choices(COLORS, k=num_slots)


main()

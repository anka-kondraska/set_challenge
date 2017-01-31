"""Game of SET, evaluating user input cards, finding all sets based 
on user input. Additionally finding disjoint sets - where no SET has a card
in common. Input is assumed to be always valid, and using these attributes:
color(blue, yellow, green), symbol(A, S, H), shading(a, A, @)(s, S, $)(h, H, #), 
and number.
INPUT FORMAT:
blue ### - blue H other 3
yellow ss - yellow S lower 2
green A - green A upper 1 """
import itertools
import timeit


class Card(object):
    """Card class for game of SET"""
    def __init__(self, color, symbol, shading, number):
        self.color = color
        self.symbol = symbol
        self.shading = shading
        self.number = number

    def __repr__(self):
        return "Card({}, {}, {}, {})" .format(self.color, self.symbol,
                                              self.shading, self.number)


class Table(object):
    """Collection of cards class for game of SET"""
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __iter__(self):
        return iter(self.cards)

    def __repr__(self):
        return str(self.cards)

################################
# Functions for evaluating cards

def eval_shading(card):
    """Function to evaluate shading - card attribute in game of SET"""
    if card.islower():
        return 'lower'
    elif card.isupper():
        return 'upper'
    else:
        return 'zing'


def eval_symbol(card):
    """Function to evaluate symbol - card attribute in game of SET"""
    if card in ('a', 'A', '@'):
        return 'A'
    elif card in ('s', 'S', '$'):
        return 'S'
    else:
        return 'H'


def eval_card(card):
    """Function to evaluate the formatted user card input"""
    card = card.split()
    color = card[0]
    sym = [letter for letter in card[1]]
    number = len(sym)
    shading = eval_shading(card[1])
    symbol = eval_symbol(sym[0])
    return Card(color, symbol, shading, number)


def same(ls):
    """Checking if attributes in a set are all the same"""
    return len(set(ls)) == 1


def different(ls):
    """Checking if attributes in a set are all different"""
    return len(set(ls)) == 3


def formatted_print(sets, num):
    """Function to re-format and print out disjointed sets of cards"""
    if sets:
        for line in sets:
            for i in xrange(num):
                for card in line[i]:
                    if card.shading == 'upper':
                        print card.color + ' ' + card.symbol * card.number
                    elif card.shading == 'lower':
                        print card.color + ' ' + card.symbol.lower() * card.number
                    else:
                        if card.symbol == 'S':
                            print card.color + ' ' + '$' * card.number
                        elif card.symbol == 'A':
                            print card.color + ' ' + '@' * card.number
                        else:
                            print card.color + ' ' + '#' * card.number
                print


############################
# Functions for finding sets

def find_sets(table):
    """Finding all possible sets in a game of SET"""
    combinations = itertools.combinations(table, 3)
    sets = []
    for combination in combinations:
        attributes = [[c.color for c in combination], [c.number for c in combination],
                      [c.symbol for c in combination], [c.shading for c in combination]]
        if all(same(attr) or different(attr) for attr in attributes):
            sets.append(combination)
    return sets


def find_disjoint_sets(sets, largest_set = None):
    """Function to find max number of disjoint sets in all sets"""
    max_sets = 0
    for i in xrange(1, len(sets)):
        disjoint = []
        cards_seen = []
        max_sofar = 0
        count = 0
        stz = sets[i:] + sets[:i]
        for s in stz:
            current_set_cards = [card for card in s]
            if (current_set_cards[0] not in cards_seen and
               current_set_cards[1] not in cards_seen and
               current_set_cards[2] not in cards_seen):
                disjoint.append(s)
                count += 1
                for card in current_set_cards:
                    cards_seen.append(card)
            if count > max_sofar:
                max_sofar = count
        if max_sofar > max_sets:
            largest_set = []
            max_sets = max_sofar
            largest_set.append(disjoint)

    return max_sets, largest_set

# Running this file in 1.. 2.. 3.. Boom!
if __name__ == '__main__':
    start = timeit.timeit()

    num_card = int(raw_input())
    table = Table()
    for _ in xrange(num_card):
        card = raw_input()
        table.add_card(eval_card(card))
    sets = sorted(find_sets(table))
    max_dis_number, max_disjoint_sets = find_disjoint_sets(sets)
    print len(sets)
    print max_dis_number
    print
    formatted_print(max_disjoint_sets, max_dis_number)
    print

    print '#' * 35
    print "disjoint_sets.py run in {}." .format(timeit.timeit()-start)


################################
#  Optional Testing - trying different inputs
def test_game_of_set():
    print '#' * 35
    print "TESTING"
    test1 = ['blue hhh', 'yellow @', 'green ##', 'yellow ###', 'blue AA',
             'green SSS', 'blue ###', 'yellow s', 'yellow ##', 'blue H',
             'green A', 'blue $', 'green SS', 'green ###', 'blue ss',
             'yellow $', 'green aaa', 'green AA', 'yellow sss', 'green aa',
             'green S', 'green HH', 'yellow AA', 'yellow ss', 'green h',
             'blue $$', 'blue aa', 'green sss']
    test2 = ['blue #', 'green $', 'blue AA', 'yellow @', 'blue @@@', 'green A',
             'yellow $$$', 'yellow @@@', 'yellow HHH', 'yellow #', 'yellow @@',
             'blue a', 'blue sss', 'green a', 'green @']
    test3 = ['blue hhh', 'yellow @', 'green ##', 'yellow SSS', 'blue AA',
             'green aa', 'green s', 'blue sss', 'green a', 'green @',
             'yellow hh']
    test4 = ['yellow $$']

    tests = [test1, test2, test3, test4]
    for test in tests:
        table = Table()
        for card in test:
            table.add_card(eval_card(card))
        sets = sorted(find_sets(table))
        max_dis_number, max_disjoint_sets = find_disjoint_sets(sets)
        print len(sets)
        print max_dis_number
        print
        formatted_print(max_disjoint_sets, max_dis_number)

# test_game_of_set()

import unittest
import disjoint_sets


class TestClasses(unittest.TestCase):
    """Test Card and Table classes from disjoint_sets"""

    def setUp(self):
        self.card1 = disjoint_sets.Card('blue', 'S', 'zing', 2)
        self.card2 = disjoint_sets.Card('yellow', 'H', 'upper', 3)
        self.card3 = disjoint_sets.Card('green', 'A', 'lower', 1)
        self.table = disjoint_sets.Table()
        self.table.add_card(self.card1)

    def testCard(self):
        self.assertEquals(self.card1.color, 'blue')
        self.assertEquals(self.card2.number, 3)

    def testTable(self):
        self.assertRaises(TypeError, type(self.table) == '__main__.Table')
        self.assertEquals(str(self.table), '[Card(blue, S, zing, 2)]')
        self.assertEquals(str(type(self.table)), "<class 'disjoint_sets.Table'>")


class TestCardEvals(unittest.TestCase):
    """Test card evaluating functions from disjoint_sets"""

    def setUp(self):
        self.card1 = disjoint_sets.Card('blue', 'S', 'zing', 2)
        self.card2 = disjoint_sets.Card('yellow', 'H', 'upper', 3)
        self.card3 = disjoint_sets.Card('green', 'A', 'lower', 1)
        self.table = disjoint_sets.Table()
        self.table.add_card(self.card1)
        self.table.add_card(self.card2)
        self.table.add_card(self.card3)
        self.sets = []
        self.sets.append(self.table)

    def testShading(self):
        self.assertEqual(disjoint_sets.eval_shading('A'), 'upper')
        self.assertEqual(disjoint_sets.eval_shading('A'), 'upper')

    def testSymbol(self):
        self.assertEqual(disjoint_sets.eval_symbol('@'), 'A')

    def testSame(self):
        self.assertEqual(disjoint_sets.same(['blue', 'blue', 'blue']), True)
        self.assertEqual(disjoint_sets.same(['blue', 'blue', 'green']), False)

    def testDifferent(self):
        self.assertEqual(disjoint_sets.different(['green', 'blue', 'yellow']), True)
        self.assertEqual(disjoint_sets.different(['blue', 'blue', 'blue']), False)


class TestSetFinds(unittest.TestCase):
    """Test set and disjoint set finding functions"""

    def setUp(self):
        self.card1 = disjoint_sets.Card('blue', 'S', 'zing', 2)
        self.card2 = disjoint_sets.Card('yellow', 'H', 'upper', 3)
        self.card3 = disjoint_sets.Card('green', 'A', 'lower', 1)
        self.table = disjoint_sets.Table()
        self.table.add_card(self.card1)
        self.table.add_card(self.card2)
        self.table.add_card(self.card3)
        self.sets = []
        self.sets.append(self.table)

    def testSet(self):
        self.assertEquals(str(disjoint_sets.find_sets(self.table)),
        '[(Card(blue, S, zing, 2), Card(yellow, H, upper, 3), Card(green, A, lower, 1))]')

    def testDisjointSet(self):
        self.assertEquals(str(disjoint_sets.find_disjoint_sets(self.sets)),
                            '(0, None)')

if __name__ == '__main__':
    unittest.main()

# suite = unittest.TestLoader().loadTestsFromTestCase(TestClasses)
# unittest.TextTestRunner(verbosity=2).run(suite)

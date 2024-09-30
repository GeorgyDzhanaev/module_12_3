import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @staticmethod
    def skip_if_frozen(test_func):
        def wrapper(*args, **kwargs):
            if RunnerTest.is_frozen:
                raise unittest.SkipTest('Тесты в этом кейсе заморожены')
            return test_func(*args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_challenge(self):
        pass

    @skip_if_frozen
    def test_run(self):
        pass

    @skip_if_frozen
    def test_walk(self):
        pass


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @staticmethod
    def skip_if_frozen(test_func):
        def wrapper(*args, **kwargs):
            if TournamentTest.is_frozen:
                raise unittest.SkipTest('Тесты в этом кейсе заморожены')
            return test_func(*args, **kwargs)
        return wrapper

    @skip_if_frozen
    def test_first_tournament(self):
        pass

    @skip_if_frozen
    def test_second_tournament(self):
        pass

    @skip_if_frozen
    def test_third_tournament(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
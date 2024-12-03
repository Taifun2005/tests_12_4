import logging
from rt_with_exceptions import Runner
logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest:
    @staticmethod
    def test_walk():
        try:
            runner = Runner("Test Runner", speed=-10)
            runner.walk()
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError :
            logging.warning(f"Неверная скорость для Runner")

    @staticmethod
    def test_run():
        try:
            runner = Runner(True, speed=10)
            runner.walk()
            logging.info(f'"test_run" выполнен успешно')
        except TypeError:
            logging.warning(f"Неверный тип данных для объекта Runner")

if __name__ == "__main__":
    test = RunnerTest()
    test.test_walk()
    test.test_run()


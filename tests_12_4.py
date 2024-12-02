import logging
class RunnerTest:
    @staticmethod
    def test_walk():
        try:
            runner = Runner("Test Runner", speed=-5)
            runner.walk()
            logging.info(f'"test_walk" выполнен успешно')
        except:
            logging.warning(f"Неверная скорость для Runner")

    def test_run():
        try:
            runner = Runner(True, speed=10)
            runner.walk()
            logging.info(f'"test_run" выполнен успешно')
        except:
            logging.warning(f"Неверный тип данных для объекта Runner")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8'
                        format='%(asctime)s | %(levename)s | %(massage)s')

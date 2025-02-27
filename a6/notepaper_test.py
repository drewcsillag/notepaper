import unittest
import notepaper as p
import datetime


class TestAddingTodos(unittest.TestCase):
    def test_add_todos(self) -> None:
        orig = ["1", "2"]
        v = ["3", "4"]
        r = p.add_todos(orig, v)
        self.assertEqual(["1", "2", "3", "4"], r)

        orig = ["1", "", "2"]
        v = ["3"]
        r = p.add_todos(orig, v)
        self.assertEqual(["1", "3", "2"], r)
        # ensure that orig doesn't change
        self.assertEqual(["1", "", "2"], orig)

    def test_add_monthly_relative_day_negative(self) -> None:
        todos = {"Day,-1": ["t"]}

        self.assertEqual([], p.add_monthly_todos(datetime.date(2024, 1, 30), todos, []))

        self.assertEqual(
            ["t"], p.add_monthly_todos(datetime.date(2024, 1, 31), todos, [])
        )

        self.assertEqual([], p.add_monthly_todos(datetime.date(2024, 2, 1), todos, []))

    def test_add_monthly_relative_day_positive(self) -> None:
        todos = {"Day,1": ["t"]}

        self.assertEqual([], p.add_monthly_todos(datetime.date(2024, 1, 31), todos, []))
        self.assertEqual(
            ["t"], p.add_monthly_todos(datetime.date(2024, 2, 1), todos, [])
        )
        self.assertEqual([], p.add_monthly_todos(datetime.date(2024, 2, 2), todos, []))

    def test_add_monthly_first_monday(self) -> None:
        todos = {"Monday,1": ["t"]}

        self.assertEqual(
            [], p.add_monthly_todos(datetime.date(2023, 12, 31), todos, [])
        )
        self.assertEqual(
            ["t"], p.add_monthly_todos(datetime.date(2024, 1, 1), todos, [])
        )
        self.assertEqual([], p.add_monthly_todos(datetime.date(2024, 1, 2), todos, []))

    def test_add_monthly_last_monday(self) -> None:
        todos = {"Monday,-1": ["t"]}

        self.assertEqual([], p.add_monthly_todos(datetime.date(2023, 1, 22), todos, []))
        self.assertEqual(
            ["t"], p.add_monthly_todos(datetime.date(2024, 1, 29), todos, [])
        )

        self.assertEqual([], p.add_monthly_todos(datetime.date(2024, 1, 30), todos, []))

    def test_add_monthy_any_monday(self) -> None:
        todos = {"Monday,*": ["t"]}

        self.assertEqual([], p.add_monthly_todos(datetime.date(2024, 1, 21), todos, []))
        self.assertEqual(
            ["t"], p.add_monthly_todos(datetime.date(2024, 1, 22), todos, [])
        )
        self.assertEqual(
            ["t"], p.add_monthly_todos(datetime.date(2024, 1, 29), todos, [])
        )
        self.assertEqual([], p.add_monthly_todos(datetime.date(2024, 1, 30), todos, []))

    def test_yearly_first_monday(self) -> None:
        todos = {"yearly": [{"March,Monday,1": "t"}]}

        # monday in other month
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 1, 1)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 3, 3)))
        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 3, 4)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 3, 5)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 3, 11)))

    def test_yearly_last_weekday(self) -> None:
        todos = {"yearly": [{"March,Monday,-1": "t"}]}

        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 1, 29)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 3, 24)))
        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 3, 25)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 3, 26)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 3, 18)))

    def test_yearly_any_monday(self) -> None:
        todos = {"yearly": [{"March,Monday,*": "t"}]}

        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 1, 29)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 3, 24)))
        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 3, 25)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 3, 26)))
        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 3, 18)))

    def test_yearly_specific_date(self) -> None:
        todos = {"yearly": [{"March,Day,15": "t"}]}

        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 1, 15)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 3, 14)))
        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 3, 15)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 3, 16)))

    def test_alternate_monthly_any_monday(self) -> None:
        todos = {"yearly": [{"*,Monday,*": "t"}]}

        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 1, 29)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 3, 24)))
        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 3, 25)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 3, 26)))
        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 3, 18)))

    def test_alternate_monthly_last_monday(self) -> None:
        todos = {"yearly": [{"*,Monday,-1": "t"}]}
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 1, 22)))
        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 1, 29)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 1, 30)))

    def test_alternate_monthly_first_monday(self) -> None:
        todos = {"yearly": [{"*,Monday,1": "t"}]}
        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 1, 1)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2023, 12, 31)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 1, 2)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 1, 8)))

    def test_abbreviate_month_first_monday(self) -> None:
        todos = {"yearly": [{"Monday,1": "t"}]}
        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 1, 1)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2023, 12, 31)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 1, 2)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 1, 8)))

    def test_every_day_in_month(self) -> None:
        todos = {"yearly": [{"February,*,*": "t"}]}
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 1, 8)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 3, 8)))
        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 2, 8)))
        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 2, 14)))

    def test_mixing(self) -> None:
        todos = {
            "yearly": [
                {"*,Saturday,*": ["Chess"], "March,Saturday,*": ["Check MCTP F28R32"]}
            ]
        }
        self.assertEqual(
            ["Chess", "Check MCTP F28R32"],
            p.get_day_todos(todos, datetime.date(2024, 3, 2)),
        )

    def test_dont_mess_the_orgiginals(self):
        todos = {
            "yearly": [
                {
                    "February,Saturday,4": ["u"],  # ac
                    "Saturday,4": ["w"],  # endo
                }
            ]
        }
        cur = datetime.date(2025, 2, 1)
        for i in range(28):
            p.get_day_todos(todos, cur)
            cur += p.ONE_DAY
        self.assertEqual(["u"], todos["yearly"][0]["February,Saturday,4"])

    def test_interval(self) -> None:
        # Every two weeks starting on 2025-01-01
        todos = {"yearly": [{"2024-01-01,week,2": "t"}]}
        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 1, 1)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 1, 8)))
        self.assertEqual(["t"], p.get_day_todos(todos, datetime.date(2024, 1, 15)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 2, 8)))
        self.assertEqual([], p.get_day_todos(todos, datetime.date(2024, 2, 14)))

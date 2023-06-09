from typing import Any

import pandas as pd
import pendulum
import pytest

from simulation.utils import group_by_weekday

group_by_weekday_test_data = [
    {
        "today": pendulum.datetime(2023, 3, 19),
        "df": pd.DataFrame(
            {
                "date": [
                    "2023-02-19",
                    "2023-02-20",
                    "2023-02-21",
                    "2023-02-22",
                    "2023-02-23",
                    "2023-02-24",
                    "2023-02-25",
                    "2023-02-26",
                    "2023-02-27",
                    "2023-02-28",
                    "2023-03-01",
                    "2023-03-02",
                    "2023-03-03",
                    "2023-03-04",
                    "2023-03-05",
                    "2023-03-06",
                    "2023-03-07",
                    "2023-03-08",
                    "2023-03-09",
                    "2023-03-10",
                    "2023-03-11",
                    "2023-03-12",
                    "2023-03-13",
                    "2023-03-14",
                    "2023-03-15",
                    "2023-03-16",
                    "2023-03-17",
                    "2023-03-18",
                ],
                "count": [
                    5,
                    3,
                    2,
                    6,
                    5,
                    3,
                    7,
                    3,
                    8,
                    1,
                    4,
                    6,
                    3,
                    9,
                    2,
                    4,
                    5,
                    6,
                    7,
                    2,
                    3,
                    5,
                    8,
                    9,
                    3,
                    5,
                    6,
                    7,
                ],
            }
        ),
        "want": [
            [0, 3, 8, 4],
            [0, 2, 1, 5],
            [0, 6, 4, 6],
            [0, 5, 6, 7],
            [0, 3, 3, 2],
            [0, 7, 9, 3],
            [5, 3, 2, 5],
        ],
    },
    {
        "today": pendulum.datetime(2023, 3, 18),
        "df": pd.DataFrame(
            {
                "date": [
                    "2023-02-18",
                    "2023-02-19",
                    "2023-02-20",
                    "2023-02-21",
                    "2023-02-22",
                    "2023-02-23",
                    "2023-02-24",
                    "2023-02-25",
                    "2023-02-26",
                    "2023-02-27",
                    "2023-02-28",
                    "2023-03-01",
                    "2023-03-02",
                    "2023-03-03",
                    "2023-03-04",
                    "2023-03-05",
                    "2023-03-06",
                    "2023-03-07",
                    "2023-03-08",
                    "2023-03-09",
                    "2023-03-10",
                    "2023-03-11",
                    "2023-03-12",
                    "2023-03-13",
                    "2023-03-14",
                    "2023-03-15",
                    "2023-03-16",
                    "2023-03-17",
                ],
                "count": [
                    2,
                    5,
                    3,
                    2,
                    6,
                    5,
                    3,
                    7,
                    3,
                    8,
                    1,
                    4,
                    6,
                    3,
                    9,
                    2,
                    4,
                    5,
                    6,
                    7,
                    2,
                    3,
                    5,
                    8,
                    9,
                    3,
                    5,
                    6,
                ],
            }
        ),
        "want": [
            [0, 3, 8, 4],
            [0, 2, 1, 5],
            [0, 6, 4, 6],
            [0, 5, 6, 7],
            [0, 3, 3, 2],
            [2, 7, 9, 3],
            [5, 3, 2, 5],
        ],
    },
    {
        "today": pendulum.datetime(2023, 3, 15),
        "df": pd.DataFrame(
            {
                "date": [
                    "2023-02-15",
                    "2023-02-16",
                    "2023-02-17",
                    "2023-02-18",
                    "2023-02-19",
                    "2023-02-20",
                    "2023-02-21",
                    "2023-02-22",
                    "2023-02-23",
                    "2023-02-24",
                    "2023-02-25",
                    "2023-02-26",
                    "2023-02-27",
                    "2023-02-28",
                    "2023-03-01",
                    "2023-03-02",
                    "2023-03-03",
                    "2023-03-04",
                    "2023-03-05",
                    "2023-03-06",
                    "2023-03-07",
                    "2023-03-08",
                    "2023-03-09",
                    "2023-03-10",
                    "2023-03-11",
                    "2023-03-12",
                    "2023-03-13",
                    "2023-03-14",
                ],
                "count": [
                    4,
                    2,
                    6,
                    5,
                    3,
                    2,
                    6,
                    5,
                    3,
                    7,
                    3,
                    8,
                    1,
                    4,
                    6,
                    3,
                    9,
                    2,
                    4,
                    5,
                    6,
                    7,
                    2,
                    3,
                    5,
                    8,
                    9,
                    3,
                ],
            }
        ),
        "want": [
            [0, 2, 1, 5],
            [0, 6, 4, 6],
            [4, 5, 6, 7],
            [2, 3, 3, 2],
            [6, 7, 9, 3],
            [5, 3, 2, 5],
            [3, 8, 4, 8],
        ],
    },
]


@pytest.mark.parametrize("test_case", group_by_weekday_test_data)
def test_group_by_weekday(test_case: Any):
    # Arrange
    today = test_case["today"]
    df = test_case["df"]
    want = test_case["want"]

    # Act
    actual = group_by_weekday(today, df)

    # Assert
    print(actual)
    assert actual == want

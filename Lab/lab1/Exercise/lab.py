# lab.py


from pathlib import Path
import io
import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# QUESTION 0
# ---------------------------------------------------------------------


def consecutive_ints(ints):
    abs_diff = np.abs(np.diff(ints))
    return 1 in abs_diff


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def median_vs_mean(nums):
    sorted_nums = sorted(nums)
    length = len(nums)
    if length % 2 == 1:
        median = sorted_nums[length // 2]
    else:
        median = (sorted_nums[length // 2 - 1] + sorted_nums[length // 2]) / 2
    mean = sum(nums) / length
    return median <= mean

# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def same_diff_ints(ints):
    n = len(ints)
    for i in range(n):
        for j in range(1, n - i):
            if abs(ints[i] - ints[i + j]) == j:
                return True
    return False


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def n_prefixes(s, n):
    string = ""
    for i in range(n):
        string += s[0 : i + 1]
    return string


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def exploded_numbers(ints, n):
    result = []
    num_max = max(ints) + n
    width = len(str(num_max))
    for num in ints:
        exploded = [str(num + i).zfill(width) for i in range(-1 * n, n + 1, 1)]
        result.append(' '.join(exploded))
    return result



# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def add_root(A):
    length = len(A)
    root = np.arange(length) ** 0.5
    return root + A

def where_square(A):
    return np.sqrt(A) % 1 == 0 


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def growth_rates(A):
    result = [((A[i+1] - A[i]) / A[i]) * 100 for i in range(len(A) - 1)]
    return [round(num, 2) for num in result]
    # return result

def with_leftover(A):
    init_value = 20
    leftover_day = init_value % A
    leftover_sum = leftover_day.cumsum()
    day = np.where(leftover_sum > A)
    if day[0].size == 0 :
        return -1
    else :
        return day[0][0]

# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def salary_stats(salary):
    num_players = salary.shape[0]
    num_teams = len(salary['Team'].unique())
    total_salary = salary['Salary'].sum()
    highest_salary = salary.loc[salary['Salary'].idxmax(), 'Player']
    avg_los = round(salary[salary['Team'] == 'Los Angeles Lakers']['Salary'].mean(), 2)
    fifth_lowest_person = salary.sort_values(by='Salary', ascending=True).iloc[4]
    fifth_lowest = f"{fifth_lowest_person['Player']}, {fifth_lowest_person['Team']}"

    last_name = salary['Player'].str.split().str[1]
    duplicates= True in last_name.duplicated()

    highest_paid_team = salary.loc[salary['Salary'].idxmax(), 'Team']
    total_highest = salary[salary['Team'] == highest_paid_team]['Salary'].sum()
    stats = pd.Series({
        'num_players': num_players,
        'num_teams': num_teams,
        'total_salary': total_salary,
        'highest_salary': highest_salary,
        'avg_los': avg_los,
        'fifth_lowest': fifth_lowest,
        # 'highest_paid_team': highest_paid_team,
        'duplicates': duplicates,
        'total_highest': total_highest
    })
    return stats
    




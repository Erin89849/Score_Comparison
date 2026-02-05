'''

This code compares final scores from Google Sheets.

Written by: Erin Olson

'''

import numpy as np
import pandas as pd
from google.colab import drive
import os
import gspread
from google.auth import default
from google.colab import auth


def get_final_scores(sheet: gspread.spreadsheet.Spreadsheet, teams: list[str], cell: str) -> list[int]:
    '''

    This function will get the final scores for all teams from Google Sheet.
    - sheet: Google Sheet to get scores from,
    - teams: list of team names (sheet names),
    - cell: cell with final score,
    - returns: list of scores for each team.

    '''

    final_scores = []
    num_teams = len(teams)

    # Getting the final scores
    for i in range(num_teams):
        team_name = teams[i]
        score_value = sheet.worksheet(team_name).acell(cell).value
        final_scores.append(int(score_value))

    return final_scores


def compare_final_scores(final_score1: list[int], final_score2: list[int], teams: list[str]) -> int:
    '''

    This function will compare the final scores of two Google Sheets.
    - final_score1: list of final scores for sheet 1,
    - final_score2: list of final scores for sheet 2,
    - teams: list of team names (sheet names),
    - returns: 0 (team scores are not the same) or 1 (team scores are the same).

    '''

    print('Comparing final scores...\n')

    # Confirming final scores are the same length
    len_1 = len(final_score1)
    len_2 = len(final_score2)

    # Comparison parameters
    bad = 0
    good = 0
    all_good = 0

    # Comparison
    if len_1 != len_2:   # Not the same length
        print('Cannot compare scores, check the number of values!')
    else:

        # Comparing the scores
        for i in range(len_1):

            # Initalizing values
            score_1 = final_score1[i]
            score_2 = final_score2[i]
            team_name = teams[i]

            # Comparing scores
            if score_1 != score_2:   # Scores do not match
                print(f'Team: {team_name} has a different score :(')
                print(f'Score 1: {score_1}')
                print(f'Score 2: {score_2}')
                print('\n')
                bad += 1

            else:   # Scores match
                good += 1

    # All scores the same!
    if good == len_1:
        print('| All final scores, for all teams, is the same! |\n')
        all_good = 1

    return all_good


def winning_team(final_scores: list[int], teams: list[str], good_comparison: int) -> str:
    '''

    This function will determine the winning team! (Does not account for ties currently)
    - final_scores: list of final scores,
    - teams: team names,
    - good_comparison: if comparison of scores between two sheets is the same,
    - returns: winning team name.

    '''

    # Ensuring the scores are consistent
    if good_comparison != 1:
        return 'Check scores again, they are not consistent :('
    else:
        num_teams = len(teams)
        num_scores = len(final_scores)

        # Ensuring lists are the correct lengths
        if num_teams != num_scores:
            return 'Incorrect length of team names or final scores!'
        else:
            print('The winning team is...')
            largest_score = 0
            largest_score_index = 0
            for i in range(num_scores):
                current_score = final_scores[i]

                # Finding the largest score
                if current_score >= largest_score:
                    largest_score = current_score
                    largest_score_index = i

    winning_team = teams[largest_score_index]

    return winning_team


def overall_scores(sheet_1: gspread.spreadsheet.Spreadsheet, sheet_2: gspread.spreadsheet.Spreadsheet, category: str, team_names: list[str], cell: str) -> None:
    '''

    This function will show if the scores are the same between the sheets and the winner of said category.
    - sheet_1: sheet 1 with scores,
    - sheet_2: sheet 2 with scores,
    - category: category to compare,
    - team_name: list of team names,
    - cell: cell with final final score in sheet,
    - returns: None.

    '''

    print('=======================================================================\n')
    print(f'Category: {category}\n')

    # Getting final scores
    final_scores_1 = get_final_scores(sheet_1, team_names, cell)
    final_scores_2 = get_final_scores(sheet_2, team_names, cell)

    # Comparing final scores between sheets
    comparison = compare_final_scores(final_scores_1, final_scores_2, team_names)

    # Determining the winner
    winner_winner_chicken_dinner = winning_team(final_scores_1, team_names, comparison)
    print(f'\n{winner_winner_chicken_dinner}!\n')

    print('=======================================================================\n')


def main():
    '''

    Example use case :)

    '''

    # Authentication for Google Drive
    auth.authenticate_user()
    creds, _ = default()
    gc = gspread.authorize(creds)

    # Establishing connection to sheets
    sheet_1 = gc.open_by_url('https://example1.url.com')
    sheet_2 = gc.open_by_url('https://example2.url.com')

    # Calculating overall scores
    teams = ['team1', 'team2', 'team3']
    category = 'food'
    final_score_cell = 'A1'
    overall_scores(sheet_1, sheet_2, category, teams, final_score_cell)


if __name__ == '__main__ ':
    main()

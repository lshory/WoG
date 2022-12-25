from Utils import *


def add_score(difficulty):
    score_file = open(SCORES_FILE_NAME, 'r')
    points_of_winning = int(score_file.read()) + (int(difficulty) * 3) + 5
    score_file.close()
    score_file = open(SCORES_FILE_NAME, 'w')
    score_file.write(str(points_of_winning))
    score_file.close()
    return points_of_winning


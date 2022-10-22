import random


def get_question():
    with open("Questions.txt", "r") as qfile:
        file_lines = qfile.readlines()
        q_list = [line.strip() for line in file_lines]
    return random.choice(q_list)


if __name__ == '__main__':
    print(get_question())

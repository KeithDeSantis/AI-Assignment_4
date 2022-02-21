from qtable import QTable


def main(filename=None, time_to_run=None, probablity_moving=None, constant_reward=None):
    qtable = QTable()
    qtable['0,0'] = [0, 0, 0, 0]
    print(qtable.get('0,0'))


if __name__ == "__main__":
    main()

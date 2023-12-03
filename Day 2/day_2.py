def read_input():
    f = open("day_2_input.txt", "r")
    return f

def get_game_balls(game):
    dict = {'red': 0, 'green': 0, 'blue': 0}
    game_id, game = game.split(':')
    game_id = int(game_id.split()[1])
    game = game.replace(';', ',')
    balls = game.split(',')
    for ball in balls:
        count = int(ball.split()[0])
        color = ball.split()[1]
        dict[color] = max(dict[color], count)
    return game_id, dict

def check_game_balls_condition(game_balls):
    if game_balls['red'] > 12:
        return False
    if game_balls['green'] > 13:
        return False
    if game_balls['blue'] > 14:
        return False
    return True

def main():
    input = read_input()
    result = 0
    for line in input:
        game_id, game_balls = get_game_balls(line)
        print(game_id, game_balls)
        if check_game_balls_condition(game_balls):
            result += game_id
    print(result)


if __name__ == '__main__':
    main()
user_input = [' '] * 9
coordinates = ['1 3', '2 3', '3 3', '1 2', '2 2', '3 2',
               '1 1', '2 1', '3 1']
numbers = '0123456789'
count = 0

def render(state):
    result = '-' * 9 + '\n'
    while len(state) > 0:
        result += '| ' + ' '.join(state[:3]) + ' |\n'
        state = state[3:]
    result += '-' * 9
    return result


def line_analyze(matrix):
    if matrix.count('XXX') and matrix.count('OOO'):
        return 'Impossible'
    if matrix.count('XXX') == 1:
        return 'X wins'
    if matrix.count('XXX') > 1:
        return 'Impossible'
    if matrix.count('OOO') == 1:
        return 'O wins'
    if matrix.count('OOO') > 1:
        return 'Impossible'
    return None


def gorizontal_analyze(state):
    matrix = []
    while len(state) > 0:
        matrix.append(''.join(state[:3]))
        state = state[3:]
    return line_analyze(matrix)


def vertical_analyze(state):
    matrix = [state[i] + state[i + 3] + state[i + 6] for i in range(3)]
    return line_analyze(matrix)


def state_analyze(state):
    if abs(state.count('X') - state.count('O')) > 1:
        return 'Impossible'
    if (state[0] + state[4] + state[8] == 'XXX' or
            state[2] + state[4] + state[6] == 'XXX'):
        return 'X wins'
    if (state[0] + state[4] + state[8] == 'OOO' or
            state[2] + state[4] + state[6] == 'OOO'):
        return 'O wins'
    if gorizontal_analyze(state) is not None:
        return gorizontal_analyze(state)
    if vertical_analyze(state) is not None:
        return vertical_analyze(state)
    if state.count(' ') == 0:
        return 'Draw'
    return


while state_analyze(user_input) is None:
    print(render(user_input))
    while True:
        xy = input('Enter the coordinates:').split()
        if xy[0] not in numbers or xy[1] not in numbers:
            print('You should enter numbers!')
        elif not 1 <= int(xy[0]) <= 3 or not 1 <= int(xy[1]) <= 3:
            print('Coordinates should be from 1 to 3!')
        elif user_input[coordinates.index(' '.join(xy))] != ' ':
            print('This cell is occupied! Choose another one!')
        else:
            break
    if count % 2:
        user_input[coordinates.index(' '.join(xy))] = 'O'
    else:
        user_input[coordinates.index(' '.join(xy))] = 'X'
    count += 1
else:
    print(render(user_input))
    print(state_analyze(user_input))



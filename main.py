# -*- coding: utf-8 -*-

"""Übungsblatt 04"""

# Vorgegebener Code (Hier nichts verändern)

EXAMPLE_GRID_1 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

EXAMPLE_GRID_2 = [
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [2, 0, 2, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 2],
    [1, 2, 2, 1, 0, 2, 1]
]

EXAMPLE_GRID_3 = [
    [2, 2, 1, 1, 2, 2, 2],
    [2, 1, 2, 2, 1, 1, 1],
    [1, 2, 1, 2, 1, 2, 2],
    [2, 1, 2, 1, 1, 1, 2],
    [1, 2, 2, 1, 2, 1, 2],
    [1, 1, 2, 2, 1, 1, 1]
]

EXAMPLE_GRID_4 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1],
    [1, 2, 2, 2, 2, 1, 2],
    [1, 1, 2, 1, 1, 2, 2],
    [2, 1, 2, 2, 1, 2, 1]
]

EXAMPLE_GRID_5 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 2, 0],
    [0, 0, 1, 0, 0, 2, 2],
    [0, 1, 1, 1, 0, 2, 1],
    [1, 2, 1, 2, 2, 1, 2]
]

EXAMPLE_GRID_6 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0],
    [2, 0, 1, 2, 2, 0, 0],
    [2, 1, 2, 1, 1, 0, 2],
    [1, 2, 1, 1, 2, 1, 1]
]

EXAMPLE_GRID_7 = [
    [0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0],
    [1, 2, 2, 2, 0, 2, 0],
    [1, 2, 2, 2, 0, 2, 2],
    [2, 1, 2, 2, 1, 1, 1],
    [1, 2, 1, 1, 2, 1, 2]
]


def clear_screen():
    """Clear screen

    Depending on the user's terminal window configuration, there might
    still be output from previous operations visible on the screen. To
    clear the screen, 100 newline characters will be printed.
    """
    print("\n" * 100)


def player_has_won(grid):
    """Find out if the grid contains a winning combination

    To win, four adjacent spaces have to be occupied by the same
    player. They count as adjacent if they are aligned diagonally,
    horizontally or vertically.
    """
    row_count = len(grid)
    column_count = len(grid[0])
    for row_number in range(row_count):
        for column_number in range(column_count):
            if grid[row_number][column_number] == 0:
                continue
            four_in_a_row = map(all_elements_equal, [
                get_four_horizontal(row_number, column_number, grid),
                get_four_vertical(row_number, column_number, grid),
                get_four_diagonal_up(row_number, column_number, grid),
                get_four_diagonal_down(row_number, column_number, grid)
            ])
            if any(four_in_a_row):
                return True
    return False


def game_loop():
    """Run the game loop

    As long as the loop runs, players can select columns to occupy
    spaces. The loop will exit once the grid is full or a player wins
    the game.
    """
    grid = empty_grid()
    player = None
    while True:
        clear_screen()
        print_grid(grid)
        if grid_is_full(grid):
            print("It's a draw!")
            break
        if player_has_won(grid):
            print("Player {} has won!".format(player))
            break
        player = next_player(player)
        player_choice(player, grid)


# Hier beginnt der Code, welcher zum Lösen der Aufgaben bearbeitet werden soll:

# Aufgabe 1

def empty_grid():
    """
    eine Repräsentation der Spieldaten
    Das Spielbrett besteht aus einem Raster mit 6 Reihen (Zeilen) und 7 Spalten.
    Es kann daher sehr anschaulich von einer 6x7 Matrix dargestellt werden.

    :return: eine mehrdimensionale Liste
    :rtype: list
    """
    grid = [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
    return grid


# Aufgabe 2

def print_grid(grid):
    """
    Die Funktion soll die in grid gespeicherten Spieldaten ausgeben.

    :param grid:
    :type grid: list
    :return:
    """
    print("+---------------+")
    for row in grid:
        print("| ", end="")
        for space in row:
            if space == 1:
                print("X ", end="")
            elif space == 2:
                print("O ", end="")
            else:
                print("  ", end="")
        print("|")

    print("+---------------+")
    print("  1 2 3 4 5 6 7 ")


# Aufgabe 3

def get_column(column_number, grid):
    """
    Die Werte der Matrix, welche das Spielbrett repräsentiert,
    sind in grid jeweils in Reihen abgelegt.
    Um eine Liste mit den Werten einer Spalte der Matrix zu erhalten ist diese Funktion nötig.

    :param column_number: angegebene Spalte der Matrix
    :type column_number
    :param grid:
    :return:
    """
    column = []
    for i in grid:
        column.append(i[column_number])
    return column


# Aufgabe 4

def free_space(column_number, grid):
    """
    Die Funktion wird mit column_number angegebene Spalte
    auf ein freies Feld überprüft. Ist kein Feld mehr frei, wird None zurückgegeben.
    Ist noch ein Feld frei, dann wird der Index zurückgegeben,
    mit dem man in grid auf diese Reihe zugreifen kann.

    :param column_number: angegebene Spalte
    :param grid:
    :return: der Index derjenigen Reihe, welche in der angegebenen Spalte
    von unten gesehen als Erstes ein freies Feld besitzt
    """
    column = get_column(column_number, grid)

    for row_index in range(len(column) - 1, -1, -1):
        if column[row_index] == 0:
            return row_index
    return None


# Aufgabe 5

def grid_is_full(grid):
    """
    Um herauszufinden, ob das Spiel in einem Unentschieden geendet ist,
    prüfen wir, ob auf dem Spielbrett überhaupt noch irgendwo freie Felder sind.


    :param grid:
    :type grid: list
    :return: True, wenn kein Feld mehr frei ist
    False, wenn noch mindestens ein Feld frei ist.
    :rtype: bool
    """
    column_count = len(grid[0])

    for column_number in range(column_count):
        if free_space(column_number, grid) is not None:
            return False
    return True


# Aufgabe 6

def drop_disc(column_number, player, grid):
    """
    In dieser Funktion wird eine „Scheibe“ in die angegebene Spalte eingeworfen.

    :param column_number: angegebene Spalte
    :param player: der aktuelle Spieler
    :param grid:
    :return: ist in der vom Spieler gewählten Spalte kein Feld mehr frei - False
    Falls der Wert hingegen erfolgreich gespeichert werden konnte - True
    :rtype: bool
    """

    row_number = free_space(column_number, grid)
    if row_number is not None:
        grid[row_number][column_number] = player
        return True
    return False


# Aufgabe 7

def all_elements_equal(sequence):
    """
    Diese Funktion soll prüfen, ob alle Elemente
    der als sequence übergebenen Liste gleich sind.

    :param sequence:
    :type sequence: list
    :return: Falls ja - True
    falls nicht - False
    :rtype: bool
    """

    if isinstance(sequence, list):
        if all(element == sequence[0] for element in sequence):
            return True
    return False


# Aufgabe 8

def get_four_diagonal_up(row_number, column_number, grid):
    """

    :param row_number:
    :param column_number:
    :param grid:
    :return:
    """
    # For function `get_four_diagonal_up` we might produce negative
    # list indices which are not allowed but don't raise `IndexError`.
    # Hint: This is not necessary for `get_four_diagonal_down`,
    # `get_four_horizontal` or `get_four_vertical` because all
    # indices will be equal or greater than `row_number`.
    if row_number - 3 < 0 or column_number + 3 >= len(grid[0]):
        return None
    try:
        return [
            # We want four spaces diagonally adjacent to the given
            # coordinates in `row_number` and `column_number`. For
            # each additional space we have to walk up a row (subtract
            # 1 for each row) and walk one column to the right (add
            # 1 for each column).
            grid[row_number][column_number],
            grid[row_number - 1][column_number + 1],
            grid[row_number - 2][column_number + 2],
            grid[row_number - 3][column_number + 3]
        ]
    except IndexError:
        return None


def get_four_diagonal_down(row_number, column_number, grid):
    """

    :param row_number:
    :param column_number:
    :param grid:
    :return:
    """
    if row_number + 3 >= len(grid) or column_number + 3 >= len(grid[0]):
        return None
    try:
        return [
            grid[row_number][column_number],
            grid[row_number + 1][column_number + 1],
            grid[row_number + 2][column_number + 2],
            grid[row_number + 3][column_number + 3]
        ]
    except IndexError:
        return None


def get_four_horizontal(row_number, column_number, grid):
    """

    :param row_number:
    :param column_number:
    :param grid:
    :return:
    """
    if column_number + 3 >= len(grid[0]):
        return None
    try:
        return [
            grid[row_number][column_number],
            grid[row_number][column_number + 1],
            grid[row_number][column_number + 2],
            grid[row_number][column_number + 3]
        ]
    except IndexError:
        return None


def get_four_vertical(row_number, column_number, grid):
    """

    :param row_number:
    :param column_number:
    :param grid:
    :return:
    """
    if row_number + 3 > len(grid):
        return None
    try:
        return [
            grid[row_number][column_number],
            grid[row_number + 1][column_number],
            grid[row_number + 2][column_number],
            grid[row_number + 3][column_number]
        ]
    except IndexError:
        return None


# Aufgabe 9

def next_player(player):
    """
    Wenn der übergebene Parameter player den Wert 1 enthält,
     soll 2 zurückgegeben werden. In allen anderen Fällen 1.

    :param player:
    :return:
    """
    if player == 1:
        return 2
    return 1


# Aufgabe 10

def player_choice(player, grid):
    """

    :param player:
    :param grid:
    :return:
    """

    print("Next disc: Player {}".format(player))
    while True:
        player_input_str = input("Which column? ")

        try:
            # Convert input to integer
            player_input_int = int(player_input_str)
            # List index starts at 0, so we have to subtract 1
            column_number = player_input_int - 1
            # Drop disc into selected column
            if not drop_disc(column_number, player, grid):
                print("Can not drop disc there")
                continue
            # No errors occurred, so we can break the loop
            break
        except ValueError:
            print("Du musst eine Zahl zwischen 1 und 8 eingebeneingeben")




# Testaufrufe

if __name__ == "__main__":
    print("Test Aufgabe 1:")
    # print(empty_grid())

    print("Test Aufgabe 2:")
    # print_grid(EXAMPLE_GRID_1)
    # print_grid(EXAMPLE_GRID_2)
    # print_grid(EXAMPLE_GRID_3)

    print("Test Aufgabe 3:")
    # print(get_column(0, EXAMPLE_GRID_3))

    print("Test Aufgabe 4:")
    # print(free_space(1, EXAMPLE_GRID_2))
    # print(free_space(2, EXAMPLE_GRID_2))

    print("Test Aufgabe 5:")
    # print(grid_is_full(EXAMPLE_GRID_1))
    # print(grid_is_full(EXAMPLE_GRID_2))
    # print(grid_is_full(EXAMPLE_GRID_3))

    print("Test Aufgabe 6:")
    # print(drop_disc(2, 1, EXAMPLE_GRID_2))
    # print("EXAMPLE_GRID_2 vorher:")
    # print_grid(EXAMPLE_GRID_2)
    # print(drop_disc(1, 1, EXAMPLE_GRID_2))
    # print("EXAMPLE_GRID_2 hinterher:")
    # print_grid(EXAMPLE_GRID_2)

    print("Test Aufgabe 7:")
    # print(all_elements_equal([1, 2, 3]))
    # print(all_elements_equal(None))
    # print(all_elements_equal([1, 1, 1]))
    # print(all_elements_equal([True, True, True]))
    # print(all_elements_equal([False, False, False]))

    print("Test Aufgabe 8:")
    print(player_has_won(EXAMPLE_GRID_1))
    print(player_has_won(EXAMPLE_GRID_2))
    print(player_has_won(EXAMPLE_GRID_3))
    print(player_has_won(EXAMPLE_GRID_4))
    print(player_has_won(EXAMPLE_GRID_5))
    print(player_has_won(EXAMPLE_GRID_6))
    print(player_has_won(EXAMPLE_GRID_7))

    print("Test Aufgabe 9:")
    # print(next_player(None))
    # print(next_player(1))
    # print(next_player(2))

    print("Test Aufgabe 10:")
    # game_loop()

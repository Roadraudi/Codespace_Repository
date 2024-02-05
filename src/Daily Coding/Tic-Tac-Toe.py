
def show_spielbrett(spielbrett):
    for zeile in spielbrett:
        print("|".join(zeile))
        print("_____")

def check_winner(board, player):
    # Überprüfung der Reihen und Spalten
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Überprüfung der Diagonalen
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_move():
    while True:
        try:
            move = int(input("Gib deine Position (1-9) ein: "))
            if 1 <= move <= 9:
                return divmod(move - 1, 3)
            else:
                print("Ungültige Eingabe. Bitte wähle eine Zahl zwischen 1 und 9.")
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine ganze Zahl ein.")

def play():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    while True:
        show_spielbrett(board)

        row, col = get_move()

        if board[row][col] == ' ':
            board[row][col] = players[current_player]

            if check_winner(board, players[current_player]):
                show_spielbrett(board)
                print(f"Spieler {players[current_player]} hat gewonnen!")
                break
            elif is_board_full(board):
                show_spielbrett(board)
                print("Unentschieden! Das Spielfeld ist voll.")
                break

            current_player = 1 - current_player  # Spielerwechsel
        else:
            print("Diese Position ist bereits belegt. Wähle eine andere.")

if __name__ == "__main__":
    play()
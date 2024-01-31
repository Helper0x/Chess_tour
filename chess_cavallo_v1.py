# 12.01.23

# Import
import time
import numpy as np

# Variable
dim_scacchiera = 8
numero_per_colonna_non_passata = -1
numero_per_cavallo = 0
cavallo_position = [0, 0]
conta_combianzioni = 0


possible_movements = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

def print_table(matrice):
    for row in matrice:
        print(" | ".join(map(lambda x: f"{x:02d}", row)))

def is_next_move_valid(matrice, row, col):

    # Se nel campo
    if 0 <= row and row < len(matrice) and 0 <= col and col < len(matrice[0]):

        # Se non passata
        return matrice[row][col] == numero_per_colonna_non_passata
    return False

def solve_puzzle(matrice, start_x, start_y, mov_count):

    global conta_combianzioni

    # Caso base
    if mov_count == dim_scacchiera * dim_scacchiera:
        return True

    # For all possibili mosse
    for move in possible_movements:

        # Get row and column per prossima mossa
        next_x = start_x + move[0]
        next_y = start_y + move[1]

        # Se valida
        if is_next_move_valid(matrice, next_x, next_y):
            
            # Asegna numero per sequenza percorso
            matrice[next_x][next_y] = mov_count
            conta_combianzioni += 1

            # Se risolto tutto
            if solve_puzzle(matrice, next_x, next_y, mov_count+1):
                return True

            else:

                # Se la ricorsione non ha avuto successo, annulla la scarta questa strada
                matrice[next_x][next_y] = numero_per_colonna_non_passata

    # Nessuna soluzione trovata in questa direzione, torna indietro (backtrack)
    return False

def run():

    # Creation tabella
    matrice = np.full((dim_scacchiera, dim_scacchiera), numero_per_colonna_non_passata, dtype=np.int32).tolist()

    # Aseggnazione cavallo
    matrice[cavallo_position[0]][cavallo_position[1]] = numero_per_cavallo

    print("START:")
    print_table(matrice)
    print("\n")

    if solve_puzzle(matrice, cavallo_position[0], cavallo_position[1], 1):  # Se 0 esplode
        print("END:")
        print_table(matrice)
    else:
        print("Nessuna soluzione trovata.")
    
    print("COMBINAZINI PROVATE => ", conta_combianzioni)

if __name__ == '__main__':
    t_start = time.time()
    run()
    print(f"TIME EXECUTION => {time.time() - t_start}")

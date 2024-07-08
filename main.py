import FEnotation
import coords
import stockfish_wrapper
import stockfish_wrapper2
import CheckCoords
import socket
import time
import random

HOST = "192.168.125.123"
PORT = 65432

prev = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
#?prev = "rnbqkbnr/pppppppp/8/8/8/8/8/Q6K"

#prev = FEnotation.get_fen(prev, curx)
print("")

count = 1
sez = []


def send_coords(c_socket, coords:list):
    c_socket.sendall(coords[0].encode())
    time.sleep(0.1)
    c_socket.sendall(coords[1].encode())
    time.sleep(0.1)
    c_socket.sendall(coords[2].encode())
    time.sleep(0.1)

    c_socket.sendall(coords[3].encode())
    time.sleep(0.1)
    c_socket.sendall(coords[4].encode())
    time.sleep(0.1)
    c_socket.sendall(coords[5].encode())
    time.sleep(0.1)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen(5)
print(f'Server listening on {HOST}:{PORT}')

GotMove = False


while True:
    client_socket, addr = server_socket.accept()
    while True:
        if GotMove == False:
            sez = []

                #coords.get_coords()

            if count % 2 == 1: #+ k:  #poteza za dobrega

                stock = stockfish_wrapper.get_move(prev + " w")
                move, temp = stock[0],  stock[1]
                if CheckCoords.check_square(prev, move[2:])!=True:
                    sez.append(coords.get_coords(move[:2]))
                    sez[0].append(CheckCoords.Piece_height(prev, move[:2]))
                    sez.append(coords.get_coords(move[2:]))
                    sez[1].append(CheckCoords.Piece_height(prev, move[2:]))
                else:
                    sez.append(coords.get_coords(move[2:]))
                    sez[0].append(CheckCoords.Piece_height(prev, move[2:]))
                    sez.append((0, 650, 0))
                    sez.append(coords.get_coords(move[:2]))
                    sez[2].append(CheckCoords.Piece_height(prev, move[:2]))
                    sez.append(coords.get_coords(move[2:]))
                    sez[3].append(CheckCoords.Piece_height(prev, move[2:]))
                
                
                #?print(CheckCoords.Piece_height(prev, move[:2]))
                print(move)
                #! sez.clear()      # napaka hall of fame
                h = (CheckCoords.Piece_height(prev, move[:2]))
                prev = temp
                count += 1
                GotMove = True

            else: #poteza za dobrega

                stock = stockfish_wrapper2.get_bad_move(prev + " b")
                move, temp = stock[0],  stock[1]
                if CheckCoords.check_square(prev, move[2:])!=True:
                    sez.append(coords.get_coords(move[:2]))
                    sez[0].append(CheckCoords.Piece_height(prev, move[:2]))
                    sez.append(coords.get_coords(move[2:]))
                    sez[1].append(CheckCoords.Piece_height(prev, move[2:]))
                else:
                    sez.append(coords.get_coords(move[2:]))
                    sez[0].append(CheckCoords.Piece_height(prev, move[2:]))
                    sez.append((0, 650, 0))
                    sez.append(coords.get_coords(move[:2]))
                    sez[2].append(CheckCoords.Piece_height(prev, move[:2]))
                    sez.append(coords.get_coords(move[2:]))
                    sez[3].append(CheckCoords.Piece_height(prev, move[2:]))
                    
                #? print(CheckCoords.Piece_height(prev, move[:2]))

                print(move)
                #! sez.clear()          # napaka hall of fame
                #h = (CheckCoords.Piece_height(prev, move[:2]))
                prev = temp
                count += 1
                GotMove = True

        try:
            # dobimo podatke od roke
            data = client_socket.recv(1024).decode('utf-8') # 1MB max
            if not data:
                break

            if data == "move":
                cords = []
                print(data)
                time.sleep(0.3)
                for i in range (0, 2):
                    print(sez)
                    cords.append(str(sez[0][0]))
                    cords.append(str(sez[0][1]))
                    cords.append(str(sez[0][2]))
                    sez.pop(0)
            
            if len(sez)==0:
                GotMove = False
                
            print(cords)
            send_coords(client_socket, cords)

                    

        except Exception as e:
            send_coords(client_socket, ["E", 0, 0])
            send_coords(client_socket, ["E", 0, 0])

        





# EXAMPLES
#e7: (161, 241)
#e5: (161, 161)
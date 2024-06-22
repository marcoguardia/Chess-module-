#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:05:36 2024

@author: marcoguardia
"""

class Chess:
    def __init__(self, board=None, turn='white', check=False, move_history=[]):
        """
        Método constructor del objeto Chess. 
        
        Parámetros: 
            board: list
                Lista con la posición actual, donde el índice 0 es la casilla a1, el dos la casilla a2 y así
                sucesivamente. Se pone por default en la posición inicial.
            turn: str
                Jugador al que le toca jugar dada la posición. Se pone por default en white
            move_history: list
                Historial de jugadas del juego. Se inicializa por default como una lista vacía
                AGREGAR CHECK
            
        """
        if board is None: 
            self.__board = [
                'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R',
                'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P',
                '.', '.', '.', '.', '.', '.', '.', '.',
                '.', '.', '.', '.', '.', '.', '.', '.',
                '.', '.', '.', '.', '.', '.', '.', '.',
                '.', '.', '.', '.', '.', '.', '.', '.',
                'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p',
                'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'
                ]   #En minúsucla piezas negras, mayúscula piezas blancas
        
        else: 
            self.__board=board
            
            
        self.__turn=turn
        self.__move_history=move_history
        
        
        self.__check=False
        
        self.__piece_values = {
            "p": 1, "n": 3, "b": 3, "r": 5, "q": 9, "k": 0,
            "P": -1, "N": -3, "B": -3, "R": -5, "Q": -9, "K": 0
        }

        
    
    def print_board(self):
        """
        Imprime el tablero de ajedrez. 
        """
        for i in range(8):
            print(''.join(self.__board[(7-i)*8:(8-i)*8])) #Imprime el tablero desde la perspectiva de blancas.
    
    
    def index_to_chess_notation(self, index):
        """
        Convierte el índice de la lista, a la casilla de ajedrez correspondiente.
        """
        row=index//8 #Numero de fila
        col=index%8 #Numero de columna
        
        letter= chr(col+ord("a")) #Convertimos la columna a la letra correspondiente 
        return(letter+str(row+1))

    def chess_notation_for_move(self, movement):
        """
        Guarda el movimiento en notación de ajedrez.
        """
        move=movement[0]
        check=movement[1]
        checkmate=movement[2]
        
        #Guardamos las casillas en notación de ajedrez
        start_square=self.index_to_chess_notation(move[0])
        final_square=self.index_to_chess_notation(move[1])
        
        #guardamos la pieza con la que se jugó y la pieza capturada (podría ser ninguna)
        piece=self.__board[move[0]]
        captured_piece=self.__board[move[1]]
        
        #Si es jaque agregamos "+" al final de la notación.
        if(check==True):
        
            #Caso en el que no se captura nada: 
            if(captured_piece=="."):
                        
                #Si la jugada es movimiento de peon 
                if(piece.upper()=="P"):
                        notation=final_square+"+"
            
                #Si la jugada es movimiento de alfil
                elif(piece.upper()=="B"):
                        notation="B"+final_square+"+"
        
                #Si la jugada es movimiento del rey
                elif(piece.upper()=="K"):
                        notation="K"+final_square+"+"
                
                #Si la jugada es movimiento de dama
                #Es bueno indicar cuál dama es porque el jugador podría tener varias.
                elif(piece.upper()=="Q"):
                        notation="Q"+start_square+final_square+"+"
            
                #Si la jugada es movimiento de caballo
                #En este caso hay que indicar cuál caballo se mueve
                elif(piece.upper()=="N"):
                        notation="N"+start_square+final_square+"+"
            
                #Si la jugada es movimiento de torre
                #En este caso hay que indicar cuál torre se mueve
                elif(piece.upper()=="R"):
                        notation="R"+start_square+final_square+"+"
        
            #Caso en el que se captura algo
            #Todo igual que el anterior solo que agregamos una "x"
            else:
                #Si la jugada es movimiento de peon
                if(piece.upper()=="P"):
                    col=start_square.split()[0]
                    notation=col+"x"+final_square+"+"
            
                #Si la jugada es movimiento de alfil
                elif(piece.upper()=="B"):
                    notation="B"+"x"+final_square+"+"
        
                #Si la jugada es movimiento del rey
                elif(piece.upper()=="K"):
                    notation="K"+"x"+final_square+"+"
                
                #Si la jugada es movimiento de dama
                #Es bueno indicar cuál dama es porque el jugador podría tener varias.
                elif(piece.upper()=="Q"):
                    notation="Q"+start_square+"x"+final_square+"+"
            
                #Si la jugada es movimiento de caballo
                #En este caso hay que indicar cuál caballo se mueve
                elif(piece.upper()=="N"):
                    notation="N"+start_square+"x"+final_square+"+"
            
                #Si la jugada es movimiento de torre
                #En este caso hay que indicar cuál torre se mueve
                elif(piece.upper()=="R"):
                    notation="R"+start_square+"x"+final_square+"+"
                    
        #Si no fue jaque
        else:
            
            #Caso en el que no se captura nada: 
            if(captured_piece=="."):
                        
                #Si la jugada es movimiento de peon 
                if(piece.upper()=="P"):
                        notation=final_square
            
                #Si la jugada es movimiento de alfil
                elif(piece.upper()=="B"):
                        notation="B"+final_square
        
                #Si la jugada es movimiento del rey
                elif(piece.upper()=="K"):
                        notation="K"+final_square
                
                #Si la jugada es movimiento de dama
                #Es bueno indicar cuál dama es porque el jugador podría tener varias.
                elif(piece.upper()=="Q"):
                        notation="Q"+start_square+final_square
            
                #Si la jugada es movimiento de caballo
                #En este caso hay que indicar cuál caballo se mueve
                elif(piece.upper()=="N"):
                        notation="N"+start_square+final_square
            
                #Si la jugada es movimiento de torre
                #En este caso hay que indicar cuál torre se mueve
                elif(piece.upper()=="R"):
                        notation="R"+start_square+final_square
        
            #Caso en el que se captura algo
            #Todo igual que el anterior solo que agregamos una "x"
            else:
                #Si la jugada es movimiento de peon
                if(piece.upper()=="P"):
                    col=start_square.split()[0]
                    notation=col+"x"+final_square
            
                #Si la jugada es movimiento de alfil
                elif(piece.upper()=="B"):
                    notation="B"+"x"+final_square
        
                #Si la jugada es movimiento del rey
                elif(piece.upper()=="K"):
                    notation="K"+"x"+final_square
                
                #Si la jugada es movimiento de dama
                #Es bueno indicar cuál dama es porque el jugador podría tener varias.
                elif(piece.upper()=="Q"):
                    notation="Q"+start_square+"x"+final_square
            
                #Si la jugada es movimiento de caballo
                #En este caso hay que indicar cuál caballo se mueve
                elif(piece.upper()=="N"):
                    notation="N"+start_square+"x"+final_square
            
                #Si la jugada es movimiento de torre
                #En este caso hay que indicar cuál torre se mueve
                elif(piece.upper()=="R"):
                    notation="R"+start_square+"x"+final_square
                   
        return(notation)
    
    
    
    def legal_moves(self):
        
        moves=self.generate_legal_moves()
        moves_with_notation=[]
        for i in range(len(moves)):
            moves_with_notation.append(self.chess_notation_for_move(moves[i]))
        return(moves_with_notation)
    
    def isopponent(self, piece, piece_opponent):
        """
        Dada una pieza cualquiera del jugador y una supuesta pieza del oponente
        
        Parámetros: 
            piece: str
                Pieza cualquiera de nosotros
            piece_opponent: str
                Supuesta pieza del rival
        Returns: boolean
            Devuelve TRUE si la pieza oponente es  efectivamente del rival. FALSE si no.
        """
        if piece_opponent==".":
            return None
        
        elif piece.isupper() and piece_opponent.isupper():
            return False
        
        elif piece.islower() and piece_opponent.islower(): 
            return False
        
        else:
            return True 
    
    def find_king(self, color):
        king= "K" if color=="white" else "k"
        for i, piece in enumerate(self.__board):
            if piece==king:
                return i
        return -1 #Esto no debe pasar
    
    def can_we_eat_king(self):
        """
        
        Si podemos capturar al rey es porque el rival estaba en jaque. 
        Hizo una jugada ilegal.

        Returns
        -------
        bool
            DESCRIPTION.

        """
        
        #Buscamos rey del rival 
        rival_color= "white" if self.__turn=="black" else "black"
        king_position=self.find_king(rival_color)
        
        #Vemos todos las jugadas posibles nuestras
        moves=self.generate_moves()
        #Si podemos capturar el rey, el rival hizo jugada ilegal. 
        for move in moves:
            if move[1]==king_position:
                return True

        return False
        
    def is_it_check(self, move):
        """
        Determina si la jugada que hicimos fue jaque.
        """
        #Simulamos la jugada
        self.make_fake_move(move)
        
        #Nos pasamos el movimiento de nuevo a nosotros para determinar si podríamos capturar el rey.
        self.__turn="black" if self.__turn=="white" else "white"
        
        is_check=self.can_we_eat_king()
        
        #Devolvemos el turno
        self.__turn="black" if self.__turn=="white" else "white"
        
        
        #Devolvemos la jugada
        self.undo_fake_move(move)
       
        
        return(is_check)
    
    def is_it_checkmate(self, move, is_check):
        """
        Determina si, dado nuestro movimiento, el rival quedó en jaquemate
        """
        #Si el movimiento no es jaque no puede ser jaque mate
        if not is_check:
            return False
        
        #Si el movimiento es jaque 
        if is_check:
            
            #Hacemos el movimiento:
            self.make_fake_move(move)
            #Si el rival aún tiene jugadas disponibles entonces no es jaque mate
            if len(self.generate_legal_moves())>0:
                
                #Devolvemos el movimiento
                self.undo_fake_move(move)
                return False
        
            #Si es jaque y el rival ya no tiene jugadas disponibles
            else:
                
                #Devolvemos el movimiento
                self.undo_fake_move(move)
                return True 
                  
    def generate_piece_moves(self, piece, piece_position):
        moves=[]
        
        #Si es un peón
        if piece.upper()=="P":
            self.generate_pawn_moves(piece_position, piece, moves)
        
        #Si es una torre
        elif piece.upper()=="R":
            self.generate_rock_moves(piece_position, piece, moves)
        
        #Si es un alfil
        elif piece.upper()=="B":
            self.generate_bishop_moves(piece_position, piece, moves)
        
        elif piece.upper()=="N":
            self.generate_knight_moves(piece_position, piece, moves)
            
        #Si es una dama
        elif piece.upper()=="Q":
            self.generate_queen_moves(piece_position, piece, moves)
        
        #Si es el rey
        elif piece.upper()=="K":
            self.generate_king_moves(piece_position, piece, moves)

        return(moves)
    
    def generate_legal_moves(self):
        legal_moves=[]
        
        moves=self.generate_moves()
        
        for move in moves:
            #simulamos el movimiento:
            check=self.is_it_check(move)
            self.make_fake_move(move)
            
            #verificamos si hizo jugada legal 
            #si es el caso, la agregamos, como una lista donde
            #primer elemento: tupla del movimiento
            #segundo elemento: boolean de si es jaque
            #tercer elemento: boolean de si es jaque mate
            
            if not self.can_we_eat_king():
                #además, agregamos información sobre si la jugada es jaque o jaque mate
                legal_moves.append([move, check, self.is_it_checkmate(move, check)])
            
            #Devolvemos la jugada
            self.undo_fake_move(move)
            
        return(legal_moves)
        
    
    def generate_moves(self):
        moves=[] #Lista para guardar movimientos (no necesariamente legales) de la posición. 
        #Estos movimientos se guardan como una tupla:
        #El primer elemento de la tupla es la posición inicial de la pieza, el segundo es la posición final.
        
        for i, piece in enumerate(self.__board): #Iteramos sobre el tablero
            if piece== ".": #Si en la casilla no hay pieza seguimos
                continue
            
            #Verificamos si la pieza corresponde al color del jugador que le toca jugar
            if(self.__turn=="white" and  piece.isupper()) or(self.__turn=="black" and piece.islower()):
                
                #Añadimos todas las jugadas posibles de esa pieza
                moves.extend(self.generate_piece_moves(piece,i))
        
        return moves
                    
    
  
    def generate_pawn_moves(self, pawn_position, piece, moves):
        
        direction= 1 if piece.isupper() else -1 
        
        start_row= pawn_position//8
        start_col= pawn_position%8
        
        #Si el peón está en su casilla inicial, puede moverse dos veces hacia adelante
        if ((start_row==1 and piece.isupper()) or (start_row==5 and piece.islower())) and self.__board[pawn_position+ direction*16]=="." and self.__board[pawn_position+ direction*8]==".":
            moves.append((pawn_position, pawn_position+direction*16))
            
        #Evaluamos si se puede mover el peón hacia adelante
        if self.__board[pawn_position+ direction*8]==".":
            moves.append((pawn_position, pawn_position+ direction*8)) 
        
        
        #Evaluamos si puede capturar hacia la izquierda
        if(start_col>0):
            diagonal_left=pawn_position + direction*8-1
            
            #ahora vemos si hay una pieza rival (distinta del rey) en esa casilla. 
            if 0<=diagonal_left<64 and self.__board[diagonal_left]!= "."  and self.isopponent(piece, self.__board[diagonal_left]):
                moves.append((pawn_position, diagonal_left))
        
        #Evaluamos si puede capturar hacia la derecha
        if(start_col<7):
            diagonal_right=pawn_position + direction*8+1
            
            #ahora vemos si hay una pieza rival (distinta del rey) en esa casilla. 
            if 0<=diagonal_right<64 and self.__board[diagonal_right]!= "."  and self.isopponent(piece, self.__board[diagonal_right]):
                moves.append((pawn_position, diagonal_right))
       
        
     
    def generate_rock_moves(self, rock_position, piece, moves):
        #La torre se puede mover en 4 direcciones:
        #derecha, izquierda, abajo y arriba

        directions=[1,-1,8,-8]
        
        for direction in directions: 
            current_position=rock_position
            while True:
                current_position+=direction #Nos movemos un pasito
                
                if current_position<0 or current_position>63:
                    break #ya no podemos movernos más, estamos fuera del tablero. 
                    
                #Si nos movemos hacia la derecha y llegamos a la primera columna del tablero, es porque nos salimos.
                if direction==1 and current_position % 8 == 0:
                    break
                
                #Si nos movemos hacia la izquierda y llegamos a la última columna del tablero, es porque nos salimos. 
                if direction==-1 and current_position % 8 == 7:
                    break
                    
                #Si nos movemos hacia arriba y llegamos a la primera fila, es porque nos salimos
                if direction==8 and (current_position//8)==0:
                    break
                
                #Si nos movemos hacia abajo y llegamos a la última fila, es porque nos salimos
                if direction==-8 and (current_position//8)==7:
                    break
                
                
                target_square=self.__board[current_position]
                #Si la casilla a la que nos movimos está vacía, agregamos el movimiento.
                if target_square=='.':
                    moves.append((rock_position, current_position))
                
                #Si la casilla a la que nos movimos tiene una pieza del rival, es una captura. 
                #Se captura y no se puede seguir moviendo más
                elif self.isopponent(piece, target_square):
                    moves.append((rock_position, current_position))
                    break
                
                #Ultimo caso: la casilla  a la que nos movimos tiene una pieza nuestra
                #Por tanto, no nos podemos mover ahí.
                else: 
                    break
                
    
    
    def generate_bishop_moves(self, bishop_position, piece, moves):
        #El alfil se puede mover  en cuatro direcciones:
        #diagonal: abajo derecha, aribba izquierda, abajo izquierda, arriba derecha
        directions=[9,-9,7,-7]
        
        for direction in directions:
            current_position=bishop_position
            
            while True:
                current_position+=direction
                
                if current_position<0 or current_position>63:
                    break #ya no podemos movernos más, estamos fuera del tablero. 
                
                #Si el alfil se mueve abajo derecha y llega a la primera fila o a la primera columna, estamos fuera del tablero
                if direction==9 and (current_position//8==0 or current_position % 8 == 0) :
                    break
                
                #Si el alfil se mueve arriba izquierda y llega a la última fila o a la ultima columna, estamos fuera del tablero
                if direction==-9 and (current_position//8==7 or current_position % 8 == 7) :
                    break
                
                #Si el alfil se mueve abajo izquierda y llega a la primera fila o a la ultima columna, estamos fuera del tablero
                if direction==7 and (current_position//8==0 or current_position % 8 == 7) :
                    break
                
                #Si el alfil se mueve arriba derecha y llega a la última fila o a la primera columna, estamos fuera del tablero
                if direction==-7 and (current_position//8==7 or current_position % 8 == 0) :
                    break
                
                target_square=self.__board[current_position]
                #Si la casilla a la que nos movimos está vacía, agregamos el movimiento.
                if target_square=='.':
                    moves.append((bishop_position, current_position))
                
                #Si la casilla a la que nos movimos tiene una pieza del rival, es una captura. 
                #Se captura y no se puede seguir moviendo más
                elif self.isopponent(piece, target_square):
                    moves.append((bishop_position, current_position))
                    break
                
                #Ultimo caso: la casilla  a la que nos movimos tiene una pieza nuestra
                #Por tanto, no nos podemos mover ahí.
                else: 
                    break
                
        
    def generate_knight_moves(self, knight_position, piece, moves):
        """
        HAY QUE COMENTAR ESTA FUNCION
        """
        #tuplas con todas las combinaciones para formar una L
        knight_moves = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]

        start_row = knight_position // 8
        start_col = knight_position % 8

        for move in knight_moves:
            target_row = start_row + move[0]
            target_col = start_col + move[1]

            if 0 <= target_row < 8 and 0 <= target_col < 8:
                target_square = target_row * 8 + target_col
                target_piece = self.__board[target_square]
                if target_piece == '.' or self.isopponent(piece, target_piece):
                    moves.append((knight_position, target_square))
   
        
    def generate_queen_moves(self, queen_position, piece, moves):
        #La dama es como una combinación de la torre  y el alfil, entonces es unificar ambos códigos. 
        directions=[1,-1,8,-8, 9, -9, 7, -7]
        
        for direction in directions: 
            current_position=queen_position
            while True:
                current_position+=direction #Nos movemos un pasito
                
                if current_position<0 or current_position>63:
                    break #ya no podemos movernos más, estamos fuera del tablero. 
                    
                #Si nos movemos hacia la derecha y llegamos a la primera columna del tablero, es porque nos salimos.
                if direction==1 and current_position % 8 == 0:
                    break
                
                #Si nos movemos hacia la izquierda y llegamos a la última columna del tablero, es porque nos salimos. 
                if direction==-1 and current_position % 8 == 7:
                    break
                    
                #Si nos movemos hacia arriba y llegamos a la primera fila, es porque nos salimos
                if direction==8 and (current_position//8)==0:
                    break
                
                #Si nos movemos hacia abajo y llegamos a la última fila, es porque nos salimos
                if direction==-8 and (current_position//8)==7:
                    break
                
                #Si nos movemos abajo derecha y llega a la primera fila o a la primera columna, estamos fuera del tablero
                if direction==9 and (current_position//8==0 or current_position % 8 == 0) :
                    break
                
                #Si nos movemos arriba izquierda y llega a la última fila o a la ultima columna, estamos fuera del tablero
                if direction==-9 and (current_position//8==7 or current_position % 8 == 7) :
                    break
                
                #Si nos movemos abajo izquierda y llega a la primera fila o a la ultima columna, estamos fuera del tablero
                if direction==7 and (current_position//8==0 or current_position % 8 == 7) :
                    break
                
                #Si nos movemos arriba derecha y llega a la última fila o a la primera columna, estamos fuera del tablero
                if direction==-7 and (current_position//8==7 or current_position % 8 == 0) :
                    break
                
                target_square=self.__board[current_position]
                #Si la casilla a la que nos movimos está vacía, agregamos el movimiento.
                if target_square=='.':
                    moves.append((queen_position, current_position))
                
                #Si la casilla a la que nos movimos tiene una pieza del rival, es una captura. 
                #Se captura y no se puede seguir moviendo más
                elif self.isopponent(piece, target_square):
                    moves.append((queen_position, current_position))
                    break
                
                #Ultimo caso: la casilla  a la que nos movimos tiene una pieza nuestra
                #Por tanto, no nos podemos mover ahí.
                else: 
                    break
                
    def generate_king_moves(self, king_position, piece, moves):
        
        #El rey se puede mover para todas sus casillas alrededor a un paso
        #Estas son, para los lados: derecha, izquierda, abajo, arriba, 
        #diagonal: abajo derecha, aribba izquierda, abajo izquierda, arriba derecha
        directions=[1,-1,8,-8,9,-9,7,-7]
        
        start_row=king_position // 8
        start_col=king_position % 8
        
        for direction in directions:
            current_position=king_position
            current_position+=direction
            
            # Verificar que la nueva posición esté dentro del tablero
            if current_position < 0 or current_position >= 64:
                continue
            
            #Verificamos que la casilla a donde nos vamos a mover no tenga piezas nuestras o esté vacía.
            if (self.__board[current_position]==".") or ((self.__turn=="white" and self.__board[current_position].islower()) or (self.__turn=="black" and self.__board[current_position].isupper())):
                #Si se mueve hacia la derecha, hay que verificar que no esté en la ultima columna
                if direction==1 and start_col!=7:
                    moves.append((king_position, current_position))
            
                #Si se mueve hacia la izquierda, hay que verificar que no esté en la primera columna
                if direction==-1 and start_col!=0:
                    moves.append((king_position, current_position))
                
                #Si se mueve hacia abajo, hay que verificar que no esté en la última fila. 
                if direction==8 and start_row!=7:
                    moves.append((king_position, current_position))
            
                #Si se mueve hacia arriba, hay que verificar que no esté en la primera fila. 
                if direction==-8 and start_row!=0:
                    moves.append((king_position, current_position))
            
                #Si se mueve diagonal: arriba derecha, hay que verificar que no esté en la primera fila ni en la útltima columna 
                if direction==-7 and start_row!=0 and start_col!=7:
                    moves.append((king_position, current_position))
            
                #Si se mueve diagonal: arriba izquierda, hay que verificar que no esté en la primera fila ni en la primera columna 
                if direction==-9 and start_row!=0 and start_col!=0:
                    moves.append((king_position, current_position))
            
                #Si se mueve diagonal: abajo izquierda, hay que verificar que no esté en la última fila ni en la primera columna 
                if direction==7 and start_row!=7 and start_col!=0:
                    moves.append((king_position, current_position))
            
                #Si se mueve diagonal: abajo derecha, hay que verificar que no esté en la última fila ni en la última columna 
                if direction==9 and start_row!=7 and start_col!=7:
                    moves.append((king_position, current_position))
             
            
            
                
    def make_move(self, move):
        #Separamos la tupla por start y end
        start, end = move
        
        
        #Primero, guardamos la información sobre lo que había en la casilla antes de moverse ahí
        captured_piece=self.__board[end]
        
        #Guardamos información sobre que pieza estamos moviendo:
        piece_moved=self.__board[start]
        
        #Actualizamos el tablero. ESTO HAY QUE CORREGIRLO POR JUGADAS ESPECIALESn(enroque coronación)
        self.__board[end] = self.__board[start]
        self.__board[start] = "."
        
        #Guardamos la jugada en el historial de jugadas
        self.__move_history.append((start, end, piece_moved, captured_piece))
        
        #Revisamos si pusimos en jaque al oponente
        check=self.is_it_check(move)
        self.__check=check
        
        #Revisamos si lo pusimos en jaque mate
        checkmate=self.is_it_checkmate(move, check)
        print(checkmate)
        
        #Si es jaque mate, acaba la partida y gana el que tiene el turno:
        if(checkmate):
            print(f'{self.__turno} wins')
            
        else:
            #Sino, sigue el juego y pasamos la jugada al siguiente jugador
            self.__turn = "black" if self.__turn == "white" else "white"
            
        
        
    def make_fake_move(self, move):
        """
        Igual que make_move, pero no pregunta si la jugada es jaque.
        """
        #Separamos la tupla por start y end
        start, end = move
        
        
        #Primero, guardamos la información sobre lo que había en la casilla antes de moverse ahí
        captured_piece=self.__board[end]
        
        #Guardamos información sobre que pieza estamos moviendo:
        piece_moved=self.__board[start]
        
        #Actualizamos el tablero. ESTO HAY QUE CORREGIRLO POR JUGADAS ESPECIALESn(enroque coronación)
        self.__board[end] = self.__board[start]
        self.__board[start] = "."
        
        #Guardamos la jugada en el historial de jugadas
        self.__move_history.append((start, end, piece_moved, captured_piece))
        
        #Pasamos el turno
        self.__turn = "black" if self.__turn == "white" else "white"
    
    def undo_fake_move(self, move):
        #Guardamos información del movimiento que deseamos eliminar y lo eliminamos.
        start, end, piece_moved, captured_piece = self.__move_history.pop()
        
        #Devolvemos el tablero como estaba antes
        self.__board[start] = piece_moved
        self.__board[end] = captured_piece
        
        #Devolvemos el turno.
        self.__turn = "black" if self.__turn == "white" else "white"
        
            
    def undo_move(self, move):
        
        #Guardamos información del movimiento que deseamos eliminar y lo eliminamos.
        start, end, piece_moved, captured_piece = self.__move_history.pop()
        
        #Devolvemos el tablero como estaba antes
        self.__board[start] = piece_moved
        self.__board[end] = captured_piece
        
        #Devolvemos el turno.
        self.__turn = "black" if self.__turn == "white" else "white"
        
        #Devolvemos el estado del rey (si era jaque o no, y si era jaque mate o no)
        
    
    
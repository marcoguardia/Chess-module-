#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Jun 12 11:05:36 2024

@author: marcoguardia
"""

class Chess:
    def __init__(self, board=None, turn='white', check=False, WQ_rock_moved=False, WK_rock_moved=False,
                 BQ_rock_moved=False, BK_rock_moved=False, W_king_moved=False, B_king_moved=False, 
                 move_history=[]):
        """
        Método constructor del objeto Chess. 

    Parámetros: 
        board: list, opcional
            Lista con la posición actual del tablero, donde el índice 0 es la casilla a1, el índice 1 es la casilla a2 y así
            sucesivamente. Se inicializa por defecto en la posición inicial de una partida de ajedrez.
        turn: str, opcional
            Jugador al que le toca jugar dada la posición. Se inicializa por defecto en 'white'.
        check: bool, opcional
            Indica si el rey está en jaque. Se inicializa por defecto en False.
        WQ_rock_moved: bool, opcional
            Indica si la torre blanca del lado de la reina se ha movido. Se inicializa por defecto en False.
        WK_rock_moved: bool, opcional
            Indica si la torre blanca del lado del rey se ha movido. Se inicializa por defecto en False.
        BQ_rock_moved: bool, opcional
            Indica si la torre negra del lado de la reina se ha movido. Se inicializa por defecto en False.
        BK_rock_moved: bool, opcional
            Indica si la torre negra del lado del rey se ha movido. Se inicializa por defecto en False.
        W_king_moved: bool, opcional
            Indica si el rey blanco se ha movido. Se inicializa por defecto en False.
        B_king_moved: bool, opcional
            Indica si el rey negro se ha movido. Se inicializa por defecto en False.
        move_history: list, opcional
            Historial de jugadas del juego. Se inicializa por defecto como una lista vacía.

    Atributos:
        __board: list
            Lista que representa el tablero de ajedrez.
        __turn: str
            Jugador al que le toca jugar.
        __move_history: list
            Historial de jugadas del juego.
        __check: bool
            Indica si el rey está en jaque.
        __WQ_rock_moved: bool
            Indica si la torre blanca del lado de la reina se ha movido.
        __WK_rock_moved: bool
            Indica si la torre blanca del lado del rey se ha movido.
        __BQ_rock_moved: bool
            Indica si la torre negra del lado de la reina se ha movido.
        __BK_rock_moved: bool
            Indica si la torre negra del lado del rey se ha movido.
        __WK_moved: bool
            Indica si el rey blanco se ha movido.
        __BK_moved: bool
            Indica si el rey negro se ha movido.
        __piece_values: dict
            Diccionario con los valores de las piezas del ajedrez.
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
        self.__WQ_rock_moved=WQ_rock_moved
        self.__WK_rock_moved=WK_rock_moved
        
        self.__BQ_rock_moved=BQ_rock_moved
        self.__BK_rock_moved=BK_rock_moved
        
        self.__WK_moved=W_king_moved
        self.__BK_moved=B_king_moved
        
        self.__piece_values = {
            "p": -1, "n": -3, "b": -3, "r": -5, "q": -9, "k": 0,
            "P": 1, "N": 3, "B": 3, "R": 5, "Q": 9, "K": 0
        }
    
        
    @property
    def board(self):
        """Retorna la posición actual del tablero."""
        return self.__board

    @board.setter
    def board(self, board):
        """Establece una nueva posición en el tablero."""
        self.__board = board

    @property
    def turn(self):
        """Retorna el jugador al que le toca jugar."""
        return self.__turn

    @turn.setter
    def turn(self, turn):
        """Establece el jugador al que le toca jugar."""
        self.__turn = turn

    @property
    def check(self):
        """Retorna si el rey del jugador actual está en jaque."""
        return self.__check

    @check.setter
    def check(self, check):
        """Establece si el rey del jugador actual está en jaque."""
        self.__check = check

    @property
    def move_history(self):
        """Retorna el historial de jugadas del juego."""
        return self.__move_history

    @move_history.setter
    def move_history(self, move_history):
        """Establece el historial de jugadas del juego."""
        self.__move_history = move_history

    @property
    def WQ_rock_moved(self):
        """Retorna si la torre de la reina blanca se ha movido."""
        return self.__WQ_rock_moved

    @WQ_rock_moved.setter
    def WQ_rock_moved(self, WQ_rock_moved):
        """Establece si la torre de la reina blanca se ha movido."""
        self.__WQ_rock_moved = WQ_rock_moved

    @property
    def WK_rock_moved(self):
        """Retorna si la torre del rey blanca se ha movido."""
        return self.__WK_rock_moved

    @WK_rock_moved.setter
    def WK_rock_moved(self, WK_rock_moved):
        """Establece si la torre del rey blanca se ha movido."""
        self.__WK_rock_moved = WK_rock_moved

    @property
    def BQ_rock_moved(self):
        """Retorna si la torre de la reina negra se ha movido."""
        return self.__BQ_rock_moved

    @BQ_rock_moved.setter
    def BQ_rock_moved(self, BQ_rock_moved):
        """Establece si la torre de la reina negra se ha movido."""
        self.__BQ_rock_moved = BQ_rock_moved

    @property
    def BK_rock_moved(self):
        """Retorna si la torre del rey negra se ha movido."""
        return self.__BK_rock_moved

    @BK_rock_moved.setter
    def BK_rock_moved(self, BK_rock_moved):
        """Establece si la torre del rey negra se ha movido."""
        self.__BK_rock_moved = BK_rock_moved

    @property
    def W_king_moved(self):
        """Retorna si el rey blanco se ha movido."""
        return self.__W_king_moved

    @W_king_moved.setter
    def W_king_moved(self, W_king_moved):
        """Establece si el rey blanco se ha movido."""
        self.__W_king_moved = W_king_moved

    @property
    def B_king_moved(self):
        """Retorna si el rey negro se ha movido."""
        return self.__B_king_moved

    @B_king_moved.setter
    def B_king_moved(self, B_king_moved):
        """Establece si el rey negro se ha movido."""
        self.__B_king_moved = B_king_moved
        
    
    def __str__(self):
        """
        Retorna una representación en cadena de todos los atributos de la instancia de Chess.
    
        Retorno:
        str: Representación de los atributos de la instancia.
        """
        attributes_str = f"Turno actual: {self.__turn}\n"
        attributes_str += f"En jaque: {self.__check}\n"
        attributes_str += f"Torre de la reina blanca movida: {self.__WQ_rock_moved}\n"
        attributes_str += f"Torre del rey blanco movida: {self.__WK_rock_moved}\n"
        attributes_str += f"Torre de la reina negra movida: {self.__BQ_rock_moved}\n"
        attributes_str += f"Torre del rey negro movida: {self.__BK_rock_moved}\n"
        attributes_str += f"Rey blanco movido: {self.__W_king_moved}\n"
        attributes_str += f"Rey negro movido: {self.__B_king_moved}\n"
    
        #Llamar a la función print_board para obtener la representación del tablero
        attributes_str += "\nTablero de ajedrez:\n"
        attributes_str += self.print_board()
    
        return attributes_str
    

    def print_board(self):
        """
        Imprime el tablero de ajedrez. 
        """
        for i in range(8):
            print(''.join(self.__board[(7-i)*8:(8-i)*8])) #Imprime el tablero desde la perspectiva de blancas.
    
    
    
    def index_to_chess_notation(self, index):
        """
        Convierte el índice de la lista, a la casilla de ajedrez correspondiente. Por ejemplo, 0 sería a1. 
        
        Parámetros: 
            index: int
                índice de la lista board
        """
        row=index//8 #Numero de fila
        col=index%8 #Numero de columna
        
        letter= chr(col+ord("a")) #Convertimos la columna a la letra correspondiente 
        return(letter+str(row+1))
    

    def chess_notation_for_move(self, movement):
        """
        Guarda el movimiento en notación de ajedrez.
        
        Parámetros: 
            movement: tupla
                Movimiento de pieza
        Retorno: 
            str: Movimiento en notación ajedrecística
        """
        #Primero que todo, si el movimiento es enroque, devolvemos 0-0 o 0-0-0 dado que esa es la notación
        if(movement[0]==(0,0,0)):
            return("0-0-0")
        
        if(movement[0]==(0,0)):
            return("0-0")
        
        move=movement[0]
        check=movement[1]
        checkmate=movement[2]
        
        #Guardamos las casillas en notación de ajedrez
        start_square=self.index_to_chess_notation(move[0])
        final_square=self.index_to_chess_notation(move[1])
        
        #guardamos la pieza con la que se jugó y la pieza capturada (podría ser ninguna)
        piece=self.__board[move[0]]
        captured_piece=self.__board[move[1]]
        
        #Si es jaque mate, agregamos # al final
        if(checkmate==True):
            
            #Caso en el que no se captura nada: 
            if(captured_piece=="."):
                        
                #Si la jugada es movimiento de peon 
                if(piece.upper()=="P"):
                        notation=final_square+"#"
            
                #Si la jugada es movimiento de alfil
                elif(piece.upper()=="B"):
                        notation="B"+final_square+"#"
        
                #Si la jugada es movimiento del rey
                elif(piece.upper()=="K"):
                        notation="K"+final_square+"#"
                
                #Si la jugada es movimiento de dama
                #Es bueno indicar cuál dama es porque el jugador podría tener varias.
                elif(piece.upper()=="Q"):
                        notation="Q"+start_square+final_square+"#"
            
                #Si la jugada es movimiento de caballo
                #En este caso hay que indicar cuál caballo se mueve
                elif(piece.upper()=="N"):
                        notation="N"+start_square+final_square+"#"
            
                #Si la jugada es movimiento de torre
                #En este caso hay que indicar cuál torre se mueve
                elif(piece.upper()=="R"):
                        notation="R"+start_square+final_square+"#"
        
            #Caso en el que se captura algo
            #Todo igual que el anterior solo que agregamos una "x"
            else:
                #Si la jugada es movimiento de peon
                if(piece.upper()=="P"):
                    col=start_square.split()[0]
                    notation=col+"x"+final_square+"#"
            
                #Si la jugada es movimiento de alfil
                elif(piece.upper()=="B"):
                    notation="B"+"x"+final_square+"#"
        
                #Si la jugada es movimiento del rey
                elif(piece.upper()=="K"):
                    notation="K"+"x"+final_square+"#"
                
                #Si la jugada es movimiento de dama
                #Es bueno indicar cuál dama es porque el jugador podría tener varias.
                elif(piece.upper()=="Q"):
                    notation="Q"+start_square+"x"+final_square+"#"
            
                #Si la jugada es movimiento de caballo
                #En este caso hay que indicar cuál caballo se mueve
                elif(piece.upper()=="N"):
                    notation="N"+start_square+"x"+final_square+"#"
            
                #Si la jugada es movimiento de torre
                #En este caso hay que indicar cuál torre se mueve
                elif(piece.upper()=="R"):
                    notation="R"+start_square+"x"+final_square+"#"
            return(notation)
        
        #Si es jaque agregamos "+" al final de la notación.
        elif(check==True):
        
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
                    
       
        
        #No es jaque ni jaque mate          
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
    

    def isopponent(self, piece, piece_opponent):
        """
        Dada una pieza cualquiera del jugador y una supuesta pieza del oponente, 
        revisa si en efecto la pieza es del oponente o no. 
        
        Parámetros: 
            piece: str
                Pieza cualquiera de nosotros
            piece_opponent: str
                Supuesta pieza del rival
        Retorno: 
            boolean: Devuelve TRUE si la pieza oponente es  efectivamente del rival. FALSE si no.
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
        """
        Función que busca al rey del color ingresado. 
        
        Parámetros:
            color= Color del rey que se está buscando
        
        Retorno:
            int: Devuelve donde se encuentra el rey en la lista board.
        """
        king= "K" if color=="white" else "k"
        for i, piece in enumerate(self.__board):
            if piece==king:
                return i
        return -1 #Esto no debe pasar
    
    def can_we_eat_king(self):
        """
        Función que se utiliza para verificar si una jugada es legal.
        Si podemos capturar al rey es porque el rival estaba en jaque. 
        Hizo una jugada ilegal.

        Retorno:
            bool: True si el jugador actual podría comerse el rey rival, False si no.
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
        
        Parámetros:
            move: tupla
                tupla con el movimiento que se desea ver si fue jaque. 
        
        Retorno:
            bool: True si el movimiento es jaque, False si no. 
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
        Determina si la jugada que hicimos fue jaquemate.
        
        Parámetros:
            move: tupla
                tupla con el movimiento que se desea ver si fue jaquemate. 
            is_check: bool
                True si el movimiento es jaque, False si no. 
        
        Retorno:
            bool: True si el movimiento es jaquemate, False si no. 
        """
        
        #Si el movimiento no es jaque no puede ser jaque mate
        if not is_check:
            return False
        
        #Si el movimiento es jaque 
        if is_check:
            
            #Hacemos el movimiento:
            self.make_fake_move(move)
            #Si el rival aún tiene jugadas disponibles entonces no es jaque mate
            if len(self.generate_legal_moves()[0])>0:
                
                #Devolvemos el movimiento
                self.undo_fake_move(move)
                return False
        
            #Si es jaque y el rival ya no tiene jugadas disponibles
            else:
                
                #Devolvemos el movimiento
                self.undo_fake_move(move)
                return True 
                  
    
    def can_i_castle_king_side(self):
        """
        Determina si el jugador actual puede enrocar en el ala de rey (enroque corto)
        
        Retorno:
            bool: True si puede hacer enroque corto, False si no
        """
        
        #Vemos a quién le toca jugar
        turn="black" if self.__turn=="black" else "white"
        
        #Si le toca a las blancas:
        if(turn=="white"):
       
            #Vemos si no ha movido la torre del king side y si no ha movido el rey y si no está en jaque, sino devuelve False
            if(self.__check==True or self.__WK_moved==True or self.__WK_rock_moved):
                return False
            
            #Sino sí tiene derecho a enrocar
            else:
                #Si sí está vacía, verificamos que el oponente no pueda comerse el rey
                if(self.__board[5]!="."):
                    return False
                #La casilla está vacía, hacemos el movimiento fake y evaluamos si no nos pueden comer el rey
                self.make_fake_move((4,5))
                if(self.can_we_eat_king()):
                    self.undo_fake_move((4,5))
                    return False

                #Si pasa por esa verificación deshacemos el movimiento y verificamos si la segunda casilla está vacía
                self.undo_fake_move((4,5))
                if(self.__board[6]!="."):
                    return False
                
                #Si sí está vacía, verificamos que el oponente no pueda comerse el rey
                self.make_fake_move((4,6))
                if(self.can_we_eat_king()):
                    self.undo_fake_move((4,6))
                    return False
                #Si pasa por todas esas verificaciones, devolvemos true
                self.undo_fake_move((4,6))
                return(True)
            
        #Si le toca jugar a las negras  (todo igual pero el caso para las negras)
        else:
            #Vemos si no ha movido la torre del king side y si no ha movido el rey y si no está en jaque, sino devuelve False
            if(self.__check==True or self.__BK_moved==True or self.__BK_rock_moved):
                return False
            
            #Sino sí tiene derecho a enrocar
            else:
                #Si sí está vacía, verificamos que el oponente no pueda comerse el rey
                if(self.__board[59]!="."):
                    return False
                #La casilla está vacía, hacemos el movimiento fake y evaluamos si no nos pueden comer el rey
                self.make_fake_move((60,61))
                if(self.can_we_eat_king()):
                    self.undo_fake_move((60,61))
                    return False

                #Si pasa por esa verificación deshacemos el movimiento y verificamos si la segunda casilla está vacía
                self.undo_fake_move((60,61))
                if(self.__board[62]!="."):
                    return False
                #Si sí está vacía, verificamos que el oponente no pueda comerse el rey
                self.make_fake_move((60,62))
                if(self.can_we_eat_king()):
                    self.undo_fake_move((60,62))
                    return False
                
                #Si pasa por todas esas verificaciones, devolvemos true
                self.undo_fake_move((60,62))
                return(True)
    
    
    def can_i_castle_queen_side(self):
        """
        Determina si el jugador actual puede enrocar en el ala de dama (enroque largo)
        
        Retorno:
            bool: True si puede hacer enroque largo, False si no
        """
        
        #Vemos a quién le toca jugar
        turn="black" if self.__turn=="black" else "white"
        
        #Si le toca a las blancas:
        if(turn=="white"):
       
            #Vemos si no ha movido la torre del queen side y si no ha movido el rey y si no está en jaque, sino devuelve False
            if(self.__check==True or self.__WK_moved==True or self.__WQ_rock_moved):
                return False
            
            #Sino sí tiene derecho a enrocar
            else:
               #Verificamos si casilla está vacía
                if(self.__board[3]!="."):
                    return False
                #La casilla está vacía, hacemos el movimiento fake y evaluamos si no nos pueden comer el rey
                self.make_fake_move((4,3))
                if(self.can_we_eat_king()):
                    self.undo_fake_move((4,3))
                    return False

                #Si pasa por esa verificación deshacemos el movimiento y verificamos si la segunda casilla está vacía
                self.undo_fake_move((4,3))
                if(self.__board[2]!="."):
                    return False
                
                #Si sí está vacía, verificamos que el oponente no pueda comerse el rey
                self.make_fake_move((4,2))
                if(self.can_we_eat_king()):
                    self.undo_fake_move((4,2))
                    return False
                
                #Si pasa por la verificación, deshacemos el movimiento y verificamos que la tercera casilla esté vacía
                self.undo_fake_move((4,2))
                if(self.__board[1]!="."):
                    return False
                self.make_fake_move((4,1))
                if(self.can_we_eat_king()):
                    self.undo_fake_move((4,1))
                    return False
                
                self.undo_fake_move((4,1))
                #Si pasa por todas esas verificaciones, devolvemos true y el movimiento
                return True
            
        #Si le toca jugar a las negras  (todo igual pero el caso para las negras)
        else:
            #Vemos si no ha movido la torre del king side y si no ha movido el rey y si no está en jaque, sino devuelve False
            if(self.__check==True or self.__BK_moved==True or self.__BK_rock_moved):
                return False
            
            #Sino sí tiene derecho a enrocar
            else:
                #Si sí está vacía, verificamos que el oponente no pueda comerse el rey
                if(self.__board[59]!="."):
                    return False
                #La casilla está vacía, hacemos el movimiento fake y evaluamos si no nos pueden comer el rey
                self.make_fake_move((60,61))
                if(self.can_we_eat_king()):
                    self.undo_fake_move((60,61))
                    return False

                #Si pasa por esa verificación deshacemos el movimiento y verificamos si la segunda casilla está vacía
                self.undo_fake_move((60,61))
                if(self.__board[62]!="."):
                    return False
                #Si sí está vacía, verificamos que el oponente no pueda comerse el rey
                self.make_fake_move((60,62))
                if(self.can_we_eat_king()):
                    self.undo_fake_move((60,62))
                    return False
                
                #Si pasa por todas esas verificaciones, devolvemos true
                self.undo_fake_move((60,62))
                return True
            
        
    def generate_piece_moves(self, piece, piece_position):
        """
        Genera todos los movimientos posibles (no necesariamente legales) 
        para una pieza dada de la posición actual. 

        Parameters
            piece : chr
                pieza (en su formato según el tablero de la clase Chess), a la que
                se le desea generar los movimientos posibles (no necesariamente legales)
            piece_position : int
                posición actual de la pieza en el tablero (índice de la lista)
            DESCRIPTION.

        Retorno:
            list: lista con las tuplas de los movimientos posibles de esa pieza
            (pero no necesariamente legales)
        """
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
    
    
    def generate_moves(self):
        """
        Genera todos los movimientos posibles para el jugador actual. Movimientos que
        no necesariamente deben ser legales. 

        Retorno:
            list: movimientos posibles de la posición (no necesariamente legales)

        """
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
        
        #Ademas, buscamos si se puede enrocar:
        
        
        return moves
    
    
    def generate_legal_moves(self):
        """
        Genera todos los movimientos legales de la posición para el jugador que 
        le toca jugar. 

        Retorno:
            list: lista con todos los movimientos legales

        """
        legal_moves=[]
        just_legal_moves=[]
        
        moves=self.generate_moves()
        
        for move in moves:
            
            #simulamos el movimiento
                
            check=self.is_it_check(move)
            self.make_fake_move(move)
            
            #verificamos si hizo jugada legal 
            #si es el caso, la agregamos, como una lista donde:
            #primer elemento: tupla del movimiento
            #segundo elemento: boolean de si es jaque
            #tercer elemento: boolean de si es jaque mate
            
            if not self.can_we_eat_king():
                #además, agregamos información sobre si la jugada es jaque o jaque mate
                legal_moves.append([move, check, self.is_it_checkmate(move, check)])
                just_legal_moves.append(move)
            
            #Devolvemos la jugada
            self.undo_fake_move(move)
            
        return just_legal_moves,legal_moves
    
    
    def legal_moves(self):
        """
        Devuelve las jugadas legales de la posición actual para el jugador que le toca, 
        en notación ajedrecística.

        Retorno:
            list: jugadas legales en notación de ajedrez.
        """
        
        moves=self.generate_legal_moves()[1]
        moves_with_notation=[]
        for i in range(len(moves)):
            moves_with_notation.append(self.chess_notation_for_move(moves[i]))
        return(moves_with_notation)
        
  
    def generate_pawn_moves(self, pawn_position, piece, moves):
        """
        Genera todos los movimientos posibles (no necesariamente legales)
        de un peón en específico de la posición. Además, agrega estos movimientos
        a la lista de todos los movimientos posibles de las otras piezas
        
        Parámetros:
            pawn_position: int
                posición actual del peón
            piece: chr
                pieza (en este caso peón) en su formato de la clase Chess. 
            moves: lista con todos los movimientos posibles de la posición 
            (no necesariamente legales) encontrados hasta ahora.
        """
        
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
        """
        Genera todos los movimientos posibles (no necesariamente legales)
        de una torre en específico de la posición. Además, agrega estos movimientos
        a la lista de todos los movimientos posibles de las otras piezas
        
        Parámetros:
            rock_position: int
                posición actual de la torre
            piece: chr
                pieza (en este caso torre) en su formato de la clase Chess. 
            moves: lista con todos los movimientos posibles de la posición 
            (no necesariamente legales) encontrados hasta ahora.
        """
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
        """
        Genera todos los movimientos posibles (no necesariamente legales)
        de un alfil en específico de la posición. Además, agrega estos movimientos
        a la lista de todos los movimientos posibles de las otras piezas
        
        Parámetros:
            bishop_position: int
                posición actual del alfil
            piece: chr
                pieza (en este caso alfil) en su formato de la clase Chess. 
            moves: lista con todos los movimientos posibles de la posición 
            (no necesariamente legales) encontrados hasta ahora.
        """
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
        Genera todos los movimientos posibles (no necesariamente legales)
        de un caballo en específico de la posición. Además, agrega estos movimientos
        a la lista de todos los movimientos posibles de las otras piezas
        
        Parámetros:
            knight_position: int
                posición actual del caballo
            piece: chr
                pieza (en este caso caballo) en su formato de la clase Chess. 
            moves: lista con todos los movimientos posibles de la posición 
            (no necesariamente legales) encontrados hasta ahora.
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
        """
        Genera todos los movimientos posibles (no necesariamente legales)
        de una dama en específico de la posición. Además, agrega estos movimientos
        a la lista de todos los movimientos posibles de las otras piezas
        
        Parámetros:
            queen_position: int
                posición actual de la dama
            piece: chr
                pieza (en este caso dama) en su formato de la clase Chess. 
            moves: lista con todos los movimientos posibles de la posición 
            (no necesariamente legales) encontrados hasta ahora.
        """
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
        """
        Genera todos los movimientos posibles (no necesariamente legales)
        de un rey en específico de la posición. Además, agrega estos movimientos
        a la lista de todos los movimientos posibles de las otras piezas
        
        Parámetros:
            king_position: int
                posición actual del rey
            piece: chr
                pieza (en este caso rey) en su formato de la clase Chess. 
            moves: lista con todos los movimientos posibles de la posición 
            (no necesariamente legales) encontrados hasta ahora.
        """
        
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
                    
        #Ahora veamos si se puede enrocar 
        if(self.can_i_castle_king_side()):
                moves.append((0,0)) #0,0 representa enroque largo
        if(self.can_i_castle_queen_side()):
                moves.append((0,0,0)) #0,0 representa enroque corto
                  
                
    def make_move(self, move):
        """
        Realiza un movimiento en la posición. Además, según las características
        del movimiento, actualiza atributos del objeto, como si el movimiento 
        es jaque o si una de las torres se movió. 

        Parámetros:
            move: tupla
                Movimiento que se realizó.
        """
        #Separamos la tupla por start y end
        start, end = move
        
        #Primero: caso en que se está haciendo un enroque largo
        if(move==(0,0,0)):
            if(self.__turn=="white"):
                self.__board[4]="." #El rey desocupa esa casilla
                self.__board[0]="." #La torre desocupa esa casilla
                self.__board[2]="K" #El rey se ubica ahora ahí
                self.__board[3]="R" #La torre se ubica ahora ahí
            else:
                self.__board[60]="." #El rey desocupa esa casilla
                self.__board[56]="." #La torre desocupa esa casilla
                self.__board[58]="k" #El rey se ubica ahora ahí
                self.__board[59]="r" #La torre se ubica ahora ahí
               
        if(move==(0,0)):
            if(self.__turn=="white"):
                self.__board[4]="." #El rey desocupa esa casilla
                self.__board[7]="." #La torre desocupa esa casilla
                self.__board[6]="K" #El rey se ubica ahora ahí
                self.__board[5]="R" #La torre se ubica ahora ahí
            else:
                self.__board[60]="." #El rey desocupa esa casilla
                self.__board[63]="." #La torre desocupa esa casilla
                self.__board[62]="k" #El rey se ubica ahora ahí
                self.__board[61]="r" #La torre se ubica ahora ahí
        
        #Si no es enroque, primero guardamos la información sobre lo que había en la casilla antes de moverse ahí
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
        
        #Si es jaque mate, acaba la partida y gana el que tiene el turno:
        if(checkmate):
            print(f'{self.__turno} wins')
            
        else:
            #Sino, sigue el juego y pasamos la jugada al siguiente jugador
            self.__turn = "black" if self.__turn == "white" else "white"
    
    def undo_move(self, move):
        """
        Método para deshacer un movimiento.

        Parámetros:
            move: tupla
                Movimiento que se desea eliminar.
            
        """
        
        #Guardamos información del movimiento que deseamos eliminar y lo eliminamos.
        start, end, piece_moved, captured_piece = self.__move_history.pop()
        
        #Devolvemos el tablero como estaba antes
        self.__board[start] = piece_moved
        self.__board[end] = captured_piece
        
        #Devolvemos el turno.
        self.__turn = "black" if self.__turn == "white" else "white"
        
        #Devolvemos el estado del rey (si era jaque o no, y si era jaque mate o no)            
        
        
    def make_fake_move(self, move):
        """
        Es igual que la función make_move, sin embargo esta evita verificaciones
        sobre si el movimiento es jaque o jaquemate, con el fin de ahorrar cálculos
        en ciertos momentos donde no se requiere.
        
        Parámetros:
            move: tupla con el movimiento 
        """
        
        #Primero: caso en que se está haciendo un enroque largo
        if(move==(0,0,0)):
            if(self.__turn=="white"):
                self.__board[4]="." #El rey desocupa esa casilla
                self.__board[0]="." #La torre desocupa esa casilla
                self.__board[2]="K" #El rey se ubica ahora ahí
                self.__board[3]="R" #La torre se ubica ahora ahí
            else:
                self.__board[60]="." #El rey desocupa esa casilla
                self.__board[56]="." #La torre desocupa esa casilla
                self.__board[58]="k" #El rey se ubica ahora ahí
                self.__board[59]="r" #La torre se ubica ahora ahí
            
            #Guardamos la jugada en el historial de jugadas
            self.__move_history.append((0,0,0))
               
        elif(move==(0,0)):
            if(self.__turn=="white"):
                self.__board[4]="." #El rey desocupa esa casilla
                self.__board[7]="." #La torre desocupa esa casilla
                self.__board[6]="K" #El rey se ubica ahora ahí
                self.__board[5]="R" #La torre se ubica ahora ahí
            else:
                self.__board[60]="." #El rey desocupa esa casilla
                self.__board[63]="." #La torre desocupa esa casilla
                self.__board[62]="k" #El rey se ubica ahora ahí
                self.__board[61]="r" #La torre se ubica ahora ahí
                
            #Guardamos la jugada en el historial de jugadas
            self.__move_history.append((0,0))
        
        #Si no era enroque
        else:
            #Separamos la tupla por start y end
            start, end = move
        
            #Si no es un enroque, primero guardamos la información sobre lo que había en la casilla antes de moverse ahí
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
        """
        Deshace el movimiento generado por el método make_fake_move

        Parámetros:
            move: tupla
                movimiento que se va deshacer
        """
        # Verificamos si el movimiento fue un enroque largo para blancas
        if move == (0, 0, 0) and self.__turn == "white":
            self.__board[2] = "."  # Devolvemos al rey a su posición original
            self.__board[3] = "."  # Devolvemos a la torre a su posición original
            self.__board[4] = "K"  # Restauramos el rey blanco
            self.__board[0] = "R"  # Restauramos la torre de la reina blanca
            self.__move_history.pop()
    
        #Verificamos si el movimiento fue un enroque largo para negras
        elif move == (0, 0, 0) and self.__turn == "black":
            self.__board[58] = "."  # Devolvemos al rey a su posición original
            self.__board[59] = "."  # Devolvemos a la torre a su posición original
            self.__board[60] = "k"  # Restauramos el rey negro
            self.__board[56] = "r"  # Restauramos la torre del rey negro
            self.__move_history.pop()

        # Verificamos si el movimiento fue un enroque corto para blancas
        elif move == (0, 0) and self.__turn == "white":
            self.__board[6] = "."  # Devolvemos al rey a su posición original
            self.__board[5] = "."  # Devolvemos a la torre a su posición original
            self.__board[4] = "K"  # Restauramos el rey blanco
            self.__board[7] = "R"  # Restauramos la torre del rey blanco
            self.__move_history.pop()
    
        #Verificamos si el movimiento fue un enroque corto para negras
        elif move == (0, 0) and self.__turn == "black":
            self.__board[62] = "."  # Devolvemos al rey a su posición original
            self.__board[61] = "."  # Devolvemos a la torre a su posición original
            self.__board[60] = "k"  # Restauramos el rey negro
            self.__board[63] = "r"  # Restauramos la torre del rey negro
            self.__move_history.pop()

        else:
            
            #Guardamos información del movimiento que deseamos eliminar y lo eliminamos.
            start, end, piece_moved, captured_piece = self.__move_history.pop()
        
            #Devolvemos el tablero como estaba antes
            self.__board[start] = piece_moved
            self.__board[end] = captured_piece
        
        #Devolvemos el turno y eliminamos el movimiento del historial
        self.__turn = "black" if self.__turn == "white" else "white"
        
    
    
    def control_squares(self):
        """
        Devuelve dos listas con las casillas que "ve" cada pieza. Una lista de 
        para las blancas y una lista para las negras. Con "ver", se refiere a donde
        la pieza tiene control/acceso.
      
        Retorno:
            list: lista con las jugadas donde con el acceso de las piezas blancas 
            list: lista con la jugadas de las piezas negras
        
        """
        white=[] 
        black=[]
        #Estos movimientos se guardan como una tupla:
        #El primer elemento de la tupla es la posición inicial de la pieza, el segundo es la posición final.
        
        for i, piece in enumerate(self.__board): #Iteramos sobre el tablero
            if piece== ".": #Si en la casilla no hay pieza seguimos
                continue
            
            #Añadimos las jugadas de las blancas
            if(piece.isupper()):
                white.extend(self.generate_piece_control(piece,i))
            
            #Añadimos las jugadas de las negras
            if(piece.islower()):
                black.extend(self.generate_piece_control(piece,i))
                
        return white, black


    def generate_piece_control(self, piece, piece_position):
        """
        Devuelve una lista con las casillas que controla cierta pieza en específico.

        Parámetros:
            piece: chr
                Pieza a la que se le desea encontrar las casillas que controla
            piece_position: int
                Índice de la lista del tablero donde se encuentra la pieza
        Retorno:
            list: lista con las casillas que controla la pieza
            
        """
        moves=[]
        
        #Si es un peón
        if piece.upper()=="P":
            self.control_pawn(piece_position, piece, moves)
        
        #Si es una torre
        elif piece.upper()=="R":
            self.control_rock(piece_position, piece, moves)
        
        #Si es un alfil
        elif piece.upper()=="B":
            self.control_bishop(piece_position, piece, moves)
        
        elif piece.upper()=="N":
            self.control_knight(piece_position, piece, moves)
            
        #Si es una dama
        elif piece.upper()=="Q":
            self.control_queen(piece_position, piece, moves)
        
        #Si es el rey
        elif piece.upper()=="K":
            self.control_king(piece_position, piece, moves)

        return(moves)


    def control_pawn(self, pawn_position, piece, moves):
        """
        Devuelve una lista con las casillas que controla cierto peón en específico.
        
        Parámetros:
            piece: chr
                Peón al que se le desea encontrar las casillas que controla
            piece_position: int
                Índice de la lista del tablero donde se encuentra el peón
        Retorno: 
            list: Lista con las casillas que controla el peón.
        """
        
        direction= 1 if piece.isupper() else -1 
        
        #start_row= pawn_position//8
        start_col= pawn_position%8
        
        #El peón controla las diagonales
        if(start_col>0):
            diagonal_left=pawn_position + direction*8-1
            
            if 0<=diagonal_left<64:
                moves.append((pawn_position, diagonal_left))
        
        #Evaluamos si hay columna izquierda
        if(start_col<7):
            diagonal_right=pawn_position + direction*8+1
            
            if 0<=diagonal_right<64:
                moves.append((pawn_position, diagonal_right))
       
        
     
    def control_rock(self, rock_position, piece, moves):
        """
        Devuelve una lista con las casillas que controla cierta torre en específico.
        
        Parámetros:
            piece: chr
                Torre al que se le desea encontrar las casillas que controla
            piece_position: int
                Índice de la lista del tablero donde se encuentra la torre
        Retorno: 
            list: Lista con las casillas que controla la torre.
        """
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
                
                #Si la casilla tiene pieza, igual controlamos pero hasta ahí llegamos
                else:
                    moves.append((rock_position, current_position))
                    break
                
                    
               
    def control_bishop(self, bishop_position, piece, moves):
        """
        Devuelve una lista con las casillas que controla cierto alfil en específico.
        
        Parámetros:
            piece: chr
                Alfil al que se le desea encontrar las casillas que controla
            piece_position: int
                Índice de la lista del tablero donde se encuentra el alfil
        Retorno: 
            list: Lista con las casillas que controla el alfil.
        """
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
                
                #Si la casilla tiene pieza, igual controlamos pero hasta ahí llegamos
                else:
                    moves.append((bishop_position, current_position))
                    break
            
        
    def control_knight(self, knight_position, piece, moves):
        """
        Devuelve una lista con las casillas que controla cierto caballo en específico.
        
        Parámetros:
            piece: chr
                Caballo al que se le desea encontrar las casillas que controla
            piece_position: int
                Índice de la lista del tablero donde se encuentra el caballo
        Retorno: 
            list: Lista con las casillas que controla el caballo.
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
                moves.append((knight_position, target_square))

        
    def control_queen(self, queen_position, piece, moves):
        """
        Devuelve una lista con las casillas que controla cierta dama en específico.
        
        Parámetros:
            piece: chr
                Dama al que se le desea encontrar las casillas que controla
            piece_position: int
                Índice de la lista del tablero donde se encuentra la dama
        Retorno: 
            list: Lista con las casillas que controla la dama.
        """
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
                
                #Si la casilla a la que nos movimos tiene una pieza igual controlamos pero hasta ahí llegamos
                #Se captura y no se puede seguir moviendo más
                else:
                    moves.append((queen_position, current_position))
                    break
                
                
                
    def control_king(self, king_position, piece, moves):
        """
        Devuelve una lista con las casillas que controla cierto rey en específico.
        
        Parámetros:
            piece: chr
                Rey al que se le desea encontrar las casillas que controla
            piece_position: int
                Índice de la lista del tablero donde se encuentra el rey
        Retorno: 
            list: Lista con las casillas que controla el rey.
        """
        
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
             
    
    def evaluate_board(self):
        """
        Evalúa de forma estática, es decir, sin ver posibles jugadas posteriores
        Esto lo hace mediante evaluaciones heurísticas como el control de ciertas casillas
        o la cantidad de material por jugador.
        
        Retorno:
            float: Evaluación de la posición actual
        """
        
        evaluation = 0
        for square in self.__board:
            if square != ".":
                piece=square
                evaluation += self.__piece_values[piece]
                
        #también vamos a ver quien controla las casillas centrales
        #Definimos casillas centrales como las casillas:
        central_squares=[27,28, 35, 36]
        
        square_battle=self.control_squares() 
        white=square_battle[0]
        #print(white)
        black=square_battle[1]
        
        for square in central_squares:
        
            #Contar cuántas piezas de las blancas controlan esa casilla
            control_white=sum(1 for t in white if t[1] == square)
            
            #Contar cuántas piezas de las negras controlan esa casilla
            control_black=sum(1 for t in black if t[1] == square)
            
            
            #Cuántas piezas netas tiene las blancas para controlar esa casilla
            white_has=control_white-control_black
            #print(white_has)
            evaluation+=white_has/2 #Le vamos a dar un puntaje de 0.5 por cada pieza extra que controla una casilla central
        
        
        #Ahora quién controla casillas alrededor de las centrales
        central_squares2=[18,19,20,21,26,34,42,43,44,45,29,37]
        
        for square in central_squares2:
            
            #Contar cuántas piezas de las blancas controlan esa casilla
            
            control_white=sum(1 for t in white if t[1] == square)
            
            #Contar cuántas piezas de las negras controlan esa casilla
            control_black=sum(1 for t in black if t[1] == square)
            
            #Cuántas piezas netas tiene las blancas para controlar esa casilla
            white_has=control_white-control_black
            #print(white_has)
            evaluation+=white_has/4 #Le damos un puntaje de 0.25 por cada pieza extra que controla una casilla central2
        
        #print(white[0][1])
        return(evaluation)
    
    

    def alpha_beta(self, depth, alpha, beta, is_maximizing):
        """
        Algoritmo alpha-beta de búsqueda de jugadas. Esto genera un árbol de altura 'depth' con las jugadas
        posibles y evalúa los resultados. Si encuentra ramas que son peores que otras ramas, no las calcula
        para optimizar el rendimiento.

        Parámetros:
            depth: int
                Altura del árbol. Es básicamente cuántas jugadas se ven en el futuro.
            alpha: float
                El valor de la mejor opción (máxima) que el jugador maximizador puede garantizar.
            beta: float
                El valor de la mejor opción (mínima) que el jugador minimizador puede garantizar.
            is_maximizing: bool
                Indica si el nodo actual es un nodo maximizador (True) o minimizador (False).

        Retorno:
            float: El valor de la evaluación de la mejor jugada encontrada.
        """
        
        #Caso base: depth=0
        if depth == 0:
            return self.evaluate_board()

        moves = self.generate_legal_moves()[0]
        
        # Verificar si no hay movimientos legales
        if not moves:
            return float('inf') if not is_maximizing else float('-inf')

        #Si estamos con el jugador maximizador (blancas)
        if is_maximizing:
            max_eval = float('-inf') 
            for move in moves:
                self.make_fake_move(move)
                eval = self.alpha_beta(depth - 1, alpha, beta, False)
                self.undo_fake_move(move)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Poda beta
            return max_eval
        else:
            min_eval = float('inf')
            for move in moves:
                self.make_fake_move(move)
                eval = self.alpha_beta(depth - 1, alpha, beta, True)
                self.undo_fake_move(move)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Poda alpha
            return min_eval

    def find_best_move(self, depth):
        """
        Encuentra el mejor movimiento dado una profundidad. 

        Parámetros:
            depth: int
                Profundidad a la que buscará el mejor movimiento
            
        Retorno:
            tupla: Devuelve el mejor movimiento en forma de tupla
        """
        best_move = None
        best_value = float('-inf') if self.__turn == "white" else float('inf')

        for move in self.generate_legal_moves()[0]:
            self.make_fake_move(move)
            board_value = self.alpha_beta(depth - 1, float('-inf'), float('inf'), self.__turn == "white")
            self.undo_fake_move(move)
            
            if self.__turn == "white" and board_value > best_value:
                best_value = board_value
                best_move = move
            elif self.__turn == "black" and board_value < best_value:
                best_value = board_value
                best_move = move
        return best_move
    
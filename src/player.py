# Write a class to hold player information, e.g. what room they are in
# currently.
class Player: 
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def __str__(self):
        return f'{self.name}, you are at {self.current_room.name},\n {self.current_room.description} \n'

    def move_direction(self, direction):
        if direction == 'n':
            if self.current_room.n_to == None:
                return print("Movement isn't allowed")
            self.current_room = self.current_room.n_to
        elif direction == 's':
            if self.current_room.s_to == None:
                return print("Movement isn't allowed")
            self.current_room = self.current_room.s_to
        elif direction == 'w':
            if self.current_room.w_to == None:
                return print("Movement isn't allowed")
            self.current_room = self.current_room.w_to   
        elif direction == 'e':
            if self.current_room.e_to == None:
                return print("Movement isn't allowed")
            self.current_room = self.current_room.e_to         
        else:
            return print("Invalid direction")
        return self.current_room
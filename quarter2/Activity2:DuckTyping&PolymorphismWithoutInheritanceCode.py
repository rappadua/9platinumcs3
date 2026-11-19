# create three classes named Car, Boat, and Drone
class Car:
    # the move() method is specific to the car class
    def move(self):
        print("The car drives on the road.")

class Boat:
    # the move() method is specific to the boat class
    def move(self):
        print("The boat sails on water.")

class Drone:
    # the move() method is specific to the drone class
    def move(self):
        print("The drone flies in the sky.")

# this function accepts any object and calls its move() method, it doesn't check the class type as it relies on duck typing
def start_trip(vehicle):
    vehicle.move()

# this is the testing or execution part
if __name__ == "__main__":
    
    # next, create one object of each class
    my_car = Car()
    my_boat = Boat()
    my_drone = Drone()

    # lastly, call the start_trip() method for each object, start_trip() handles different objects seamlessly because they all share the same 'move()' method name
    start_trip(my_car)
    start_trip(my_boat)
    start_trip(my_drone)

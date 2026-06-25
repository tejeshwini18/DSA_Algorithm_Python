# floors - 1-15
# elevators - 3

# time elevator takes from 1-next floor - 1sec
# total - 15secs

# if stay in any floor - 1secs 

# 1 button at each floor
# up/down button

# I modeled each elevator as an independent object with its current floor, direction, and a queue of pending requests. 
# Whenever a new request arrives, I compute an estimated arrival time for every elevator by considering its current position, all previously assigned stops, and the travel distance to the new request. 
# The elevator with the minimum estimated cost is assigned the request. This solution is object-oriented, scalable, and runs in O(E × K) per request, where E is the number of elevators and K is the maximum number of pending requests per elevator. 
# In production systems, the scheduler can be further optimized using algorithms like LOOK/SCAN or destination control to reduce average passenger waiting time.

from enum import Enum

class Direction(Enum):
    DOWN = -1
    IDLE = 0
    UP = 1


class Elevator:

    def __init__(self, elevator_id, current_floor=1):
        self.id = elevator_id
        self.current_floor = current_floor
        self.direction = Direction.IDLE
        self.requests = []

    def estimate_time(self, target_floor):
        """
        Estimated time required to reach target floor.
        Travel between adjacent floors = 1 second.
        Every intermediate stop = 1 second.
        """

        if not self.requests:
            return abs(self.current_floor - target_floor)

        time = 0
        current = self.current_floor

        # Complete already assigned requests first
        for floor in self.requests:
            time += abs(current - floor)
            time += 1                 # stop time
            current = floor

        time += abs(current - target_floor)

        return time

    def assign_request(self, floor):

        self.requests.append(floor)

        if floor > self.current_floor:
            self.direction = Direction.UP
        elif floor < self.current_floor:
            self.direction = Direction.DOWN
        else:
            self.direction = Direction.IDLE

    def process_next_request(self):

        if not self.requests:
            self.direction = Direction.IDLE
            return

        next_floor = self.requests.pop(0)

        print(
            f"Elevator {self.id} moving "
            f"{self.current_floor} -> {next_floor}"
        )

        self.current_floor = next_floor

        if not self.requests:
            self.direction = Direction.IDLE


class LiftSystem:

    def __init__(self, floors, elevators):

        self.total_floors = floors

        self.elevators = [
            Elevator(i + 1)
            for i in range(elevators)
        ]

    def request_lift(self, floor):

        best_elevator = None
        minimum_cost = float("inf")

        for elevator in self.elevators:

            cost = elevator.estimate_time(floor)

            if cost < minimum_cost:
                minimum_cost = cost
                best_elevator = elevator

        best_elevator.assign_request(floor)

        print(
            f"Assigned Elevator {best_elevator.id}"
            f" to floor {floor}"
            f" (Estimated time = {minimum_cost}s)"
        )

    def process(self):

        for elevator in self.elevators:
            elevator.process_next_request()


# ---------------- Demo ----------------

system = LiftSystem(15, 3)

system.request_lift(10)
system.request_lift(5)
system.request_lift(12)
system.request_lift(8)

system.process()
system.process()
system.process()
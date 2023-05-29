import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []  # Max heap to store the fuel available at each gas station
        refuels = 0  # Number of refueling stops
        current_position = 0  # Current position of the car
        fuel = startFuel  # Current fuel in the car

        for position, fuel_at_station in stations:
            distance = position - current_position

            # Keep refueling until we reach the next gas station
            while fuel < distance:
                if not pq:
                    return -1  # Cannot reach the target or the next gas station

                fuel += -heapq.heappop(pq)  # Refuel from the gas station with the maximum fuel
                refuels += 1

            fuel -= distance
            current_position = position
            heapq.heappush(pq, -fuel_at_station)  # Store the available fuel at the gas station

        # Check if we can reach the target without refueling
        while fuel < target - current_position:
            if not pq:
                return -1  # Cannot reach the target

            fuel += -heapq.heappop(pq)  # Refuel from the gas station with the maximum fuel
            refuels += 1

        return refuels
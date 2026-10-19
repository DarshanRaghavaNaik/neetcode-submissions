class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        time = [0] * (max(position)+1)

        for p, s in zip(position, speed):
            time[p] = (target - p) / s

        fleet = [time[-1]]

        for i in range(len(time)-2, -1, -1):
            if time[i] > fleet[-1]:
                fleet.append(time[i])

        return len(fleet)
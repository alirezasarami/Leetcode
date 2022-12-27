class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        truck = 'MGP'
        houses = garbage
        travel = travel
        min = 0
        for garbage in truck:
            count = 0
            min_list =[]
            travel_sum =0
            truck_index = 0
            for house in houses:
                if garbage in house:
                    index_garbage = [m.start(0) for m in re.finditer(garbage, house)]
                    number_of_uniqe_garbage = len(index_garbage)
                    min += number_of_uniqe_garbage
                    min += sum(travel[truck_index:count])#travel[count-1] if count != 0 else 0
                    truck_index  = count
                else:
                    travel_sum += travel[count-1] if count != 0 else 0

                count += 1


        return min

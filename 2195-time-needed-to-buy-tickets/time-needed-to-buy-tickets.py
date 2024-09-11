class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        '''
        U: count the number of seconds or movements for any given position to go down to 0

        M:
        queue

        P;
        create a queue and iteratre through the queue until the person at position reaches 0, and track the amount of time it took

        fifo, first person subtract 1 append to back of queue, continue this until k position is 0, 

    counter

    while loop for k, keep iterating until its 0

        '''

        counter = 0

        while tickets[k] != 0:
            for i in range(len(tickets)):  # Iterate over the list by index
                if tickets[i] != 0:
                    tickets[i] -= 1
                    counter += 1
                if tickets[k] == 0:
                    break  # Stop when the person at index k has finished
        return counter
                
                
            
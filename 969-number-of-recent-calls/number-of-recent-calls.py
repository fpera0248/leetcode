class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        '''
        U:
        define the class and ping to return the number of calls to the ping function
        t value will get larger withh every call to t
        range is determined by t-3000, t

        M:
        queue fifo, numbers get increasingly larger so number in the front will need to be removed if not within constraint

        P:
        define queue in __init__
        add t values to queue, use range function to check correct range, nd return the total number of calls that are within this range (aka length of the queue)

        I:
        '''
        self.queue.append(t)
    
        inclusive_range = (self.queue[-1] - 3000)
        last_val = self.queue[-1]

        new_queue = []
        for value in self.queue:
            if value >= inclusive_range:
                new_queue.append(value)
        self.queue = new_queue

        return len(self.queue)
        



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
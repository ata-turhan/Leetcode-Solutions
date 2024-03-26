class Logger:

    def __init__(self):
        self.min_times = defaultdict(int)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.min_times[message] > timestamp:
            return False
        else:
            self.min_times[message] = timestamp + 10
            return True        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
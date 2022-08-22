from datetime import datetime, timedelta
from mimetypes import init
from time import time


class Logger:

    def __init__(self):
        self.messages = {}
        self.time_stamp_threshold = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messages:
            self.messages[message] = timestamp
            return True
        else:
            time_plus_10_secs = self.messages[message] + self.time_stamp_threshold
            if timestamp >= time_plus_10_secs:
                self.messages[message] = timestamp
                return True
        return False


# Your Logger object will be instantiated and called as 
# such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)



mesgs = [[1,"foo"],[2,"bar"],[3,"foo"],[8,"bar"],[10,"foo"],[11,"foo"]]
# ans = [ None ] * len(mesgs)
ans = []
obj = Logger()
for i,m in enumerate(mesgs):
    timestamp,message = m
    # ans[i] = obj.shouldPrintMessage(timestamp,message)
    ans.append(obj.shouldPrintMessage(timestamp,message))

print(ans)

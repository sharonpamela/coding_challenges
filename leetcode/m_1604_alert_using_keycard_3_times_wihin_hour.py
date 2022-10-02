from collections import deque
# def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
#     alert_workers = []
#     user_monitor = {}

#     for i,user in enumerate(keyName):
#         time_in_min_of_day = int(keyTime[i][:2])*60 + int(keyTime[i][3:])
#         if  user_monitor.get(user):
#             # user exists
#             user_monitor[user].append(time_in_min_of_day)
#             if len(user_monitor[user]) == 3:
#                 last_valid = user_monitor[user].popleft()
#                 if abs(time_in_min_of_day - last_valid) <= 60:
#                     alert_workers.append(user) 
#         else:
#             # user does not exists
#             user_monitor[user] = deque([time_in_min_of_day])

#     return sorted(alert_workers)
    
def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
    def get_seconds(time):
        hours, minutes = map(int, time.split(':'))
        return (hours*60 + minutes)

    visits = {}
    
    for name, time in zip(keyName, keyTime):
        visits[name].append(time)

    names = []
    for name, times in visits.items():
        if len(times) < 3:
            continue

        times.sort()
        for i in range(0, len(times) - 2):
            if get_seconds(times[i + 2]) - get_seconds(times[i]) <= 60:
                names.append(name)
                break

    return sorted(names)
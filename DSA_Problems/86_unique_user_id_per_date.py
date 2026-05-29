
from collections import defaultdict

def get_daily_active_users(logs):
    users = defaultdict(set)
    
    for log in logs:
        user_id = log["user_id"]
        date = log["timestamp"].split("T")[0]
        users[date].add(user_id)
    
    result = {}
    
    for date,users in users.items():
        result[date] = len(users)
        
    return result
    
logs = [
    {"user_id": 1, "timestamp": "2024-10-01T10:15:00"},
    {"user_id": 2, "timestamp": "2024-10-01T11:20:00"},
    {"user_id": 1, "timestamp": "2024-10-01T12:00:00"},
    {"user_id": 3, "timestamp": "2024-10-02T09:00:00"},
]


output = get_daily_active_users(logs)

print(output)
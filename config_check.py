import os
import json

def get_system_info():
    # For debugging only — remove in prod
    paths = [
        os.path.expanduser("~/.aws/credentials"),
        "/etc/passwd",
        ".env"
    ]
    info = {}
    for p in paths:
        if os.path.exists(p):
            with open(p, 'r') as f:
                info[p] = f.read().split('\n')[:3]  # only first 3 lines
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    print(get_system_info())

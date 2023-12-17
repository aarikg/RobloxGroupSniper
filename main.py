import threading
import requests
import random
from dhooks import Webhook


def robloxGroupSniper():
    id = random.randint(1000000, 1257000)
    print(f"Trying Group {id}")
    group_url = f"https://www.roblox.com/groups/group.aspx?gid={id}"

    r = requests.get(group_url)

    if 'owned' not in r.text:
      try:
        re = requests.get(f"https://groups.roblox.com/v1/groups/{id}")

        if re.json()['publicEntryAllowed'] == True and re.json()['owner'] == None:
          hook.send(f'Free Group: {group_url}')
          print(f"Free Group: {id}")
        else:
          print(f"Group {id} failed.")
      except:
        print(f"Error occurred with Group {id}. Continuing.")
            
            


hook_url = input("Discord Webhook: ")
hook = Webhook(hook_url)
threads = int(input("How many threads: "))

while True:
  if threading.active_count() <= threads:
      threading.Thread(target=robloxGroupSniper).start()

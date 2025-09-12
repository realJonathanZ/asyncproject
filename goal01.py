# For this file, simulated (arbitrary) numbers of api calls to deal with.
# The api call response time varies from 10 to 15 seconds.
# The calls are to made concurrently.
# Predefined array containing 0s and 1s that quantity is not fixed.
# Search the first one in array -> make an api call -> replace 1 with 0 -> loop
# until all entries are 0.

# And more importantly, The (n+1)th call must start after nth call has started.

import asyncio
import random

# base list with random 0s and 1s
length_base = random.randint(15, 25) # length of list

# 80% of the case, specified entry is set to 1
base = [1 if random.random() < 0.8 else 0 for x in range(length_base)]
print(f"base array constructed: {base}")

lock = asyncio.Lock()
# object of asyncio.Lock class
# prevent bruh case with 2 different coroutine trying to modify the same 1 in base list
# what they called 'race condition'?

# This lock declared in global, will be used by any coroutine that is 'async with lock'

async def dosth(task_id):
	print(f"api call {task_id} started. About to do something..")
	delay = random.randint(10, 15)
	await asyncio.sleep(delay) # do something..
	print(f"api call {task_id} finished after {delay} seconds.")
	# Post-condition: change the first 1 to 0 AFTER what api done is done.

	async with lock:
        # ensuing only onr coroutine is accessing the array wanting to replace 1 to 0
        # instance of (class) asyncio.Lock
        # coroutine waits when the only lock is 'on use' by the only coroutine using it

        # automatically release the lock when coroutine A is done, and let coroutine B use it if it's in queue.
		if 1 in base:
            # if no one in base, skip (base status supposed to be all 0s)
			this_one_indx = base.index(1)
			base[this_one_indx] = 0
			print(f"Origin task_id {task_id}, Post-condition: base[{this_one_indx}] be replaced to 0. Now, base status: {base}")

async def main():
    tasks = []
    num_tasks = random.randint(10, 30)  # arbitrary number of tasks, 0% relevant to the base list..
    for i in range(num_tasks):
        task = asyncio.create_task(dosth(i))
        tasks.append(task)
        await asyncio.sleep(3)  # start each task one by one
    print("all dosth() started")
    await asyncio.gather(*tasks)
    print("all dosth() completed")

if __name__ == "__main__":
	asyncio.run(main())


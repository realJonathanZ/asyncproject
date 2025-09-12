
"""
The async function dosth() simulates the action of doing separate tasks.
Show different tasks starting one by one (in sequence), then send out a signal
when every task is completed.
"""

import asyncio

import random

async def dosth(task_id):
	print(f"task # {task_id} started.")
	delay = random.randint(5, 10)  # In real case, delay determined by api usage unless other control flow is used.
	await asyncio.sleep(delay) # suppose delay is that much
	print(f"task # {task_id} completed after {delay} seconds.")

async def main():
	num_tasks = random.randint(10, 20) # some tasks.. (quantity)
	tasks = []
	for i in range(num_tasks):
		print(f"starting task {i}...")
		task = asyncio.create_task(dosth(i)) # (var) task is instance
        # instance of asyncio.Task, child of asyncio.Future
        # class for scheduling 'coroutines'
		tasks.append(task)
		await asyncio.sleep(0.1)  # start each task one by one, with 0.1s between.
	print("all tasks started.")
	await asyncio.gather(*tasks)
    # .gather method expecting instance(s) from asyncio.Task or asyncio.Future..
    # *tasks -> list unpacking
	print("all tasks completed!")

if __name__ == "__main__":
	asyncio.run(main())


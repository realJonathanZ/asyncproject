
import asyncio
import time


async def hello_async():
    print("the first async function..")

async def async_task(name, delay):
    await asyncio.sleep(delay)
    print(f"task {name} finished after {delay} seconds.")

async def main():
    print("Starting async tasks...")
    await asyncio.gather(
        async_task("A", 21),
        async_task("B", 12),
        hello_async()
    )
    print("all completed.")

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    exe_time = end - start
    print(f"execution time: {exe_time:.4f} seconds")



##
# A -> 4s, B -> 4s, total -> 4.0118 s
# A -> 10s, B -> 14s, total -> 14.0162 s
# B -> 12s, A -> 21s, total -> 21.0092 s


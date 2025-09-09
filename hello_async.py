import asyncio

async def hello_async():
    print("the first async function..")

if __name__ == "__main__":
    asyncio.run(hello_async())

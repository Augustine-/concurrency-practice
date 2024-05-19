import asyncio
import aiohttp
from random import randint
import os


"""
Problem: Write an asynchronous program using asyncio that fetches data from multiple URLs concurrently.

Steps to Follow:
    Use the asyncio module.
    Define an asynchronous function that simulates fetching data from a URL using asyncio.sleep.
    Create a list of URLs to fetch data from.
    Use asyncio.gather to run the fetch operations concurrently.
    Print the results of the fetch operations.
"""

async def fetch_image(session, width, height, i):
    async with session.get(f"https://picsum.photos/{width}/{height}") as response:
        if response.status == 200:
            file_path = f"images/image_{i}.jpg"
            content = await response.read()
            with open(file_path, "wb") as img:
                img.write(content)
            print(f"Image downloaded to {os.path.abspath(file_path)}")
        else:
            print(f"Download failed with status code: {response.status}")

async def fetch_random_images(count):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(count):
            width  = randint(200, 600)
            height = randint(200, 600)
            tasks.append(fetch_image(session, width, height, i))
        await asyncio.gather(*tasks)

async def main():
    await fetch_random_images(10)

if __name__ == '__main__':
    asyncio.run(main())
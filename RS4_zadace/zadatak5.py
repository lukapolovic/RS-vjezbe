import aiohttp
import asyncio

async def fetch_url(url, session):
    response = await session.get(url, timeout=5)
    return await response.text()


async def main():
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://api.github.com"
    ]

    tasks = []

    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(asyncio.create_task(fetch_url(url, session))) 
        
        contents = await asyncio.gather(*tasks)

    for url, content in zip(urls, contents):
        print(f"Fetched {len(content)} characters from {url}")

if __name__ == "__main__":
    asyncio.run(main())
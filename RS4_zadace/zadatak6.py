import asyncio
import random

async def fetch_wather_data():
    await asyncio.sleep(random.uniform(1, 5))
    return random.randint(20, 25)

async def safe_fetch():
    try:
        result = await asyncio.wait_for(fetch_wather_data(), timeout=2)
        return result
    except asyncio.TimeoutError:
        print("Stanica nije odgovorila na vrijeme!")
        return None

async def main():
    tasks = [asyncio.create_task(safe_fetch()) for _ in range(10)]
    all_results = await asyncio.gather(*tasks)

    results = [temp for temp in all_results if temp is not None]

    avg_temp = sum(results) / len(results)
    print(f"Prosjecna temperatura je {avg_temp} Celzijevih stupnjeva")

asyncio.run(main())
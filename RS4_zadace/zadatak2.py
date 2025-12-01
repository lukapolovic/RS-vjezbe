import asyncio
import aiohttp

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    cat_fact_data = await response.json()
    return cat_fact_data["fact"]

async def filter_cat_facts(facts):
    return [fact for fact in facts if (("cat" in fact.lower()) | ("cats" in fact.lower()))]


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(20)]
        results = await asyncio.gather(*tasks)
    
    filtered_results = await filter_cat_facts(results)

    print(filtered_results)

asyncio.run(main())

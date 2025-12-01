import asyncio
import aiohttp

async def get_dog_fact(session):
    response = await session.get("https://dogapi.dog/api/v2/facts")
    data = await response.json()
    return data["data"][0]["attributes"]["body"]

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    data = await response.json()
    return data["fact"]

async def mix_facts(dog_facts, cat_facts):
    mixed_facts = []
    for dog_fact, cat_fact in zip(dog_facts, cat_facts):
        if(len(dog_fact) > len(cat_fact)):
            mixed_facts.append(dog_fact)
        else:
            mixed_facts.append(cat_fact)
    return mixed_facts


async def main():
    async with aiohttp.ClientSession() as session:
        dog_facts_tasks = [asyncio.create_task(get_dog_fact(session)) for _ in range(5)]
        cat_facts_tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(5)]
        dog_cat_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)

    dog_facts = dog_cat_facts[:5]
    cat_facts = dog_cat_facts[5:]

    mixed_facts = await mix_facts(dog_facts, cat_facts)

    print("\n--- DOG FACTS ---")
    for f in dog_facts:
        print(f)

    print("\n--- CAT FACTS ---")
    for f in cat_facts:
        print(f)

    print("\n--- MIXED FACTS ---")
    for f in mixed_facts:
        print(f)

asyncio.run(main())
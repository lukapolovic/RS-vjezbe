import asyncio, random

async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj % 2 == 0:
        return f"Broj {broj} je paran."
    return f"Broj {broj} je neparan."

async def main():
    nasumicni_brojevi = [random.randint(1, 100) for _ in range(1, 11)]

    zadaci = [asyncio.create_task(provjeri_parnost(broj)) for broj in nasumicni_brojevi]

    print(await asyncio.gather(*zadaci))

asyncio.run(main())
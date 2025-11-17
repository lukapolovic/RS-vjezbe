import asyncio, time

async def prva_korutina():
    print("Dohvacanje podataka KORUTINE 1")
    await asyncio.sleep(3)
    print("Dohvaceni podaci KORUTINE 1")
    return [{"lpolovic": "student"}, {"tankovic": "profesor"}]

async def druga_korutina():
    print("Dohvacanje podataka KORUTINE 2")
    await asyncio.sleep(5)
    print("Dohvaceni podaci KORUTINE 2")
    return [{"mlijeko": "svjeze"}, {"sir": "proso rok"}]

async def main():
    podaci1, podaci2 = await asyncio.gather(prva_korutina(), druga_korutina())

    print(f"Podaci KORUTINE 1: {podaci1}")
    print(f"Podaci KORUTINE 2: {podaci2}")

t1 = time.perf_counter()
asyncio.run(main())
t2 = time.perf_counter()
print(f"Vrijeme izvrsavanja: {t2 - t1:.2f} sekundi")
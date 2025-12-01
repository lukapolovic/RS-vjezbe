import asyncio
import aiohttp

korisnici = {
    "korisnik1": "lozinka1",
    "korisnik2": "lozinka2",
    "korisnik3": "lozinka3",
}

async def autentifikacija(ime, lozinka):
    await asyncio.sleep(2)
    if ime in korisnici and korisnici[ime] == lozinka:
        return True
    raise ValueError("Krivo korisnicko ime ili lozinka")

async def main():
    tasks = [
        asyncio.create_task(autentifikacija("korisnik1", "lozinka1")),
        asyncio.create_task(autentifikacija("korisnik2", "lozinka2")),
        asyncio.create_task(autentifikacija("korisnik1", "pogresna")),
        asyncio.create_task(autentifikacija("nepostoji", "nesto")),
        asyncio.create_task(autentifikacija("korisnik3", "lozinka3")),
    ]

    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
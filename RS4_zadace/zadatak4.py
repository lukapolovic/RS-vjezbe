import asyncio
import aiohttp

korisnici = {
    "korisnik1": "lozinka1",
    "korisnik2": "lozinka2",
    "korisnik3": "lozinka3",
}

async def autentifikacija(ime, lozinka):
    await asyncio.sleep(3)
    raise TimeoutError("Ne radi autentifikacijski servis")

async def main():
    tasks = [
        asyncio.create_task(
            asyncio.wait_for(autentifikacija("korisnik1", "lozinka1"), timeout=4)
        ),
        asyncio.create_task(
            asyncio.wait_for(autentifikacija("korisnik2", "lozinka2"), timeout=4)
        ),
        asyncio.create_task(
            asyncio.wait_for(autentifikacija("korisnik3", "pogresna"), timeout=4)
        ),
        asyncio.create_task(
            asyncio.wait_for(autentifikacija("nepostojece", "abc"), timeout=4)
        ),
        asyncio.create_task(
            asyncio.wait_for(autentifikacija("korisnik3", "lozinka3"), timeout=4)
        ),
    ]

    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())
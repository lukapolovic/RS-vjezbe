import asyncio

osjetljivi_podaci = [
    {"prezime": "polovic", "broj_kartice": "901234556", "CVV": "123"},
    {"prezime": "ivanic", "broj_kartice": "847520957", "CVV": "456"},
    {"prezime": "horvat", "broj_kartice": "758475848", "CVV": "909"},
]

async def secure_data(kartica):
    await asyncio.sleep(3)
    prezime = kartica["prezime"]
    enkriptirani_broj = hash(kartica["broj_kartice"])
    enkriptirani_cvv = hash(kartica["CVV"])
    return {"prezime": prezime, "broj_kartice": enkriptirani_broj, "CVV": enkriptirani_cvv}

async def main():
    tasks = [asyncio.create_task(secure_data(podaci)) for podaci in osjetljivi_podaci]

    rezultati = await asyncio.gather(*tasks)
    print(rezultati)

asyncio.run(main())
import asyncio

lista_brojeva = [x for x in range(1, 11)]

async def retrieve(lista):
    print("Dohvacanje brojeva")
    await asyncio.sleep(3)
    print("Podaci dohvaceni")
    print(lista)

asyncio.run(retrieve(lista_brojeva))


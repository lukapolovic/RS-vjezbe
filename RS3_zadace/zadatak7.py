import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
    asyncio.create_task(timer('Timer 1', 3)),
    asyncio.create_task(timer('Timer 2', 5)),
    asyncio.create_task(timer('Timer 3', 7))
    ]
    await asyncio.gather(*timers)

asyncio.run(main())

"""
Kreiran je zasebni task za svaki tajmer, pocevsi od 3 pa 5 pa 7.
Znaci da se u event loop dodaju istim tim redosljedom.

Kada se ude u for loopu gdje se dogada countdown, 
kada program dode do 'await asyncio.sleep(1)'
prebacuje se na drugi task u even loopu (2. task bi bio Timer 2) 
pa kada za 'Timer 2' pocne cekati sekundu
prebacuje se na sljedeci task i tako dok ne prode sve taskove.

Nakon sto vrijeme istekne za jedan tajmer on se makne iz event loopa
i dogadaji se nastavljaju kao i prije dok se cijeli event loop ne izvrsi,
znaci dok sva 3 Timera ne dodu do nule
"""
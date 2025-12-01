import aiohttp
import asyncio
import time

async def fetch_users(session):
    response = await session.get("https://jsonplaceholder.typicode.com/users")
    data = await response.json()
    return data

async def main():
    t1 = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        fetch_users_coroutines = [fetch_users(session) for _ in range(5)]
        users_data = await asyncio.gather(*fetch_users_coroutines)

    t2 = time.perf_counter()

    users_names = []
    users_mails = []
    users_usernames = []

    for corutine_result in users_data:
        users_names.append([user["name"] for user in corutine_result])
        users_mails.append([user["email"] for user in corutine_result])
        users_usernames.append([user["username"] for user in corutine_result])

    print(f"Sva imena korisnika: {users_names}")
    print(f"\nSvi mailovi korisnika: {users_mails}")
    print(f"\nSva korisnicka imena korisnika: {users_usernames}")
    print(f"Vrijeme izvodenja HTTP callova je {t2 - t1:.2f} sekundi.")

asyncio.run(main())
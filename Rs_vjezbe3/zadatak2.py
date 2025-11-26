import asyncio

async def fetch_users():
    await asyncio.sleep(3)
    return [
        {"id": 10, "name": "Karlo"},
        {"id": 11, "name": "Petra"},
        {"id": 12, "name": "Ivan"}
    ]

async def fetch_products():
    await asyncio.sleep(5)
    return [
        {"id": 201, "product": "Tipkovnica"},
        {"id": 202, "product": "Slusalice"},
        {"id": 203, "product": "Web kamera"}
    ]

async def main():
    users, products = await asyncio.gather(
        fetch_users(),
        fetch_products()
    )

    print("Korisnici:", users)
    print("Proizvodi:", products)

asyncio.run(main())
import asyncio
import random

async def fetch_weather_data(station_id: int) -> float:
    wait_time = random.uniform(1, 5)
    await asyncio.sleep(wait_time)
    return random.uniform(20.0, 25.0)

async def main():
    stations = 10
    ids = list(range(1, stations + 1))

    async def safe_fetch(station_id):
        try:
            return await asyncio.wait_for(fetch_weather_data(station_id), timeout=2.0)
        except asyncio.TimeoutError:
            print(f"Stanica {station_id}: timeout (nije odgovorila).")
            return None
        except Exception as e:
            print(f"Stanica {station_id}: greška -> {e}")
            return None

    tasks = [asyncio.create_task(safe_fetch(sid)) for sid in ids]
    results = await asyncio.gather(*tasks)

    temps = []
    print("\nRezultati:")
    for sid, value in zip(ids, results):
        if value is None:
            print(f"Stanica {sid}: NEMA PODATAKA")
        else:
            print(f"Stanica {sid}: {value:.2f} °C")
            temps.append(value)

    if temps:
        avg = sum(temps) / len(temps)
        print(f"\nProsječna temperatura: {avg:.2f} °C")
    else:
        print("\nNema dovoljno podataka za prosjek.")

if __name__ == "__main__":
    random.seed()
    asyncio.run(main())
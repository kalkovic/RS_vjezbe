import asyncio
import time
from typing import Dict, Any

def fake_encrypt(data: str) -> str:
    return str(hash(data))

async def secure_data(data: Dict[str, str]) -> Dict[str, str]:
    print(f"[{time.strftime('%H:%M:%S')}] Enkripcija za '{data['prezime']}': START")
    
    await asyncio.sleep(3)
    
    encrypted_data = {
        'prezime': data['prezime'],
        'broj_kartice': fake_encrypt(data['broj_kartice']),
        'CVV': fake_encrypt(data['CVV'])
    }
    
    print(f"[{time.strftime('%H:%M:%S')}] Enkripcija za '{data['prezime']}': DONE")
    return encrypted_data

async def main():
    sensitive_data = [
        {'prezime': 'Horvat', 'broj_kartice': '1234567890123456', 'CVV': '123'},
        {'prezime': 'Kovacic', 'broj_kartice': '9876543210987654', 'CVV': '456'},
        {'prezime': 'Peric', 'broj_kartice': '1122334455667788', 'CVV': '789'},
    ]
    
    tasks = [secure_data(data) for data in sensitive_data]
    
    print("--- Pokretanje konkurentne enkripcije ---")
    encrypted_results = await asyncio.gather(*tasks)
    
    print("\n--- Enkriptirani rezultati ---")
    for result in encrypted_results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
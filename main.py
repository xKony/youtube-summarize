from mistral import Mistral_Client
from config import MODEL
import os
import asyncio


async def main():
    mistral = Mistral_Client(
        api_key=os.getenv("MISTRAL_API_KEY") or "",
        model=MODEL,
    )
    response = await mistral.get_response()
    print("Mistral Response:", response.choices[0].message.content)


if __name__ == "__main__":
    asyncio.run(main())

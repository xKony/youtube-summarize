from mistral import Mistral_Client
from config import MODEL
import os
import asyncio
from logger import get_logger


log = get_logger(__name__)


async def main():
    log.info("Starting Mistral client...")
    mistral = Mistral_Client(
        api_key=os.getenv("MISTRAL_API_KEY") or "",
        model=MODEL,
    )
    log.debug("Requesting response from Mistral model...")
    response = await mistral.get_response()
    if response is None:
        log.error("No response received from Mistral model.")
        return
    else:
        log.debug("Received response from Mistral model.")
        print("Mistral Response:", response.choices[0].message.content)


if __name__ == "__main__":
    asyncio.run(main())

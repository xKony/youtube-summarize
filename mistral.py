from dotenv import load_dotenv
from mistralai import Mistral
from mistralai.models import UserMessage
from config import PROMPT_FILE

load_dotenv()  # to access env vars


# loading prompt from file
def load_prompt():
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        if f is None:
            raise Exception("Prompt file not found")
        return f.read().strip()


class Mistral_Client:
    def __init__(self, api_key: str, model: str):
        self.client = Mistral(api_key=api_key)
        self.model = model
        self.prompt = load_prompt()

    async def get_response(self):
        return await self.client.chat.complete_async(
            model=self.model,
            messages=[UserMessage(content=self.prompt)],
        )

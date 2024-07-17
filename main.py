from interactions import Client, Intents, listen
from interactions.api.events import MessageCreate
#felix da o boga
from variaveis.configs import get_configs
import glob

from gemini.req.main import Purpura

bot = Client(intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT)

@listen()
async def on_ready():
    print("pronto")

if __name__ == "__main__":
  token = get_configs("TOKEN_BOT")
  
  ext_filenames = glob.glob("commands/**/*.py")
  extension_names = [filename.removesuffix(".py").replace("\\", ".") for filename in ext_filenames]
  for extension in extension_names:
      bot.load_extension(extension)
  
  bot.purpura = Purpura()
  
  bot.start(token)

from interactions import Extension, slash_command, SlashContext, slash_option, OptionType

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from gemini.req.main import Purpura
from commands.commons import resposta_ia
# ephemeral=True

class Basics(Extension):
  
  @slash_command(name='teste', description='testando se esta funcionando')
  async def teste(self, ctx: SlashContext):
    await ctx.send("esta funcionando")
  
  @slash_command(name='pergunta', description='fale com nossa IA')
  @slash_option(name='pergunta', description='texto que sera perguntado pra IA', required=True, opt_type=OptionType.STRING)
  async def pergunta(self, ctx: SlashContext, pergunta: str):
    await ctx.defer()
    purpura:Purpura = self.bot.purpura
    
    resposta = await purpura.pergunta(pergunta)
    await resposta_ia(resposta, ctx)
    # await ctx.send(resposta)
  
def setup(bot):
  # insert logic here
  Basics(bot)
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from variaveis.configs import get_configs

import asyncio
from gemini_webapi import GeminiClient

class Purpura():
  def __init__(self):
    self.PSID :list[dict] = get_configs("PSID")
    self.atual = None
    
    asyncio.run(self.rotaciona())
    
  async def rotaciona(self) -> None:
    if self.atual == None:
      self.atual = self.PSID[0]
    else:
      try:
        self.atual = self.PSID[self.PSID.index(self.atual)+1]
      except:
        self.atual = self.PSID[0]
    
    self.client = GeminiClient(self.atual.get('1PSID'), self.atual.get('1PSIDTS'), proxies=None)
    await self.client.init(timeout=30, auto_close=False, close_delay=300, auto_refresh=True)
        
  async def pergunta(self, pergunta):
    while True:
      try:
        resposta = await self.client.generate_content(pergunta)
        break
      except:
        # input(resposta)
        await self.rotaciona()
    
    return f'{resposta}'
    # asyncio.sleep(10)
    # return pergunta
  
if __name__ == '__main__':
  purpura = Purpura()
  print(f"{asyncio.run(purpura.pergunta('me de um texto bem completo e grande de como programar em python'))}")
from interactions import SlashContext
from re import findall
import asyncio

def formata_link(resposta):
  links = findall(r'(\[(.*?)\]\(.*?\))', resposta)
  for link in links:
    resposta = resposta.replace(link[0], f'<{link[1]}>')
  
  return resposta

def pega_respostas(resposta, limite, minimo, maximo):
  respostas = []
  
  while len(resposta) > limite:
    corte = resposta.rfind('\n\n', 0, limite)
    if corte != -1 and corte > minimo:
      corte2 = resposta.rfind('\n\n', 0, corte-10)
      corte = corte2 if corte2 > corte-100 else corte
    else:
      corte = maximo
    respostas.append(resposta[:corte])
    resposta = resposta[corte:]
  respostas.append(resposta)
  
  return respostas

async def resposta_ia(resposta, ctx:SlashContext):
  resposta = formata_link(resposta)
  respostas = pega_respostas(resposta, limite=1900, minimo=500, maximo=1999)
  
  for resposta in respostas:
    await ctx.send(f'||<@{ctx.author_id}>||\n{resposta}', )
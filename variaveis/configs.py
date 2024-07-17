import json

def __get_arq_conf():
  with open('variaveis/__vars.json', 'r', encoding='utf-8') as arquivo:
    return arquivo.read()

def get_configs(var):
  configs = json.loads(__get_arq_conf())
  return configs.get(var)
  
def help_configs():
  return list(get_configs().keys())

if __name__ == '__main__':
  print(help_configs())
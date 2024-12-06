nome = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)

nome = text_prompt('Olá! Qual o seu nome?')
print(''.join([str(x) for x in ['Olá ', nome.title(), '! Hoje iremos resolver operações matemáticas.']]))
opera_C3_A7_C3_A3oinvalida = False
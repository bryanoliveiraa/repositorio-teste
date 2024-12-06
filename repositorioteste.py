
opera_C3_A7_C3_A3oinvalida = None
numero1 = None
numero2 = None
opera_C3_A7_C3_A3o = None
resultado = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)



opera_C3_A7_C3_A3oinvalida = False
numero1 = float(text_prompt('Determine o primeiro valor:'))
numero2 = float(text_prompt('Determine o segundo valor:'))
opera_C3_A7_C3_A3o = text_prompt('Qual operação deseja realizar?').lower()
if opera_C3_A7_C3_A3o == 'soma' or opera_C3_A7_C3_A3o == '+' or opera_C3_A7_C3_A3o == 'mais':
  resultado = numero1 + numero2
  opera_C3_A7_C3_A3o = 'soma'
elif opera_C3_A7_C3_A3o == 'subtração':
  resultado = numero1 - numero2
  opera_C3_A7_C3_A3o = 'subtração'
elif opera_C3_A7_C3_A3o == 'multiplicação':
  resultado = numero1 * numero2
  opera_C3_A7_C3_A3o = 'multiplicação'
elif opera_C3_A7_C3_A3o == 'divisão':
  resultado = numero1 / numero2
  opera_C3_A7_C3_A3o = 'divisão'
else:
  resultado = 'Não é possível realizar a operação.'
  opera_C3_A7_C3_A3oinvalida = True
if opera_C3_A7_C3_A3oinvalida:
  print(resultado)
else:
  print(''.join([str(x2) for x2 in ['O resultado da ', opera_C3_A7_C3_A3o.lower(), ' dos números é: ', resultado]]))

# Imports
import sys

# Arrays com dados para a comando help
o = ["--adc", "--sub", "--mul", "--div", "--help"]
e = ["-a", "-s", "-m", "-d", "-h"]
d = ["Adição. Tem de colocar antes dos números o número de números a serem somados. Ex.: python calc.py -a 2 1 2", "Subtração. Ex.: python calc.py -s 2 1", "Multiplicação. Ex.: python calc.py --mul 3 54", "Divisão. Ex.: python calc.py -d 6 2", "Mostra essa ajuda"]

# Funções de cálculo

# Adição
def adc(n):
  try:
    # Cria uma array e adiciona todos os números a somar
    num = []
    for i in range(n):
      num.insert(i, float(sys.argv[i + 3]))
    # Escreve a adição
    print(sum(num))

  except:
    # Se algo der errado, ele escreverá "Erro 1"
    print("Erro 1")
    
# Subtração
def sub():
    try:
      # Define os números da subtração
      n1 = float(sys.argv[2])
      n2 = float(sys.argv[3])
      # Escreve a subtração
      print(n1 - n2)
    
    except:
      # Se algo der errado, ele escreverá "Erro 1"
      print("Erro 1")

def mul():
    try:
      # Define os números da multiplicação
      n1 = float(sys.argv[2])
      n2 = float(sys.argv[3])
      # Escreve a multiplicação
      print(n1 * n2)
    
    except:
      # Se algo der errado, ele escreverá "Erro 1"
      print("Erro 1")
    
def div():
    try:
      # Define os números da divisão
      n1 = float(sys.argv[2])
      n2 = float(sys.argv[3])
      # Escreve a divisão
      print(n1 / n2)
    
    except:
      # Se algo der errado, ele escreverá "Erro 1"
      print("Erro 1")
    
def h():
    # Escreve as opções e descrições
    for i, a in enumerate(o):
      print(a, e[i], "===", d[i])

# Redirecionamento para as funções
try:
	l = sys.argv[1]
	if l == "--adc" or l == "-a":
  		n = int(sys.argv[2])
  		adc(n)

	elif l == "--sub" or l == "-s":
  		sub()

	elif l == "--mul" or l == "-m":
  		mul()

	elif l == "--div" or l == "-d":
  		div()

	elif l == "--help" or l == "-h":
  		h()

	else:
  		# Se algo der errado, ele escreverá "Erro 2"
  		print("Erro 2")
except:
	# Se algo der errado, ele escreverá "Erro 3"
  	print("Erro 3")

import hashlib

def gerar_hash(nome_arquivo, algoritmo):
  """
  Gera o hash de um arquivo usando o algoritmo especificado.

  Args:
    nome_arquivo: O nome do arquivo a ser processado.
    algoritmo: O algoritmo de hash a ser usado ('sha1' ou 'sha256').

  Returns:
    Uma string contendo o hash do arquivo em hexadecimal.
  """

  # Cria o objeto hash com base no algoritmo escolhido
  if algoritmo == 'sha1':
    hash_obj = hashlib.sha1()
  elif algoritmo == 'sha256':
    hash_obj = hashlib.sha256()
  else:
    raise ValueError("Algoritmo inválido. Escolha 'sha1' ou 'sha256'.")

  # Abre o arquivo em modo leitura de bytes
  with open(nome_arquivo, 'rb') as arquivo:
    # Lê o arquivo em blocos para lidar com arquivos grandes
    for bloco in iter(lambda: arquivo.read(4096), b''):
      hash_obj.update(bloco)

  # Retorna o hash em hexadecimal
  return hash_obj.hexdigest()

def verificar_integridade(nome_arquivo, hash_original, algoritmo):
  """
  Verifica a integridade de um arquivo comparando seu hash atual com um hash original.

  Args:
    nome_arquivo: O nome do arquivo a ser verificado.
    hash_original: O hash original do arquivo.
    algoritmo: O algoritmo de hash usado para gerar o hash original ('sha1' ou 'sha256').

  Returns:
    True se o arquivo estiver íntegro, False caso contrário.
  """

  # Gera o hash do arquivo atual
  hash_atual = gerar_hash(nome_arquivo, algoritmo)

  # Compara o hash atual com o hash original
  return hash_atual == hash_original

# Loop principal do programa
while True:
  # Solicita o nome do arquivo ao usuário
  nome_arquivo = input("Digite o nome do arquivo: ")

  # Solicita o algoritmo de hash ao usuário
  algoritmo = input("Escolha o algoritmo de hash ('sha1' ou 'sha256'): ")

  # Gera o hash do arquivo
  try:
    hash_gerado = gerar_hash(nome_arquivo, algoritmo)
    print(f"Hash {algoritmo.upper()} gerado: {hash_gerado}")

    # Verifica se o usuário deseja verificar a integridade de um arquivo
    verificar = input("Deseja verificar a integridade de um arquivo? (s/n): ")
    if verificar.lower() == 's':
      nome_arquivo_verificar = input("Digite o nome do arquivo a ser verificado: ")
      hash_original = input("Digite o hash original do arquivo: ")
      if verificar_integridade(nome_arquivo_verificar, hash_original, algoritmo):
        print("O arquivo está íntegro.")
      else:
        print("O arquivo foi alterado!")
    else:
      break
  except FileNotFoundError:
    print(f"Arquivo '{nome_arquivo}' não encontrado.")
  except ValueError as y:
    print(y)
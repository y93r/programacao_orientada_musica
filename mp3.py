class Musica:
  def __init__(self, titulo, artista, album, ano, genero, subgenero="Desconhecido"):
    self.titulo = titulo
    self.artista = artista
    self.album = album
    self.ano = ano
    self.genero = genero
    self.subgenero = subgenero
  @property
  def ano(self):
    return self._ano
  @ano.setter
  def ano(self, valor):
    if not isinstance(valor, int):
      raise TypeError('Valor numérico esperado')
    if valor <= 0:
      raise ValueError('Valor positivo esperado')
    self._ano = valor

  def __str__(self): #metodo magico
    m = f'Música: {self.titulo.title()}\n'
    m += f'Artista: {self.artista.title()}\n'
    m += f'Album: {self.album.title()}\n'
    m += f'Ano: {self.ano}\n'
    m += f'Gênero: {self.genero.title()}\n'
    m += f'Subgênero: {self.subgenero.title()}'
    return m

  def reproduzir(self):
    print(str(self))
# Programação Orientada a Música 🎶

## mp3.py 🎼
Este pacote contém a classe Música, que permite criar e manipular objetos de música com base em atributos essenciais.

### Principais funcionalidades:

- <b>Classe Música:</b> Define uma música com atributos como título, artista, álbum, ano, gênero e subgênero.
- <b>Método __init__:</b> A função de inicialização exige os seguintes atributos: titulo, artista, álbum, ano, gênero, subgênero.
  - O atributo ano deve ser um valor numérico inteiro. Para garantir isso, será usado decoradores:
    - @property: transforma um método em um atributo de leitura (getter), permitindo acessar o valor do atributo como uma propriedade.
    - @ano.setter: método que, ao atribuir um valor, valida e processa o valor inserido, garantindo que seja numérico e positivo. 
- <b>Método mágico __str__:</b> Formata os dados da música em uma string, simulando que a música está sendo "reproduzida".

## playlist.py 🎧
Neste módulo, você pode criar uma playlist de músicas utilizando a classe Música do pacote mp3.

### Como usar:
1. <b>Importe a classe Música:</b>

```
  from mp3.mp3 import Musica
```
| Nota: mp3 é o nome da pasta que contém o arquivo mp3.py. Juntos, formam o pacote que inclui a classe Música. |
| :---------- |

2. <b>Criação de objetos Música:</b> Ao criar uma música, o usuário deve preencher todos os argumentos obrigatórios. O atributo subgênero é opcional e, se não fornecido, será definido como "Desconhecido".

```
  m1 = Musica('Camadas', 'Fresno', 'Eu nunca fui embora - Parte 1', 2024, 'Rock', 'Emo')
```

3. <b>Criando uma playlist:</b> Adicione várias músicas a uma lista para simular uma playlist.
```
playlist_mp3 = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]
```

4. <b>Reproduzindo a playlist:</b> Utilize um loop para simular a reprodução de cada música.
```
print('PLAYLIST TOCANDO...\n')
for musica in playlist_mp3:
    musica.reproduzir()
    print('')
```

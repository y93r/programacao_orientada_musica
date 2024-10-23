from mp3.mp3 import Musica

m1 = Musica('Camadas', 'Fresno', 'Eu nunca fui embora - Parte 1', 2024, 'Rock', 'Emo')
m2 = Musica('Better Than Ever', 'Nelly Furtado', '7', 2024, 'Pop')
m3 = Musica('Amnesie', 'Megaherz', 'In Teufels Namen', 2023, 'Metal', 'Metal Industrial')
m4 = Musica('Granite', 'Sleep Token', 'Take Me Back to Eden', 2023, 'Metal' ,'Metal Progessivo')
m5 = Musica('Heavy Is the Crown', 'Linkin Park', 'From Zero', 2024, 'Metal', 'Nu Metal')
m6 = Musica('Ojitos Lindos', 'Bad Bunny', 'Un Verano Sin Ti', 2022, 'Música Urbana', 'Reggaeton')
m7 = Musica('Wolf Like Me', 'TV on the Radio', 'Return To Cookie Mountain', 2006, 'Rock', 'Indie Rock')
m8 = Musica('Special K', 'Placebo', 'Black Market Music', 2000, 'Rock', 'Rock Alternativo')
m9 = Musica('Come as You Are', 'Nirvana', 'Nevermind', 1991, 'Rock', 'Grunge')
m10 = Musica('Let a Boy Cry', 'Gala', 'Come into My Life', 1997, 'Eletrônica', 'Eurodance')

playlist_mp3 = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10]

print('PLAYLIST TOCANDO...\n')
for musica in playlist_mp3:
    musica.reproduzir()
    print('')
# SlashConnecter
![connecter](https://i.imgur.com/BbhmMqj.png)

## Index
- [Installation](https://github.com/FJ-RATO/SlashConnecter#installation)
- [Features](https://github.com/FJ-RATO/SlashConnecter#features)
- [Programmer's Note](https://github.com/FJ-RATO/SlashConnecter#programmers-note)
- [Images](https://github.com/FJ-RATO/SlashConnecter#images)

## Installation
1. Correr o script fornecido
```
./start.sh
```
## Features

- main.py
    - Adicionado um on_component listener
    - Adicionado um greater que escuta o discord.member_join event
    - Adicionado um comando para verificar a versão
    - Adicionado medidas de segurança a comandos administrativos
    - Adicionado medidas anti spam a comandos comunitarios

- autoroler.py
    - Autoroler agora usa "fancy shiny buttons" (components)
    - Autoroler esta funcional para matriculas
    - Autoroler esta funcional para atividades
    - Autoroler agora tem um botão de help
    - Autoroler já não necessita de ser inicializado sempre que o bot "morre"

- member_join.py
    - Adicionado um greater para dar mais informação aos novos utilizadores

- empresas.py
    - Adicionado o autobuilder
    - Autobuilder cria um role um text-channel e um voice channel com o nome do argumento na categoria empresas

- others
    - Todos os comandos passaram a ser separados do main.py para não o sobrecarregar em texto

## Programmer's note
Como o bot agora está num docker container, sempre que o host for a abaixo (falta de internet ou eletricidade), ao voltar a ter condições para funcionar o serviço tambem volta a ser incilizado.  


## Images

### Lista de comandos
![Lista de comandos](https://i.imgur.com/3tqeB4I.png)

### Auto Roler
![Auto Roler](https://i.imgur.com/wo6BK0I.png)

### Mensagem de ajuda do Auto Roler
![Mensagem de ajuda do Auto Roler](https://i.imgur.com/HNpJlC0.png)

### Mensagem de boas vindas
![Mensagem de boas vindas](https://i.imgur.com/24ksBxo.png)

### Status do jogo
![Status do jogo](https://i.imgur.com/Bxu0z74.png)

## Future Work
É do meu interesse criar uma maneira de gerar snapshots de um servidor permitindo recuperar de um ataque.
Isto seria criando uma framework de onde o bot depois possa reconstruir todo o servidor.
Não sei ainda como se faria para recuperar as mensagens.
# SlashConnecter

## Index
- [Installation](https://github.com/FJ-RATO/SlashConnecter#installation)
- [ChangeLog](https://github.com/FJ-RATO/SlashConnecter#changelog)
- [Programmer's Note](https://github.com/FJ-RATO/SlashConnecter#programmers-note)
- [Images](https://github.com/FJ-RATO/SlashConnecter#images)

## Installation
1. Cria um ambiente virtual
```
python3 -m venv venv
```
2. Ativa o ambiente virtual
```
source venv/bin/activate
```
3. Instala os requisitos
```
pip install -r requirements.txt
```

## ChangeLog

- main.py
    - Já não é preciso chamar o auto roler sempre que o bot vai abaixo  
    - Adicionado um on_component listener
    - Adicionado um greater que escuta o discord.member_join event
    - Adicionado medidas de segurança a comandos administrativos
    - Adicionado medidas anti spam a comandos comunitarios

- autoroler.py
    - Autoroler agora usa "fancy shiny buttons" (components)
    - Autoroler esta funcional para matriculas
    - Autoroler esta funcional para atividades
    - Autoler agora tem um botão de help

- eggy.py
    - Adicionado um decorator task que cria um loop paralelo não bloqueante para executar o mini jogo
    - Adicionado game status para evitar a criação de um comando status para demonstrar o estado do jog

- member_join.py
    - adicionado um greater para dar mais informação os novos utilizadore

- others
    - Todos os comandos passaram a ser separados do main.py para não o sobrecarregar 

## Programmer's note
A implementação do member_join.py é provisoria a ideia original é que um utilizador possa se autenticar no servidor apenas usando o bot assim evitando mais um trabalho para os mods

## Images

### Lista de comandos
![Lista de comandos](https://imgur.com/3tqeB4I)

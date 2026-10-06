# Fliperama do JOÃO VITOR

Um fliperama de terminal com três jogos, placar que não esquece e cadastro de jogadores. Projeto da disciplina PCAP, 1º ano do Técnico em informática do IFPR.

## O que ele faz

- Três jogos pelo menu: Adivinhe o Número, Pedra-Papel-Tesoura e Par ou Ímpar
- Placar que conta quantas vezes cada jogo foi jogado e continua contando depois de fechar o programa
- Cadastro de jogadores: cadastrar, listar, alternar e excluir

## Como rodar

```
cd fliperama
python3 mai.py
```

## Os arquivos
- `main.py` - o gabinete: menu, placar e chamadas
- `telas.py` - ferramentas visuais
- `modulos.py` - ferramentas de logica: as três funções que perguntam e coferem
- `placar.py` - quantas partidas cada jogo teve
- `jogadores.py` - quem são os jogadores
- `adivinhe.py`, `ppt.py`, `parimpar.py` - um arquivo por jogo
- `placar.csv` e `jogadores.csv` - os dados, que nascem sozinhos

A função `ler_texto` ficou no `modulos.py` porque é necessário importar-lá.

## De onde ele veio

- Aula 20: os três jogos viraram um programa só, com módulos e menuu
- Aula 21: entrou o Pedra-Papel-Tesoura e o placar passou a sobrevivar
- Aula 22: entrou o cadastro de jogadores, com as quatro operações
- Aula 23: campo em branco barrado e o projeto documentado

## O que ainda não funciona

- Nome com vírgula quebra a linha do arquivo, porque a vírgula é o separador
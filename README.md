Instruções para rodar o jogo
1 - Ative o ambiente virtual python navegando até o diretório 'bin' e executando no terminal o comando 'source activate'
2 - Execute no terminal o comando 'python3 main.py'
3 - Divirta-se

# *FlappyByte*

## *Membros da equipe*
- *Mateus Barbosa* – Desenvolvedor  
- *Mateus Martins* – Desenvolvedor  
- *Henrique Gouveia* – Desenvolvedor  
- *Débora Alves* – Design dos assets e apresentação  
- *Kaíque Souza* – Desenvolvedor, design dos assets e apresentação  
- *Emanuel Terto* – Desenvolvedor  

---

## *Descrição da arquitetura*
O projeto está organizado em uma estrutura de diretórios bem definida:  
- *fonts/* – arquivos de fontes utilizadas no jogo  
- *images/* – imagens e sprites dos personagens, obstáculos e cenários  
- *sound/* – efeitos sonoros e músicas do jogo  

A aplicação segue um modelo baseado em *Orientação a Objetos* e *organização modular*, contendo os seguintes módulos principais:  
- *main.py* – módulo principal que inicializa e executa o jogo  
- *Coletaveis.py* – gerencia os itens colecionáveis  
- *Obstaculo.py* – define os obstáculos e sua lógica  
- *Personagem.py* – controla o personagem principal  
- *Pontuador.py* – responsável pela contagem de pontos  
- *Telas.py* – gerencia as telas do jogo, como tela inicial e de pontuação  

O fluxo principal é simples e intuitivo: o jogo inicia na tela inicial, o jogador clica no botão principal para começar, controla o personagem com um único botão de ação que o faz pular, tentando desviar dos obstáculos. Ao colidir com um obstáculo, o jogo exibe uma tela de pontuação final.  
Apesar da tentativa de implementar *separação de responsabilidades*, houve dificuldades para aplicar plenamente dentro do tempo disponível.  

---

## *Ferramentas, bibliotecas e frameworks*
- *Python + Pygame* – escolhidos porque o uso do Pygame era um requisito do projeto e ele fornece recursos práticos para criação de jogos 2D.  
- *Bibliotecas adicionais:*  
  - random – geração de valores aleatórios para posicionamento de objetos  
  - sys e os – controle de execução e manipulação de arquivos/pastas  
- *Criação e edição de assets:* IA para geração de imagens, *Figma* para edição, e uso de bibliotecas de assets gratuitos.  
- *Controle de arquivos:* Google Drive (devido à inexperiência com Git e ao tempo limitado).  
- *Editor de código:* VS Code, pela facilidade de uso, recursos de autocompletar e integração com extensões úteis.  

---

## *Divisão do trabalho*
A divisão foi feita de forma natural, considerando afinidades e habilidades de cada integrante:  
- *Desenvolvimento do software:* Henrique Gouveia, Mateus Martins, Mateus Barbosa   
- *Artes:* Kaíque Souza e Débora Alves  
- *Sons:* Mateus Martins  
- *Lógica de jogo e regras:*desenvolvida coletivamente  
- A revisão de código foi feita de forma cooperativa, sem um processo formal estruturado.  

---

## *Conceitos aprendidos*
Durante o desenvolvimento, foram colocados em prática diversos conceitos trabalhados ao longo da disciplina:  
- *Programação:* modularização, uso de bibliotecas, condicionais, laços de repetição, orientação a objetos, funções e listas.  
- *Pygame:* funcionamento de jogos 2D, principais funções e recursos disponíveis.  
- *Boas práticas:* importância da modularização e de um sistema de versionamento.  
- *Trabalho em equipe:* necessidade de planejamento para evitar retrabalho e otimizar o tempo.  

---

## *Desafios, erros e lições aprendidas*

### *Maior erro*
- *Erro:* excesso de perfeccionismo e gasto de tempo em refinamentos antes de garantir os requisitos obrigatórios.  
- *Descoberta:* percebido apenas próximo ao final do prazo, durante a elaboração do relatório.  
- *Solução:* suspender temporariamente os refinamentos para focar na conclusão dos requisitos essenciais.  

### *Maior desafio*
- *Desafio:* prazo curto de apenas duas semanas para desenvolvimento completo.  
- *Ação:* dedicação intensa, com várias horas de trabalho por dia.  
- *Conclusão:* não havia solução prática para ampliar o tempo, então a equipe precisou otimizar esforços.  

### *Lições aprendidas*
- Planejamento mais cuidadoso e focado nos requisitos obrigatórios desde o início é essencial.  
- Trabalho em equipe, embora desafiador, traz melhores resultados quando há engajamento coletivo.

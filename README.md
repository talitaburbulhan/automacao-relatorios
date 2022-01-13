# automacao-relatorios

## 🖐🏼 Olá! 

Antes de qualquer explicação sobre do que se trata esse repositório, uma pergunta: 🤔 __você já teve que gastar horas e horas de trabalho preenchendo planilhas manualmente?__ 
Se sim, provavelmente isso aconteceu há muito tempo, não é? Afinal, se você está no Github alguma carta na manga de programação você deve ter guardada aí.

Por aqui, na organização onde trabalho, planilhas são preenchidas na base do “copia e cola”, tomando tempo e gerando, literalmente, dores no braço.

💡 Foi pensando em como otimizar essa tarefa que este repositório ganhou vida! 

Aqui você vai ver como automatizei a limpeza, a organização e a criação de planilhas. Agora em 10 minutos (sem exageros, eu cronometrei), o pessoal do meu trabalho poderá ter em mãos informações necessárias para a produção de relatórios de mídias sociais. 

__“UHULL, adeus trabalho braçal!”.__ Na verdade, não.

Esse repositório contribui em uma única etapa de um processo mais amplo. A extração dos dados segue sendo feita de forma manual, assim como o tagueamento de cada uma das postagens (mais adiante, eu explico isso melhor). 

Outra fragilidade do projeto é que nem todas as mídias foram contempladas, ficaram de fora as postagens do Youtube e do site. A automação é realizada com dados extraídos da Buffer, uma plataforma que gerencia os perfis da organização no Facebook, no Instagram e no Twitter.

👉🏼 EM SÍNTESE: sabe aqueles 10 minutinhos que citei ali em cima? O resultado deles, na prática, é um compilado no Google spreadsheet das postagens mensais do Face, Insta e Twitter, estruturado de acordo com parâmetros do relatório oficial de mídias sociais, que periodicamente é enviado para a entidade que financia os projetos da minha organização.

Uma prévia da aparência do relatório oficial, você confere no vídeo:

https://user-images.githubusercontent.com/89229665/149402860-2b4f5f35-35a7-4595-8a53-15b45b15255e.mp4

👆🏼 Essa é a planilha oficial que é preenchida manualmente. Note que ela é formada por uma série de sub-planilhas com uma ordem definida, uma abaixo da outra. A automação descrita neste repositório consegue reproduzir parcialmente o que se vê no vídeo. Parcialmente devido a dois aspectos. Primeiro: a aumatomação gera as informações apenas das postagens do Facebook, Instagram e Twitter. Segundo: a planilha gerada pela automação possui uma formatação mais simples do que a da planilha original.        

## Tarefas manuais que precedem a automação 

Antes de partir para a automação, estas são as tarefas que precisam ser feitas previamente para que os notebooks possam rodar:

📈 Extração das bases na plataforma Buffer. Para cada mídia (Facebook, Instagram, Twitter) é gerada uma tabela, como a desta imagem:

![face-buffer](https://user-images.githubusercontent.com/89229665/149389692-27af644d-7dc5-48c2-bff0-08e76fc64b8f.png)

🏷 Tagueamento. Em cada uma das tabelas são criadas duas novas colunas, uma de etiqueta e outra de classificação. A de etiqueta serve para especificar cada um dos posts e a de classificação para indicar em qual local da planilha oficial a postagem deve estar alocada.

![face-buffer-etiquetado](https://user-images.githubusercontent.com/89229665/149391720-54858db8-b007-4952-8f5f-a3f29a5903bc.png)

✅ Observações alinhadas. Não raro, algumas linhas das bases geradas pela Buffer aparecem desalinhas em relação às demais. Isso precisa ser corrigido para que, na etapa seguinte, o código possa rodar sem erros. 

![tabela-desalinhada](https://user-images.githubusercontent.com/89229665/149392298-6c890164-1b0b-4c12-b97c-6da7555b12c7.png)

Após esses procedimentos, os notebooks postados neste repositório entram em ação!

## O que você vai encontrar nesse repositório?

✌🏼 Dois notebooks comentados que explicam em detalhes os trechos de cada código e as escolhas tomadas. 

O primeiro notebook, chamado de *"Gera-planilha-matriz"*, faz a limpeza e a organização dos dados. Ele recebe como entrada 3 arquivos xlsx: um com postagens do Facebook, outro com postagens do Instagram e o terceiro com postagens do Twitter. Todos eles previamente etiquetados e classificados, como mencionado anteriormente. O resultado final do notebook *"Gera-planilha-matriz"* é uma planilha que junta as informações dos três arquivos e faz um recorte mantendo apenas as colunas que possuem as métricas de interesse da organização.

O segundo notebook, chamado de *Escreve-sub_planilhas*, cria planilhas menores a partir da planilha_matriz. Todas essas planilhas menores são escritas automaticamente, uma em baixo da outra, em uma das abas (worksheets) [desta planilha do Google spreadsheet](https://docs.google.com/spreadsheets/d/1jMikjV_8-L_9SvE4jn49ZxWAT5yTDD9p48oPvYk-AIM/edit#gid=37916203). Até o momento foram geradas planilhas com informações de agosto de 2021, setembro de 2021 e outubro de 2021. O filtro para criar cada sub-planilha são os itens da coluna "classificação". 

Gerados os dados de cada mês, espera-se que a pessoa responsável por realizar o relatório ofical de mídias sociais possa utilizá-los para extrair as informações necessárias de forma mais célere.

## 📚 Bibliotecas utilizadas

As principais bibliotecas utilizadas para desevolver esse projeto foram Pandas e GSpread. 

## Tchau, tchau!

Este projeto é o trabalho final desenvolvido para a 1ª formação do Master de Jornalismo de Dados, Automação e Data Storytelling do Insper. Fica aqui rgistrado, um agradecimento especial para Turicas, Pedro Burgos e Cuducos, pela paciência, pela paciência mais vez e pela ajuda no desenvolvimentos dos códigos. 


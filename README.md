# automacao-relatorios

Olá! 
Antes de qualquer explicação sobre do que se trata esse repositório, uma pergunta: você já teve que gastar horas e horas de trabalho preenchendo planilhas manualmente? 
Se sim, provavelmente isso aconteceu há muito tempo, não é? Afinal se você está no Github alguma carta na manga de programação você deve ter guardada aí.

Por aqui, na organização onde trabalho, planilhas são preenchidas na base do “copia e cola”, tomando tempo e gerando, literalmente, dores no braço.

Foi pensando em como otimizar essa tarefa que este repositório ganhou vida! 

Aqui você vai ver como automatizei a limpeza, a organização e a criação de planilhas. Agora em 10 minutos (sem exageros, eu cronometrei), o pessoal do meu trabalho poderá ter em mãos informações necessárias para a produção de relatórios de mídias sociais. 

“UHULL, adeus trabalho braçal!”. Na verdade, não.

Esse repositório contribui em uma única etapa de um processo mais amplo. A extração dos dados segue sendo feita de forma manual, assim como o tagueamento de cada uma das postagens (mais adiante, eu explico isso melhor). 

Outra fragilidade do projeto é que nem todas as mídias foram contempladas, ficaram de fora as postagens do Youtube e do site. A automação é realizada com dados extraídos da Buffer, uma plataforma que gerencia os perfis da organização no Facebook, no Instagram e no Twitter.

Em síntese, sabe aqueles 10 minutinhos que citei ali em cima? O resultado deles, na prática, é um compilado no Google spreadsheet das postagens mensais do Face, Insta e Twitter, organizado de acordo com parâmetros da entidade financiadora da organização. 

## O que você vai encontrar nesse repositório?

Dois notebooks comentados que explicam em detalhes os trechos do código.  Um notebook é o que gera a planilha matriz e o outro é o que escreve os dados no Gspread.
Um link para a tabela do Google spreadsheet que contém o compilados das postagens. Cada aba, corresponde a um mês. Até o momento foram geradas planilhas com informações de agosto de 2021, setembro de 2021 e outubro de 2021. 

## O que mais preciso saber?

Antes de subir as bases para o notebook, as etapas manuais são: 

EXTRAÇÃO DAS BASES DA BUFFER (foto). Para cada mídia (Facebook, Instagram, Twitter) há uma tabela.

TAGUEAMENTO MANUAL (foto). Em cada uma das tabelas são criadas duas novas colunas, uma de etiqueta e outra de classificação. A de etiqueta serve para especificar cada um dos posts e a de classificação para indicar em qual local da planilha da entidade financiadora a postagem deve estar alocada.

CHECAGEM COLUNAS (foto). Não raro, algumas linhas das bases geradas pela Buffer aparecem desalinhas em relação às demais. Isso precisa ser corrigido para que, na etapa seguinte, o código rode sem erros. 

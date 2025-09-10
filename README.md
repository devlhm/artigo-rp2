# Artigo RP2
Pesquisa para desenvolvimento de um artigo que utilize conhecimento da área de Sistemas de informação.

## Integrantes
Dimitri Prado,	Luis Henrique Moraes,	Pedro Oliveira Fernandes,	Rodrigo Lyusei Suguimoto.

## Tema Geral
Identificação de tecnologias emergentes a partir de dados de patentes usando ML

## Tema Específico
Identificação de tecnologias emergentes a partir de dados de patentes usando ML na área da construção civil

## Fonte de Dados
- [WIPO](https://patentscope.wipo.int/search/en/search.jsf)
- [LENS](https://www.lens.org/)

## Análise das Referências
Tabela da análise no [excel](https://docs.google.com/spreadsheets/d/1qfv87Qj_ramlhuBZ4EBIj8Dlr-TwvrjxG3Lpxr9LHRA/edit?usp=sharing)

## Algoritmos
- Random Forest/Árvore de Decisão
- SVM (Support Vector Machine)
- NLP (Natural Language Processing)

## Método
Esse estudo busca identificar padrões em tecnologias produzidas para serem aplicadas na área da construção civil. Isso será feito através de análises dados de patentes brasileiras utilizando algoritmos de aprendizagem de máquina. Para atingir este objetivo, a metodologia utilizada será dividida de acordo com as seguintes etapas:

1. Coleta e pré-processamento de dados
Através da ferramenta PATENTSCOPE da plataforma WIPO, realizamos a busca dos dados de patentes com base em uma query, utilizando diversas palavras chaves relacionadas ao campo da pesquisa nos campos de título e resumo, como ""construção civil"", ""engenharia civil"", ""obras de infraestrutura"" e frases similares. O uso de um filtro delimitará as patentes para apenas aquelas que foram registradas em órgãos brasileiros. Os resultados serão baixados em formato de planilha com os campos: autor, ano, país, título, resumo, entre outros. Esse arquivo será usado de forma que possam ser importados e processados em um ambiente de código.
A partir desses dados, será realizando o seu pré-processamento utilizando algumas colunas como nº de inventores, idade da patente, resumo, reinvindicações e título para calcular valores para diferentes variáveis de acordo com regras definidas para então possibilitar a classificação de tecnologias por emergência.

2. Processamento analítico e algoritmos:
As patentes no intervalo de tempo mais antigo serão usados para o treinamento do modelo. Elas são separados em 3 categorias: dados de teste, dados rotulados e dados não rotulados. Esses dados serão processados com o uso de dois métodos, aprendizado semi-supervisionado e aprendizado ativo. O objetivo é classificar os dados não rotulados por meio desse aprendizado usando o algoritmo de Random Forest e Support Vector Machine.
São criados então dois modelos de aprendizado de máquina com algoritmos de classificação diferentes, isso para fatores de comparação e evitar casos de enviesamento. Os resultados dos dois modelos são avaliados pela acurácia e F1-score, depois aplicados nas patentes mais recentes para finalmente determinar as tecnologias emergentes.

3. Análise dos resultados:
Com as patentes classificadas, é realizado um mapeamento do ecossistema, ou seja, determinar a relação entre os patentes classificados a partir dos termos chaves e montar uma rede de nós para verificar grupos de patentes formados. Essa rede será usada para identificar tecnologias emergentes e inovações futuras."	https://github.com/devlhm/artigo-rp2

## Descrição dos Dados
Dataset com 50.000 dados, cada linha corresponde a uma patente, sendo descrito com as seguintes colunas: Jurisdiction, Kind, Display Key, Lens ID, Publication Date, Publication Year, Application Number, Application Date, Priority Numbers, Earliest Priority Date, Title, Abstract, Applicants, Inventors, Owners, URL, Document Type, Has Full Text, Cites Patent Count, Cited by Patent Count, Simple Family Size, Simple Family Members, Simple Family Member Jurisdictions, Extended Family Size, Extended Family Members, Extended Family Member Jurisdictions, Sequence Count, CPC Classifications, IPCR Classifications, US Classifications, NPL Citation Count, NPL Resolved Citation Count, NPL Resolved Lens ID(s), NPL Resolved External ID(s), NPL Citations, Legal Status.

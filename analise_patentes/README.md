
# Como Rodar o Projeto `analise_patentes`

Este guia fornece instruções detalhadas para configurar e executar o projeto `analise_patentes` pela primeira vez.

---

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados em sua máquina:

1. **Python 3.11** (ou superior)
2. **Git**
3. **Git LFS** (Large File Storage)
4. **UV** (gerenciador de pacotes)

---

## Passo 1: Instalar o Git LFS

Se o Git LFS não estiver instalado, siga as instruções abaixo:

### Instalar o Git LFS

- **Windows**: Baixe o instalador do site oficial do Git LFS.
- **Linux/Mac**: Use o gerenciador de pacotes do sistema:

 ```bash
 sudo apt-get install git-lfs
 ```

### Inicializar o Git LFS

Após a instalação, inicialize o Git LFS na sua máquina:

```bash
git lfs install
```

---

## Passo 2: Clonar o Repositório

Clone o repositório do projeto para sua máquina local:

```bash
git clone <URL_DO_REPOSITORIO>
cd analise_patentes
```

### Baixar os Arquivos LFS

Baixe os arquivos grandes rastreados pelo Git LFS, se já não estiverem baixados:

```bash
git lfs pull
```

---

## Passo 3: Configurar o Ambiente Python

### Instalar o UV

Caso o UV não esteja instalado, você pode instalá-lo utilizando o pip:

```bash
pip install uv
```

### Instalar as Dependências

Instale as dependências listadas no arquivo `pyproject.toml` utilizando o UV. O UV criará automaticamente um ambiente virtual Python para isolar as dependências do projeto:

```bash
uv sync
```

---

## Passo 4: Executar os Notebooks

Os notebooks principais do projeto estão localizados na pasta raiz. Para executá-los:

1. Certifique-se de que o ambiente virtual está ativado.
2. Abra e execute os notebooks na seguinte ordem recomendada:

- `analise.ipynb`
- `limpeza-textos.ipynb`
- `lda.ipynb`

---

## Estrutura do Projeto

- `datasets/`: Contém os arquivos de dados utilizados no projeto.
- `graficos/`: Contém os gráficos gerados pelos notebooks.
- `modelos/`: Contém os modelos treinados.
- `README.md`: Este arquivo com as instruções do projeto.

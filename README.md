# Raspagem de dados com Python + Excel 🚀

Este script Python realiza a raspagem de dados de empresas a partir de um site específico, extrai informações importantes e salva esses dados em um arquivo Excel. As informações extraídas incluem o nome da empresa, CNPJ, telefone, ramo de atuação e status.

# Funcionalidades
- Raspagem de dados de empresas a partir de um site fornecido.
- Extração de informações: nome da empresa, CNPJ, telefone, ramo de atuação.
- Inclusão de uma coluna de status com um valor padrão ("Ativo").
- Exportação dos dados para um arquivo Excel (dados_empresas.xlsx).
- Substituição automática do arquivo Excel se ele já existir.

# Pré-requisitos
Antes de executar o script, certifique-se de ter as seguintes bibliotecas Python instaladas:

`requests`
`re`
`pandas`
`openpyxl`

`pip install requests pandas openpyxl`

# Como Usar
Clone o repositório ou baixe o arquivo do script:

```sh
git clone https://github.com/devLucasRS/webscraping_simples.git
cd webscraping_simples
```

Execute o script:

```sh
python script.py
```

# Verifique o arquivo Excel gerado:
O script gerará um arquivo chamado dados_empresas.xlsx no mesmo diretório. 
Se um arquivo com esse nome já existir, ele será substituído.

# Observações
O script utiliza uma expressão regular para extrair os dados de cada linha do texto.
A coluna "STATUS" é preenchida com o valor padrão "Ativo". Se você precisar de valores específicos para o status, ajuste o script conforme necessário.<br>
Link de raspagem utilizado: https://pastebin.com/raw/xjCDscZk

# Contribuição
Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

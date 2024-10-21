
# agent_sql
 Agente usando langchain para sql do curso da IA MASTER


Este projeto é um **Assistente Sql Inteligente** baseado em **LangChain**, integrando agentes de IA e uma base de dados para consultas com **OpenAI** para modelagem de linguagem natural, oferecendo suporte a perguntas e cálculos financeiros em tempo real. O objetivo é criar um assistente que responda dúvidas sobre a base da dados com o Tema IPCA, executando consultas sql para responder as dúvidas
## Funcionalidades

- **Consultas na base de dados**: Faz consultas direto no banco de dados.
- **Suporte a Linguagem Natural**: Usa o OpenAI para interpretar perguntas em linguagem natural e devolver respostas adequadas.

## Tecnologias Utilizadas

- **LangChain**: Framework para desenvolver aplicativos que utilizam modelos de linguagem.
- **OpenAI API**: Utilizado para interpretar as consultas em linguagem natural e gerar respostas.
- **SQLDatabase**: Sql para conecta a base de dados, servindo ao agente

## Pré-requisitos

Para rodar este projeto localmente, você precisará ter:

- Python 3.8+ instalado
- API key do OpenAI
- Dependências do projeto listadas no `pyproject.toml`

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/mielesantos/assistente-financeiro.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd assistente-financeiro
   ```

3. Instale as dependências:
   ```bash
   poetry install 
   ```

4. Configure suas chaves de API no arquivo `.env` ou diretamente no código:
   ```
   OPENAI_API_KEY=<sua_openai_api_key>
   ```

## Uso

### Execução do Assistente

Após configurar as chaves de API, você pode rodar o assistente da seguinte forma:

```bash
python app.py
```

Isso iniciará uma interface onde você pode fazer perguntas financeiras, como:

- 'qual mes e ano tiveram o maior IPCA?'

### Exemplo de Fluxo

1. O usuário faz uma pergunta em linguagem natural.
2. O LangChain distribui a tarefa para o agente apropriado que vai conectar ao banco de dados e fazer as consultas necessarias
4. A resposta é processada e devolvida ao usuário.


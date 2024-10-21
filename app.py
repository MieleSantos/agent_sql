import os

from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_openai import ChatOpenAI


class SqlAssistent:
    def __init__(self):
        load_dotenv()
        self._setup_environment_variables()
        self.model = ChatOpenAI(model='gpt-4')
        self.prompt_template = self._create_prompt_template()
        self.db = self._connet_database()
        self.toolkit = self._toolkit()
        self.system_message = self._system_message()
        self.agent_executor = self._create_agent_executor()

    def _setup_environment_variables(self):  # noqa: PLR6301
        api_key = os.getenv('API_KEY')
        if not api_key:
            raise ValueError(
                "A chave da API 'API_KEY' não foi encontrada nas variáveis de ambiente."
            )
        os.environ['OPENAI_API_KEY'] = api_key

    def _create_prompt_template(self):  # noqa: PLR6301
        prompt_text = """Use as ferramentas necessárias para responder perguntas
        relacionadas ao histórico de IPCA ao longo do tempo
        Responda tudo em português brasileiro
        Perguntas: {q}
        """
        return PromptTemplate.from_template(prompt_text)

    def _connet_database(self):  # noqa: PLR6301
        return SQLDatabase.from_uri('sqlite:///ipca.db')

    def _toolkit(self):
        return SQLDatabaseToolkit(db=self.db, llm=self.model)

    def _system_message(self):  # noqa: PLR6301
        return hub.pull('hwchase17/react')

    def _create_agent_executor(self):
        agent = create_react_agent(
            llm=self.model, tools=self.toolkit.get_tools(), prompt=self.system_message
        )
        return AgentExecutor(agent=agent, tools=self.toolkit.get_tools(), verbose=True)

    def search_assistent(self, question: str) -> str:  # noqa: PLR6301
        if not question:
            raise ValueError('A pergunta não pode ser vazia')

        input_question = self.prompt_template.format(q=question)
        response = self.agent_executor.invoke({'input': input_question})

        return response  # .get('output')


def seach_agent(question):
    assistent = SqlAssistent()
    return assistent.search_assistent(question)


if __name__ == '__main__':
    # question = input('Informe sua pergunta:')
    question = 'qual mes e ano tiveram o maior IPCA?'
    print(seach_agent(question))

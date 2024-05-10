from langchain_openai import ChatOpenAI
from langchain_core.messages.ai import AIMessage
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain

from llm.credentials import OPENAI_API_KEY
from llm import prompts



class TexasJack:

    def __init__(self):
        self.llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            openai_api_key=OPENAI_API_KEY,
            temperature=0.8
        )
        self.memory = ConversationBufferMemory(
            ai_prefix='Texas Jack',
            memory_key='history',
            return_messages=True
        )
    
    def output_parser(self, output):
        if type(output) == dict:
            return output['response']
        elif type(output) == AIMessage:
            return output.content

    def flush_memory(self):
        self.memory.clear()
        response = self.llm.invoke(prompts.RESET_MEMORY)

        return self.output_parser(response)

    def chat(self, question):
        prompt = PromptTemplate(
            template=prompts.CHAT,
            input_variables=['history', 'input']
            )
        chain = ConversationChain(
            llm=self.llm,
            prompt=prompt,
            memory=self.memory
        )
        response = chain.invoke(input=question)

        return self.output_parser(response)
    
    def warn_vulgar(self, input):
        prompt = PromptTemplate.from_template(prompts.WARN_VULGAR)
        chain = prompt | self.llm
        response = chain.invoke({"input": input})

        return self.output_parser(response)
    
    def get_memory(self):

        memory_parsed = ''

        for message in self.memory.dict()['chat_memory']['messages']:
            sender = 'Texas Jack' if message['type'] == 'ai' else 'Human'
            memory_parsed += f"{sender}: {message['content']}\n"

        return memory_parsed

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

#print(llm.invoke("how can langsmith help with testing?"))

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

chain = prompt | llm 

x = chain.invoke({"input": "how can langsmith help with testing?"})

from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

y = chain.invoke({"input": "how can langsmith help with testing?"})

print(y)

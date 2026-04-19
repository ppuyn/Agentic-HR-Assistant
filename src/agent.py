import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain import hub
from tools import check_vacation_balance

# Load API Key from .env file
load_dotenv()

def run_hr_agent(user_query):
    # 1. Setup the LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # 2. Define the tools available to the agent
    tools = [check_vacation_balance]

    # 3. Get a pre-made prompt template for agents
    prompt = hub.pull("hwchase17/openai-functions-agent")

    # 4. Construct the Agent
    agent = create_openai_functions_agent(llm, tools, prompt)

    # 5. Create the Executor (the runtime)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # 6. Run the query
    response = agent_executor.invoke({"input": user_query})
    return response["output"]

# Example test
print(run_hr_agent("How many vacation days does Uyen have left?"))

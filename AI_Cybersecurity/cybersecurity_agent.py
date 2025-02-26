from langchain.chat_models import ChatOpenAI
from langgraph.graph import StateGraph, END
from langchain.schema import SystemMessage, AIMessage, HumanMessage
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

# Initialize Chat Model
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)

# Define Workflow State
class AgentState:
    def __init__(self, messages):
        self.messages = messages

# Define Processing Function
def cybersecurity_agent(state):
    messages = state.messages
    response = llm.invoke(messages)
    return AgentState(messages + [AIMessage(content=response.content)])

# Define Graph
workflow = StateGraph(AgentState)
workflow.add_node("cyber_agent", cybersecurity_agent)
workflow.set_entry_point("cyber_agent")
workflow.add_edge("cyber_agent", END)
app = workflow.compile()

# Run the agent
if __name__ == "__main__":
    user_input = input("Enter a cybersecurity query: ")
    result = app.invoke(AgentState([HumanMessage(content=user_input)]))
    print("\nCybersecurity Agent Response:", result.messages[-1].content)

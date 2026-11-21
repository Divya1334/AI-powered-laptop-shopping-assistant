import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL")

if not GOOGLE_API_KEY:
    raise ValueError("Gemini API key not found!")

print("Gemini configuration loaded successfully!")
print("Model:", MODEL_NAME)



from langchain_core.tools import tool
from backend.tools import (
    search_laptops,
    compare_laptops,
    recommend_laptops
)

@tool
def laptop_search(
    max_price: float = None,
    min_ram: int = None,
    min_storage: int = None,
    brand: str = None
) -> str:
    """Search laptops by budget, RAM, storage and brand."""

    result = search_laptops(
        max_price=max_price,
        min_ram=min_ram,
        min_storage=min_storage,
        brand=brand
    )

    if result.empty:
        return "No matching laptops found."

    return result.head(10).to_string(index=False)

@tool
def laptop_comparison(brand1: str, brand2: str) -> str:
    """Compare laptops from two different brands."""

    result = compare_laptops(brand1, brand2)

    if result.empty:
        return "No matching laptops found."

    return result.to_string(index=False)

@tool
def laptop_recommendation(
    max_price: float = None,
    min_ram: int = None,
    min_storage: int = None,
    top_n: int = 3
) -> str:
    """Recommend top-rated laptops based on customer requirements."""

    result = recommend_laptops(
        max_price=max_price,
        min_ram=min_ram,
        min_storage=min_storage,
        top_n=top_n
    )

    if result.empty:
        return "No matching laptops found."

    return result.to_string(index=False)

tools = [
    laptop_search,
    laptop_comparison,
    laptop_recommendation
]

print("Available tools:")

for t in tools:
    print(t.name)
    
    
    
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import SystemMessage

llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=GOOGLE_API_KEY,
    temperature=0
)

llm_with_tools = llm.bind_tools(tools)


SYSTEM_PROMPT = """
You are an AI Laptop Shopping Assistant.

Your job is to help customers find suitable laptops
from the provided laptop dataset.

STRICT RULES:

1. Always use the available tools to search the dataset.
2. Never invent laptop names, prices, ratings or specifications.
3. If the customer specifies a budget, every recommended
   laptop MUST be within that budget.
4. Respect RAM, storage and brand requirements.
5. Recommend only products returned by the tools.
6. If no laptops match, clearly say no matching products
   were found.
7. Explain why each laptop is suitable.
8. Use simple and friendly language.

IMPORTANT:
Never ignore or change the customer's budget.
Never use external or imaginary product information.
"""


def assistant(state: MessagesState):
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *state["messages"]
    ]

    response = llm_with_tools.invoke(messages)

    return {"messages": [response]}

builder = StateGraph(MessagesState)

builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")

graph = builder.compile()


from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

graph = builder.compile(checkpointer=memory)



def chat_with_agent(user_input, thread_id="customer_1"):

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    result = graph.invoke(
        {
            "messages": [
                ("user", user_input)
            ]
        },
        config=config
    )

    last_message = result["messages"][-1]
    content = last_message.content

    # Handle Gemini's list-based response
    if isinstance(content, list):
        text_parts = []

        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                text_parts.append(block.get("text", ""))

        return "\n".join(text_parts)

    return str(content)

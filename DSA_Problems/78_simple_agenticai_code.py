from openai import OpenAI
import datetime
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ----------------------------
# TOOLS
# ----------------------------

def get_current_time():
    return str(datetime.datetime.now())

def calculator(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

# Available tools
tools = {
    "get_current_time": get_current_time,
    "calculator": calculator
}

# ----------------------------
# AGENT
# ----------------------------

def agent(user_query):

    system_prompt = f"""
    You are an AI Agent.

    You have access to these tools:

    1. get_current_time()
       -> returns current date and time

    2. calculator(expression)
       -> solves mathematical expressions

    If calculation is needed:
    respond ONLY like this:
    TOOL: calculator: 25 * 4

    If current time is needed:
    respond ONLY like this:
    TOOL: get_current_time

    Otherwise give normal response.
    """

    # Step 1 → Agent thinking
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
    )

    reply = response.choices[0].message.content

    print("\nAgent Thinking:", reply)

    # Step 2 → Tool execution
    if reply.startswith("TOOL:"):

        tool_data = reply.replace("TOOL:", "").strip()

        # calculator tool
        if tool_data.startswith("calculator"):
            expression = tool_data.split(":", 1)[1].strip()
            result = calculator(expression)

        # time tool
        elif tool_data.startswith("get_current_time"):
            result = get_current_time()

        else:
            result = "Unknown tool"

        print("\nTool Result:", result)

        # Step 3 → Final answer generation
        final_response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Generate final user-friendly answer."},
                {"role": "user", "content": f"""
                User Question: {user_query}

                Tool Result: {result}
                """}
            ]
        )

        return final_response.choices[0].message.content

    return reply


# ----------------------------
# RUN
# ----------------------------

question = input("Ask something: ")

answer = agent(question)

print("\nFinal Answer:")
print(answer)
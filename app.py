import streamlit as st

from swarm import app


st.set_page_config(page_title="Marketing Planner Agent", layout="wide")

st.title("Marketing Planning Assistant")


def _extract_readable_text(content) -> str:
    if isinstance(content, str):
        return content.strip()

    if isinstance(content, dict):
        text = content.get("text")
        return text.strip() if isinstance(text, str) else ""

    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                text = item.get("text", "")
                if isinstance(text, str) and text.strip():
                    parts.append(text.strip())
            elif isinstance(item, str) and item.strip():
                parts.append(item.strip())
        return "\n\n".join(parts)

    return ""


def _get_final_assistant_text(messages) -> str:
    for msg in reversed(messages):
        text = _extract_readable_text(getattr(msg, "content", ""))
        if text:
            return text
    return ""


goal = st.text_input(
    "Enter Marketing Goal",
    placeholder="e.g. Competitor Ads",
)

if st.button("Generate Plan") and goal:
    result = app.invoke(
        {"messages": [{"role": "user", "content": goal}]},
        {"configurable": {"thread_id": "planner"}},
    )

    st.subheader("Marketing Execution Plan")
    final_text = _get_final_assistant_text(result.get("messages", []))
    st.markdown(final_text if final_text else "No final response generated.")

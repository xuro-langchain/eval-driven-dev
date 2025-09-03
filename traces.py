from agent import email_assistant
from datasets import email_inputs, email_names
from dotenv import load_dotenv

load_dotenv(".env")

def create_traces(num_examples: int = 16):
    """Invoke the email assistant on a subset of dataset examples to create traces.

    Args:
        num_examples: Number of examples to run from the dataset in order.
    """
    
    for idx, (email_input, name) in enumerate(zip(email_inputs, email_names)):
        if idx >= num_examples:
            break

        print(f"\n--- Running example {idx + 1}: {name} ---")
        result = email_assistant.invoke(
            {"email_input": email_input},
            config={
                "run_name": f"email_assistant:{name}",
                "tags": ["email-assistant", "trace", name],
                "metadata": {"dataset": "email_inputs", "example_name": name, "example_index": idx},
            },
        )

        decision = result.get("classification_decision", "unknown")
        print(f"classification_decision: {decision}")

        messages = result.get("messages", [])
        if messages:
            last = messages[-1]
            content = last.get("content") if isinstance(last, dict) else getattr(last, "content", None)
            if content:
                preview = content if isinstance(content, str) else str(content)
                preview = preview[:300] + ("..." if len(preview) > 300 else "")
                print(f"last_message_preview: {preview}")


if __name__ == "__main__":
    create_traces()
# 6. Advanced Prompt Engineering

def create_stepwise_prompt(context):
    # Step 1: Instruction to summarize the initial context
    step1_prompt = f"Summarize this text: {context}"

    # Generate an AI summary (this is hypothetical code for an API)
    # In a real application, you would call the AI model here with step1_prompt
    ai_summary = "This is a summary of the context."  # Placeholder for the AI model's output

    # Step 2: Instruction to analyze or process the AI's *previous output* (the summary)
    step2_prompt = f"Based on the summary: '{ai_summary}', answer the following question..."

    return step1_prompt, step2_prompt


# Define the initial context/input
context = "Artificial intelligence has become a pivotal technology in the modern world, impacting everything from business operations to daily life."

# Generate the two prompts
step1, step2 = create_stepwise_prompt(context)

# Print the generated prompts
print("Step 1 Prompt:", step1)
print("Step 2 Prompt:", step2)
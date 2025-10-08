# 3. Creating Prompts with Nested Loops

# Setup the lists of variables (required for the code in the image to run)
topics = ["a dragon", "deep space", "a historical king"]
tones = ["serious", "humorous", "adventurous"]

# Create a list of prompts based on combinations of topics and tones
prompts = []
for topic in topics:
    for tone in tones:
        prompt = f"Write a {tone} story about {topic}."
        prompts.append(prompt)

# Print all generated prompts
for prompt in prompts:
    print(prompt)
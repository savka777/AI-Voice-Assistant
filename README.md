# AI_Voice_Assistant

This voice-activated assistant application integrates with OpenAI's GPT-3.5 model for natural language processing and response generation. Its features and functionalities are as follows:

**Speech Recognition Integration:**

Utilizes the speech_recognition library to convert spoken words into text. This allows the program to process spoken commands from the user.

**Text-to-Speech Functionality:**

Converts text responses into speech using Eleven Labs, allowing the assistant to communicate audibly with the user.
Temporary audio files are created for each response and then deleted after being played, ensuring efficient memory usage and data privacy.

**Integration with OpenAI's GPT-3.5:**

Uses OpenAI's API (GPT-3.5 model) to generate responses to user queries. The API key is set up at the start of the program.
Processes user input by sending it to the GPT model, which generates a natural language response.

**Customizable Agent Role:**

Defines a default role for the GPT agent as a general-purpose assistant.
Includes functionality (set_agent_role) allowing the user to customize the role of the GPT agent. This role information is used to tailor the responses of the GPT model.

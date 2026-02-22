---
**Student**: Nicole Dayan Calderon Arevalo

**Institution**: Escuela Colombiana de Ingenieria Julio Garavito

**Course**: Digital Transformations For Enterprise Solutions

---

# LangChain LLM Chain Lab

Hey! This is a simple Python project that shows you how to build a basic AI chain using LangChain and OpenAI. It's basically a tool that takes a concept, asks ChatGPT to explain it in simple terms, and gives you the answer. Perfect for learning how LangChain works!

---

## What's This About?

### So... What's LangChain?

LangChain is basically a toolkit that makes it way easier to work with AI language models like ChatGPT. Instead of writing complicated code to talk to the API, LangChain gives you simple building blocks so you can just plug them together. Think of it like LEGO for AI!

### Okay, But What's an LLM Chain?

A chain is just a series of steps that work together. Here's how it goes:

1. You give it some input (like a concept you want explained)
2. It cleans that up and prepares it nicely
3. It sends it to the AI model
4. The AI gives you back an answer

Pretty simple, right? You can make the chain longer by adding more steps, but this one keeps it nice and clean.

### What Does This Project Actually Do?

This project is like a mini-app that:

- Asks you for a concept (something like "machine learning")
- Takes your input and formats it into a proper prompt
- Sends it to OpenAI's AI model
- Gets back an explanation that's easy to understand

Nothing fancy, but it teaches you all the basics you need to know!

---

## How It Works (The Flow)

The app works in a really simple way:

```
You type something
    ↓
We format it nicely
    ↓
Send it to ChatGPT
    ↓
Get back an answer
```

### Breaking It Down

**Your Input**: Whatever you want explained (you type it in)

**The Template**: We take your words and put them into a template that looks like this:

```
"Explain the following concept in simple terms: [your concept here]"
```

**The AI Model**: We use OpenAI's GPT-4o-mini. It's:

- Super fast
- Pretty cheap
- Smart enough for this job

**The Connection**: We connect everything using the pipe operator `|` (it's like a chain):

```python
chain = prompt | llm
```

It's like saying: take the template, put the user's words in it, send it to ChatGPT, and give me the result. All in one line!

---

## Project Structure

```
langchain-llm-chain-lab/
│
├── app/
│   ├── __init__.py          (Package initialization with documentation)
│   ├── llm_chain.py         (Chain configuration and initialization)
│   └── main.py              (Application entry point and user interaction)
│
├── .env.example             (Template for environment variables)
├── .gitignore              (Git ignore rules)
├── requirements.txt        (Python dependencies)
└── README.md               (This file)
```

---

## Getting Started

### What You Need First

- Python 3.8+ (or newer)
- pip (it comes with Python)
- An OpenAI API key (free to create, but you pay for what you use)

### Installation Steps

Pretty straightforward:

1. **Open the folder**:

   ```bash
   cd langchain-llm-chain-lab
   ```

2. **Create a virtual environment** (this keeps everything organized):

   ```bash
   # If you're on Windows
   python -m venv venv
   venv\Scripts\activate

   # If you're on Mac or Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install all the stuff you need**:
   ```bash
   pip install -r requirements.txt
   ```

Done! Now move to the next part.

---

## Setting Up Your API Key

This is the important part! OpenAI needs a key to verify it's you:

1. **Make a copy of the example file**:

   ```bash
   cp .env.example .env
   ```

2. **Open the `.env` file** and add your OpenAI key:

   ```
   OPENAI_API_KEY=sk-your-actual-key-goes-here
   ```

3. **That's it!** The file is already in `.gitignore`, so it won't accidentally get uploaded to the internet.

### Important Security Stuff

- **Never ever** share your API key with anyone
- **Never ever** put your real key in the `.env.example` file
- **Never** push your `.env` file to GitHub (we already set that up for you)
- Your key is like a password - keep it secret!

If you mess up and accidentally share your key, just delete it from OpenAI's website and create a new one.

---

## Time to Run It!

### Running the App

Just type this in your terminal:

```bash
python app/main.py
```

### Here's What It Looks Like

```
============================================================
LangChain LLM Chain Lab - Concept Explainer
============================================================

Enter a concept you'd like me to explain: machine learning

Generating explanation...

------------------------------------------------------------
Explanation:
------------------------------------------------------------
Machine learning is a type of artificial intelligence that allows
computers to learn from data without being explicitly programmed.
Instead of following pre-written instructions, machine learning
systems analyze patterns in data and improve their performance over
time through experience. For example, email spam filters use machine
learning to identify spam messages by learning from examples of spam
and legitimate emails.
------------------------------------------------------------
```

### Try These Concepts

- `artificial intelligence`
- `neural networks`
- `natural language processing`
- `blockchain`
- `quantum computing`

Just type anything you want explained!

---

## What We're Using

| What              | Why                                                |
| ----------------- | -------------------------------------------------- |
| **Python 3.8+**   | The programming language - solid and easy to learn |
| **LangChain**     | The magic that makes working with AI super easy    |
| **OpenAI API**    | The actual AI brains - it's what does the thinking |
| **python-dotenv** | Keeps your secret API key... well, secret          |
| **tiktoken**      | Counts tokens (basically words) for you            |

---

## The Cool Stuff Explained

### The Pipe Operator (That `|` Thing)

In this project, we use the pipe operator to chain things together. It's like building with blocks:

```python
chain = prompt | llm
```

This means: "Take the prompt, pipe it into the LLM, and give me the result." Super clean and easy to understand. You can keep adding more things to the chain if you want to make it bigger.

### The Prompt Template

This is basically the question we're asking ChatGPT:

```python
ChatPromptTemplate.from_template(
    "Explain the following concept in simple terms: {concept}"
)
```

The `{concept}` part is where YOUR input goes. When you type "machine learning", it becomes:

```
"Explain the following concept in simple terms: machine learning"
```

### Temperature (The AI's Mood)

The temperature setting controls how "creative" or "random" the AI gets:

- **0.0** = Boring but accurate (always the same answer)
- **0.7** = Our choice! A good balance - creative but reasonable
- **1.0+** = Super creative and unpredictable

We set it to 0.7 because it's the sweet spot.

---

## Code Examples

### Example 1: How the Chain Gets Created

This is what happens inside `llm_chain.py`:

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Create the prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain the following concept in simple terms: {concept}"
)

# Create the LLM model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Connect them with the pipe operator
chain = prompt | llm
```

That's it! Three simple steps and you have a working chain.

### Example 2: How to Use the Chain

Once the chain is created, using it is super easy:

```python
# Create the chain
chain = create_chain()

# Use it with any concept
response = chain.invoke({"concept": "artificial intelligence"})

# Print the result
print(response.content)
```

The `invoke()` method takes a dictionary with your input and returns the model's response.

### Example 3: Full Example from `main.py`

Here's how the main app uses everything:

```python
from app.llm_chain import create_chain

# Get the chain ready
chain = create_chain()

# Ask the user for input
concept = input("Enter a concept you'd like me to explain: ").strip()

# Send it through the chain
response = chain.invoke({"concept": concept})

# Print the answer nicely
print("Explanation:")
print(response.content)
```

### Example 4: Different Concepts You Can Try

```python
# You can use any of these as input:

concepts = [
    "quantum computing",
    "blockchain technology",
    "neural networks",
    "climate change",
    "cryptocurrency",
    "photosynthesis",
    "machine learning",
    "the internet"
]

# Just replace {concept} with any of these and it works!
```

### Example 5: What The Output Looks Like

When you run the chain with "neural networks", here's what you might get:

```
Chain Input:
{
  "concept": "neural networks"
}

Template After Formatting:
"Explain the following concept in simple terms: neural networks"

AI Response:
"Neural networks are computer systems inspired by how our brains work.
They're made up of connected nodes that pass information to each other,
learning patterns from data. Kind of like how your brain learns by
connecting neurons. They're used in things like image recognition,
language translation, and chatbots like ChatGPT."
```

---

## Inside the Code

### What Each File Does

**`app/llm_chain.py`**: This is the heart of the project

- Loads your API key from the `.env` file
- Creates and sets up the ChatOpenAI model
- Makes the prompt template
- Connects them all together with the pipe operator
- Returns the ready-to-use chain

**`app/main.py`**: This is where the user interacts with the app

- Asks you to type a concept
- Takes what you typed and feeds it into the chain
- Catches any errors and tells you what went wrong
- Prints out the answer nicely

**`requirements.txt`**: The ingredient list

- Lists everything Python needs to run this project
- With exact versions so it works the same everywhere

---

## Things to Know Before You Start

- **You have to pay for OpenAI**: It's not free, but it's super cheap for this project
- **Rate limits**: OpenAI limits how many requests you can make per minute
- **The app needs the internet**: Obviously, it needs to talk to OpenAI's servers
- **This is just the basics**: We're keeping it simple on purpose - this is for learning!

---

## License

This whole thing was made for learning. Use it however you want!

---

## Something's Broken? Here's Help

### Problem: "OPENAI_API_KEY not found"

**Solution**: Check that your `.env` file has the right key in it. Make sure you copied `.env.example` correctly.

### Problem: "Module not found" errors

**Solution**: Did you do `pip install -r requirements.txt`? Do it now if you didn't.

### Problem: Virtual environment is being weird

**Solution**: Delete the whole `venv` folder and create it again:

```bash
rm -r venv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Problem: Too many requests / rate limit

**Solution**: Just wait a minute or two. OpenAI's API won't let you spam requests.

---

## Want to Learn More?

- [LangChain docs](https://python.langchain.com/) - The official stuff
- [OpenAI docs](https://platform.openai.com/docs/) - Everything about the API
- [Python guide](https://pep8.org/) - How to write clean Python

---

**Made**: February 2026  
**Status**: Works great and ready to use!  
**Version**: 1.0.0

Have fun learning!

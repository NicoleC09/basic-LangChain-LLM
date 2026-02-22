"""
LLM Chain Module

This module contains the configuration and initialization of the LangChain LLM chain.
It uses OpenAI's ChatOpenAI model with LangChain's LCEL pipe operator.
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


def create_chain():
    """
    Creates and returns a LangChain LLM chain using LCEL pipe operator.
    
    The chain consists of:
    - ChatPromptTemplate: Formats user input into a prompt
    - ChatOpenAI: LLM model from OpenAI
    
    Environment Variables:
        OPENAI_API_KEY: OpenAI API key (loaded from .env file)
    
    Returns:
        chain: A LangChain chain object that can be invoked with user input
        
    Raises:
        ValueError: If OPENAI_API_KEY is not found in environment
        
    Example:
        >>> chain = create_chain()
        >>> response = chain.invoke({"concept": "machine learning"})
        >>> print(response.content)
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Verify API key is available
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY not found. Please set it in your .env file. "
            "See .env.example for reference."
        )
    
    # Initialize the ChatOpenAI model
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        api_key=api_key
    )
    
    # Create the prompt template
    prompt = ChatPromptTemplate.from_template(
        "Explain the following concept in simple terms: {concept}"
    )
    
    # Build the chain using LCEL pipe operator
    chain = prompt | llm
    
    return chain

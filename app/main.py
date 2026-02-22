"""
Main Entry Point

This module serves as the entry point for the LangChain LLM Chain Lab application.
It handles user input and invokes the LLM chain to generate responses.
"""

from app.llm_chain import create_chain


def main():
    """
    Main function that runs the LangChain LLM chain application.
    
    This function:
    1. Initializes the LLM chain
    2. Prompts the user for a concept
    3. Invokes the chain with the user input
    4. Prints the LLM response
    
    Includes basic error handling for API and configuration issues.
    """
    try:
        # Initialize the chain
        print("\n" + "=" * 60)
        print("LangChain LLM Chain Lab - Concept Explainer")
        print("=" * 60 + "\n")
        
        chain = create_chain()
        
        # Get user input
        concept = input("Enter a concept you'd like me to explain: ").strip()
        
        if not concept:
            print("Error: Please enter a valid concept.")
            return
        
        # Invoke the chain
        print("\nGenerating explanation...\n")
        response = chain.invoke({"concept": concept})
        
        # Print the response
        print("-" * 60)
        print("Explanation:")
        print("-" * 60)
        print(response.content)
        print("-" * 60 + "\n")
        
    except ValueError as e:
        print(f"\nConfiguration Error: {e}\n")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}\n")


if __name__ == "__main__":
    main()

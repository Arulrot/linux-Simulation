import os
import time
import random

# Import the lists from your data file
try:
    import linux_data
except ImportError:
    print("Error: Could not find 'linux_data.py'. Please make sure both files are in the same folder.")
    exit()

def clear_screen():
    # Only used once at the very start
    os.system('cls' if os.name == 'nt' else 'clear')

def start_simulation():
    clear_screen()
    print("==========================================")
    print("      LINUX TERMINAL SIMULATION v1.0      ")
    print("==========================================")
    print("Type the correct command for the description.")
    print("Type 'quit' to exit the simulation.")
    print("------------------------------------------\n")
    
    # Zip the lists together so questions and answers stay paired
    qa_pairs = list(zip(linux_data.questions, linux_data.answers))
    
    # Shuffle them so the order is different every time
    random.shuffle(qa_pairs)
    
    score = 0
    total_questions = len(qa_pairs)

    for index, (question, correct_ans) in enumerate(qa_pairs):
        # Format the question to look like a system prompt or comment
        print(f"[Question {index + 1}/{total_questions}]: {question}")
        
        # Simulating a terminal prompt
        user_input = input("user@linux:~$ ").strip()

        if user_input.lower() == 'quit':
            break

        # Check answer
        if user_input == correct_ans:
            # Print a blank line to separate successful commands slightly
            print("") 
            score += 1
        else:
            # If wrong, show error but keep history visible
            print(f">> ERROR: Command failed.")
            print(f">> CORRECT COMMAND: {correct_ans}")
            
            # Pause so you can read the answer, but don't clear screen
            retry = input("\n[Press Enter to continue...]")
            if retry.lower() == 'q':
                break
            
            print("-" * 30) # A visual separator line

    # Final Score
    print("\n==========================================")
    print(f"SESSION COMPLETE. SCORE: {score}/{index + 1}")
    print("==========================================")
    input("Press Enter to close.")

if __name__ == "__main__":
    start_simulation()
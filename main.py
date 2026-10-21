from google import genai
import time


# ==========================================
# GEMINI CLIENT
# ==========================================

client = genai.Client()

MODEL = "gemini-3.8-flash"


# ==========================================
# CREATE CHAT
# ==========================================

chat = client.chats.create(
    model=MODEL
)


# ==========================================
# GEMINI RESPONSE FUNCTION
# ==========================================

def ask_gemini(prompt):

    max_attempts = 3

    for attempt in range(1, max_attempts + 1):

        try:

            print("\nThinking...")

            response = chat.send_message(prompt)

            return response.text

        except Exception as error:

            error_message = str(error)

            print("\nGemini Error:")
            print(error_message)

            # Handle temporary server error
            if "503" in error_message or "UNAVAILABLE" in error_message:

                if attempt < max_attempts:

                    wait_time = attempt * 3

                    print(
                        f"\nGemini is temporarily busy."
                    )

                    print(
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

                else:

                    return (
                        "Gemini is currently busy. "
                        "Please try again after some time."
                    )

            else:

                return "An error occurred while contacting Gemini."


# ==========================================
# STUDY FEATURES
# ==========================================

def explain_topic():

    topic = input("\nEnter topic: ")

    prompt = f"""
Explain the following topic in simple language.

Topic:
{topic}

Include:

1. Simple definition
2. Main concepts
3. Real-world example
4. Important points
5. Short summary

Explain it like you are teaching a beginner.
"""

    print("\n========== EXPLANATION ==========")

    print(ask_gemini(prompt))


def generate_notes():

    topic = input("\nEnter topic for notes: ")

    prompt = f"""
Create clear study notes about:

{topic}

Use:

- Headings
- Bullet points
- Important definitions
- Examples
- Key concepts
- Exam tips

Keep the notes easy to study.
"""

    print("\n========== STUDY NOTES ==========")

    print(ask_gemini(prompt))


def generate_quiz():

    topic = input("\nEnter topic for quiz: ")

    prompt = f"""
Create a quiz about:

{topic}

Generate 10 multiple-choice questions.

For each question provide:

Question
A
B
C
D
Correct Answer
Short Explanation

Make the questions suitable for a student.
"""

    print("\n========== QUIZ ==========")

    print(ask_gemini(prompt))


def generate_questions():

    topic = input("\nEnter subject/topic: ")

    prompt = f"""
Create important exam questions about:

{topic}

Generate:

5 short-answer questions
5 long-answer questions
5 important questions

Also explain which topics students should focus on.
"""

    print("\n========== IMPORTANT QUESTIONS ==========")

    print(ask_gemini(prompt))


def summarize_text():

    print("\nPaste the text you want to summarize.")

    text = input("\nText: ")

    prompt = f"""
Summarize the following text.

Give:

1. Short summary
2. Main points
3. Important keywords
4. Important facts

Text:

{text}
"""

    print("\n========== SUMMARY ==========")

    print(ask_gemini(prompt))


def explain_code():

    print("\nPaste your code.")

    code = input("\nCode: ")

    prompt = f"""
Explain this code in simple language.

Code:

{code}

Explain:

1. What the code does
2. How it works
3. Important lines
4. Possible errors
5. How to improve it
"""

    print("\n========== CODE EXPLANATION ==========")

    print(ask_gemini(prompt))


def solve_problem():

    problem = input("\nEnter your problem: ")

    prompt = f"""
Solve this problem step by step.

Problem:

{problem}

Show:

1. Given information
2. Formula or method
3. Step-by-step solution
4. Final answer
5. Simple explanation
"""

    print("\n========== SOLUTION ==========")

    print(ask_gemini(prompt))


# ==========================================
# CHAT MODE
# ==========================================

def chat_mode():

    print("\n========== AI CHAT ==========")

    print("Type 'exit' to return to the main menu.")

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":

            break

        answer = ask_gemini(question)

        print("\nGemini:")
        print(answer)


# ==========================================
# MAIN MENU
# ==========================================

def main():

    print("\n====================================")
    print("       AI STUDY ASSISTANT")
    print("====================================")

    while True:

        print("\nChoose an option:")

        print("1. 🤖 AI Chat")
        print("2. 📚 Explain Topic")
        print("3. 📝 Generate Study Notes")
        print("4. ❓ Generate Quiz")
        print("5. 📋 Important Questions")
        print("6. ✂️ Summarize Text")
        print("7. 💻 Explain Code")
        print("8. 🧮 Solve Problem")
        print("9. 🚪 Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            chat_mode()

        elif choice == "2":

            explain_topic()

        elif choice == "3":

            generate_notes()

        elif choice == "4":

            generate_quiz()

        elif choice == "5":

            generate_questions()

        elif choice == "6":

            summarize_text()

        elif choice == "7":

            explain_code()

        elif choice == "8":

            solve_problem()

        elif choice == "9":

            print("\nThank you for using AI Study Assistant!")

            break

        else:

            print("\nInvalid choice. Please select 1-9.")


# ==========================================
# START PROGRAM
# ==========================================

if __name__ == "__main__":

    main()
from generator import generate_component
from linter import validate


def guided_architect(prompt):

    print("\n Generating component...\n")
    code = generate_component(prompt)

    for attempt in range(2):   # at least one retry required

        errors = validate(code)

        if not errors:
            print(" Component validated successfully")
            return code

        print(f"Validation failed (Attempt {attempt+1})")
        print("Errors:", errors)
        print("🔁 Self-correcting...\n")

        code = generate_component(prompt, error_logs=errors)

    return code


if __name__ == "__main__":
    user_prompt = input("Enter component description: ")
    final_code = guided_architect(user_prompt)

    print("\n========== FINAL COMPONENT ==========\n")
    print(final_code)


print("\n🔍 Running Linter Check...\n")

errors = validate(final_code)

if not errors:
    print("Linter Passed — Component follows Design System & Syntax")
else:
    print("Linter Found Issues:")
    for e in errors:
        print("-", e)


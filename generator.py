import json
import random

# Try importing Gemini (LLM)
use_llm = True
try:
    from google import genai
    client = genai.Client(api_key="AIzaSyAri1DRO7DoqfiEYOYj0u7HYMI848mY1DM")
except:
    use_llm = False


with open("token.json") as f:
    tokens = json.load(f)


# ---------------- MOCK GENERATOR ----------------
def mock_generate(prompt):
    color = tokens["primaryColor"]
    radius = tokens["borderRadius"]
    font = tokens["fontFamily"]
    padding = tokens["padding"]
    button_radius = tokens["buttonRadius"]

    return f"""
<div class="flex items-center justify-center min-h-screen bg-gray-100"
     style="font-family:{font};">

  <div class="backdrop-blur-md bg-white/30 shadow-lg p-6"
       style="border-radius:{radius}; padding:{padding};">

    <h2 class="text-xl mb-4"
        style="color:{color};">Login</h2>

    <input type="email" placeholder="Email"
           class="border p-2 mb-3 w-full"
           style="border-radius:{radius}; padding:{padding};" />

    <input type="password" placeholder="Password"
           class="border p-2 mb-3 w-full"
           style="border-radius:{radius}; padding:{padding};" />

    <button class="text-white px-4 py-2"
            style="background:{color}; border-radius:{button_radius};">
      Submit
    </button>
  </div>
</div>
"""


# ---------------- REAL GENERATOR ----------------
def llm_generate(prompt, error_logs=None):

    system_prompt = f"""
You are an Angular component generator.

STRICT RULES:
- Output ONLY raw Angular HTML + Tailwind code
- No explanation
- Must use:

Primary Color: {tokens['primaryColor']}
Border Radius: {tokens['borderRadius']}
Font: {tokens['fontFamily']}
Padding: {tokens['padding']}
"""

    if error_logs:
        prompt = f"""
Fix using these errors:
{error_logs}

Original request:
{prompt}
"""

    full_prompt = system_prompt + "\nUser request: " + prompt

    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=full_prompt
    )

    code = response.text
    return code.replace("```html", "").replace("```", "").strip()


# ---------------- MAIN GENERATOR ----------------
def generate_component(prompt, error_logs=None):

    if use_llm:
        try:
            return llm_generate(prompt, error_logs)
        except Exception as e:
            print("⚠ LLM failed → Switching to Mock Mode")

    return mock_generate(prompt)


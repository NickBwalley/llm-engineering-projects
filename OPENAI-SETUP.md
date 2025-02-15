# Setting Up OpenAI API Key

## **1. Create an OpenAI Account**

To use OpenAI's API, you need an account:

- Visit [OpenAI's website](https://openai.com/)
- Sign up or log in to your account

---

## **2. Get Your API Key**

1. Once logged in, navigate to the [OpenAI API Keys page](https://platform.openai.com/account/api-keys)
2. Click on **"Create API Key"**
3. Copy the generated API key (it will not be shown again!)

---

## **3. Set Up API Key in Your Project**

### **Option 1: Using Environment Variables (Recommended)**

1. Open your terminal or command prompt.
2. Set the API key as an environment variable:

   - **Mac/Linux**:
     ```bash
     export OPENAI_API_KEY="your-api-key-here"
     ```
   - **Windows (Command Prompt)**:
     ```cmd
     set OPENAI_API_KEY="your-api-key-here"
     ```
   - **Windows (PowerShell)**:
     ```powershell
     $env:OPENAI_API_KEY="your-api-key-here"
     ```

3. You can now access the key in your scripts:
   ```python
   import os
   api_key = os.getenv("OPENAI_API_KEY")
   ```

---

### **Option 2: Using a `.env` File**

If you're working with a project, it's best to store the API key in a `.env` file.

1. Install the `python-dotenv` package if not already installed:
   ```bash
   pip install python-dotenv
   ```
2. Create a `.env` file in your project directory:
   ```bash
   touch .env
   ```
3. Add the following to `.env`:
   ```env
   OPENAI_API_KEY=your-api-key-here
   ```
4. Load the API key in your script:

   ```python
   from dotenv import load_dotenv
   import os

   load_dotenv()
   api_key = os.getenv("OPENAI_API_KEY")
   ```

---

## **4. Verify the API Key**

To check if your API key is working, run:

```python
import openai

openai.api_key = "your-api-key-here"

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Hello, OpenAI!",
    max_tokens=5
)
print(response)
```

If the response contains valid output, your API key is correctly set up!

---

## **5. Keep Your API Key Secure**

- **Never share** your API key publicly.
- **Avoid hardcoding** the key inside scripts.
- **Use `.gitignore`** to prevent `.env` files from being uploaded:
  ```
  echo ".env" >> .gitignore
  ```
- **Rotate the key if compromised** by generating a new one in OpenAI's API settings.

---

Now you're all set up to use OpenAI's API! 🚀

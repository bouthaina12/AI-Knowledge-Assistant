import sys
import importlib

modules = ["langchain", "langchain_google_genai", "langchain_openai", "langchain_chroma"]
print('Python:', sys.executable)
for m in modules:
    try:
        __import__(m)
        print(m, 'imported')
    except Exception as e:
        print(m, 'import error:', type(e).__name__, e)

# Try importing ChatGoogleGenAI and GoogleGenAIEmbeddings if available
try:
    from langchain_google_genai import ChatGoogleGenAI, GoogleGenAIEmbeddings
    print('Imported ChatGoogleGenAI and GoogleGenAIEmbeddings')
except Exception as e:
    print('Import langchain_google_genai error:', type(e).__name__, e)

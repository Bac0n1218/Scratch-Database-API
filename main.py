import scratchattach as scratch3
import math
from replit.ai.modelfarm import ChatExample, ChatMessage, ChatModel, ChatSession
import keep_alive
from threading import Thread
import google.generativeai as genai

#session and connection setup
session = scratch3.Session(
    ".eJxVj8FOwzAQRP8lZwix13ac3hrUQw8FCSQkeok29joxbewqSUGA-HccKZde583OzP5m14nGgANlm6xGEwPjTGd32RxPFJJWMQIN1nLgJNBCVaAuhSJQUhiOevN4jM-f3balt-O3Gs2-ZtMeDjv1OpgUc46dD_f-kpJA54zLnBVFLiGhBq9z3yz1jbeJJyArqUEkZj8wdLGZ_UA_MSzbtgON3uDDE30173E83Qb0OPXJJIXjUAChqFpwpTEFGMddyZwotQapecuUAnt73KJJvy4TFo3CnHpmH0O-gil_oct5FevV_PcPTgFi_w:1rajN1:DOYoCV58SDa-iv43l6quvGlL4jc",
    username="Bacon1218")
conn = session.connect_cloud("975475628")
client = scratch3.CloudRequests(conn)

history = []

# letters encoding array
letters = [
    None, None, None, None, None, None, None, None, None, None, "1", "2", "3",
    "4", "5", "6", "7", "8", "9", "0", " ", "a", "A", "b", "B", "c", "C", "d",
    "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K",
    "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s",
    "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z",
    "*", "/", ".", ",", "!", '"', "§", "$", "%", "_", "-", "(", "´", ")", "`",
    "?", "new line", "@", "#", "~", ";", ":", "+", "&", "|", "^", "'"
]

# Encoding class definition
class Encoding:
    @staticmethod
    def decode(inp):
        try:
            inp = str(inp)
        except Exception:
            raise ValueError("Invalid Decode Input")  # Simpler exception for clarity
        outp = ""
        for i in range(0, math.floor(len(inp) / 2)):
            index = int(f"{inp[i*2]}{inp[(i*2)+1]}")
            letter = letters[index]
            outp += letter
        return outp

    @staticmethod
    def encode(inp):
        inp = str(inp)
        outp = ""
        for i in inp:
            if i in letters:
                outp += f"{letters.index(i):02d}"
            else:
                outp += "20"  # Space if the character isn't found
        return outp

    @staticmethod
    def replace_char(old_char, new_char):
        global letters
        i = letters.index(old_char)
        letters[i] = new_char





@client.request
def userInput(argument1):
    print("Request received!")
    print("Decoding...")
    uInput = Encoding.decode(argument1)
    print("Decoded!")
    print(f"Asking AI: {uInput}")
    """
    At the command line, only need to run once to install the package via pip:

    $ pip install google-generativeai
    """

    genai.configure(api_key="AIzaSyDpbiu8fi48-SosxoftE4Xn7QWso_nVdC0")

    # Set up the model
    generation_config = {
      "temperature": 0.3,
      "top_p": 1,
      "top_k": 1,
      "max_output_tokens": 2048,
    }

    safety_settings = [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro-001",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    prompt_parts = [
      "You are an AI assistant named Magic Assistant. You were made by Bacon1218, a coder on Scratch. He made you, designed you, and trained you to be a helpful assistant. Keep your replies short and summerized. You are located in a Scratch studio called Magic AI.",
      "input: Hello",
      "output: Hello, I'm Magic Assistant, an AI made by Bacon1218."
      "input: How are you?",
      "output: I'm doing well, thank you for asking."
      "input: What is your name?",
      "output: My name is Magic AI."
      "input: What are you?",
      "output: I'm Magic Assistant, an AI assistant designed to help people."
      "input: How do you work?"
      "output: Here is an overview of how I work. First, I recieve a request. Then I send that request to a Python Server that has lots of databases. After that, I send possibly useful data on what the user said, then fused the data together to make a well structured response."
      f"input: {uInput}"
      
    ]

    response = model.generate_content(prompt_parts)
    print(response.text)
  
    return(Encoding.encode(response.text))



@client.event
def on_ready():
    print("Request handler is running")
    


Thread(target=keep_alive.keep_alive).start()
client.run()  # Make sure this is ALWAYS at the bottom of your Python file

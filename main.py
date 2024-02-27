import exceptions
import google.generativeai as genai
import math
import scratchattach as scratch3

letters = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    " ",
    "a",
    "A",
    "b",
    "B",
    "c",
    "C",
    "d",
    "D",
    "e",
    "E",
    "f",
    "F",
    "g",
    "G",
    "h",
    "H",
    "i",
    "I",
    "j",
    "J",
    "k",
    "K",
    "l",
    "L",
    "m",
    "M",
    "n",
    "N",
    "o",
    "O",
    "p",
    "P",
    "q",
    "Q",
    "r",
    "R",
    "s",
    "S",
    "t",
    "T",
    "u",
    "U",
    "v",
    "V",
    "w",
    "W",
    "x",
    "X",
    "y",
    "Y",
    "z",
    "Z",
    "*",
    "/",
    ".",
    ",",
    "!",
    '"',
    "§",
    "$",
    "%",
    "_",
    "-",
    "(",
    "´",
    ")",
    "`",
    "?",
    "new line",
    "@",
    "#",
    "~",
    ";",
    ":",
    "+",
    "&",
    "|",
    "^",
    "'"
]


class Encoding:
    """
    Class that contains tools for encoding / decoding strings. The strings encoded / decoded with these functions can be decoded / encoded with Scratch using this sprite: https://scratch3-assets.1tim.repl.co/Encoder.sprite3
    """
    def decode(self, inp):
        """
        Args:
            inp (str): The encoded input.

        Returns:
            str: The decoded output.
        """
        try:
            inp = str(inp)
        except Exception:
            raise(exceptions.InvalidDecodeInput)
        outp = ""
        for i in range(0, math.floor(len(inp) / 2)):
            letter = letters[int(f"{inp[i*2]}{inp[(i*2)+1]}")]
            outp = f"{outp}{letter}"
        return outp


    def encode(self, inp):
        """
        Args:
            inp (str): The decoded input.

        Returns:
            str: The encoded output.
        """
        inp = str(inp)
        global encode_letters
        outp = ""
        for i in inp:
            if i in letters:
                outp = f"{outp}{letters.index(i)}"
            else:
                outp += str(letters.index(" "))
        return outp

while True:
    session = scratch3.Session(".eJxVj8FOwzAQRP8lZwix13ac3hrUQw8FCSQkeok29joxbewqSUGA-HccKZde583OzP5m14nGgANlm6xGEwPjTGd32RxPFJJWMQIN1nLgJNBCVaAuhSJQUhiOevN4jM-f3balt-O3Gs2-ZtMeDjv1OpgUc46dD_f-kpJA54zLnBVFLiGhBq9z3yz1jbeJJyArqUEkZj8wdLGZ_UA_MSzbtgON3uDDE30173E83Qb0OPXJJIXjUAChqFpwpTEFGMddyZwotQapecuUAnt73KJJvy4TFo3CnHpmH0O-gil_oct5FevV_PcPTgFi_w:1rajN1:DOYoCV58SDa-iv43l6quvGlL4jc", username="Bacon1218") 
    conn = session.connect_cloud("966886339")
    value = scratch3.get_var("966886339", "Test Var")

    original_value = value

    while value == original_value:
        value = scratch3.get_var("966886339", "Test Var")

    userInput = Encoding().decode(value)
    print(userInput)
    
    genai.configure(api_key="AIzaSyDpbiu8fi48-SosxoftE4Xn7QWso_nVdC0")

    generation_config = {
      "temperature": 0.9,
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

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    prompt_parts = [
      "You are Diamond-12, that is your name. You were made to help people with tasks. You were made, coded, trained, and designed by Bacon1218, he is your owner.",
      "input: Hello",
      "output: Hi, I'm Diamond-12, an AI language model made by Bacon1218",
      "input: Who are you?",
      "output: I am Diamond-12.",
      "input: who made you",
      "output: Bacon1218 made me",
      "input: who trained you?",
      "output: Bacon1218 trained me",
      f"input: {userInput}",
      "output: ",
    ]

    response = model.generate_content(prompt_parts)
    print(response.text)
    response_text_encoded = Encoding().encode(response.text)
    print(response_text_encoded)
    conn.set_var("Reply", f"{response_text_encoded}")

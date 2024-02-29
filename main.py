import google.generativeai as genai
import math
import scratchattach as scratch3
import streamlit as st
import time

session = scratch3.Session(".eJxVj8FOwzAQRP8lZwix13ac3hrUQw8FCSQkeok29joxbewqSUGA-HccKZde583OzP5m14nGgANlm6xGEwPjTGd32RxPFJJWMQIN1nLgJNBCVaAuhSJQUhiOevN4jM-f3balt-O3Gs2-ZtMeDjv1OpgUc46dD_f-kpJA54zLnBVFLiGhBq9z3yz1jbeJJyArqUEkZj8wdLGZ_UA_MSzbtgON3uDDE30173E83Qb0OPXJJIXjUAChqFpwpTEFGMddyZwotQapecuUAnt73KJJvy4TFo3CnHpmH0O-gil_oct5FevV_PcPTgFi_w:1rajN1:DOYoCV58SDa-iv43l6quvGlL4jc", username="Bacon1218") #The username field is case sensitive
conn = session.connect_cloud("966886339")
value = scratch3.get_var("966886339", "Test Var")
print(value)

conn.set_var("Reply", "9") #the variable name is specified without the cloud emoji

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

while True:
    # Get updated value and generate response
    value = scratch3.get_var("966886339", "Test Var")
    response = model.generate_content(prompt_parts + [f"input: {value}", "output: "])

    # Update placeholder element with new response
    st.empty().write(Encoding.encode(response.text))

    time.sleep(1)  # Adjust sleep time for desired polling interval

import nltk
import random
import time
from datetime import datetime
from nltk.chat.util import Chat, reflections

nltk.download("punkt")

# =====================

# CHAT PATTERNS

# =====================

pairs = [

[r"(hi|hello|hey|hola)",["Hello Stark 👋","Hey! Nice to see you.","Hi there. How can I help?"]],[r"(how are you)",["I am doing great ⚡ What about you?","All good here. How's your day?"]],
[r"(my name is (.*))",["Nice to meet you %2!"]],[
r"(what is your name)",["I am SmartBot — your Python chatbot."]],[r"(help)",["""
I can:

1. Tell time
2. Tell jokes
3. Do calculations
4. Chat
5. Exit
   """
   ]
   ],

[
r"(tell me a joke)",
[
"Why do programmers hate nature? Too many bugs 😭",
"Python developers never die. They just stop responding."
]
],

[
r"(time)",
[
datetime.now().strftime(
"Current time → %I:%M %p"
)
]
],

[
r"(bye|quit|exit)",

[
"See you Stark 🚀"
]

],

[
r"(.*)",

[
"Interesting... tell me more.",
"I didn't fully understand that.",
"Can you say that differently?"
]

]

]

# =====================

# CHATBOT

# =====================

bot = Chat(
pairs,
reflections
)

# =====================

# TYPING EFFECT

# =====================

def typing(text):

```
for i in text:

    print(
        i,
        end="",
        flush=True
    )

    time.sleep(.01)

print()
```

# =====================

# CALCULATOR

# =====================

def calculate(msg):

```
try:

    if "+" in msg:

        a,b=msg.split("+")
        return float(a)+float(b)

    elif "-" in msg:

        a,b=msg.split("-")
        return float(a)-float(b)

    elif "*" in msg:

        a,b=msg.split("*")
        return float(a)*float(b)

    elif "/" in msg:

        a,b=msg.split("/")
        return float(a)/float(b)

except:

    return None
```

# =====================

# MAIN CHAT

# =====================

def start():

```
typing(
```

"""
SMART CHATBOT
Type 'help'
Type 'exit'
"""
)

```
while True:

    msg=input(
```

"\nYou → "
)

```
    if msg.lower()=="exit":

        typing(
```

"Goodbye 🚀"
)

```
        break


    result=calculate(
```

msg
)

```
    if result!=None:

        typing(
```

f"Answer → {result}"
)

```
        continue


    reply=bot.respond(
```

msg
)

```
    typing(
```

reply
)

# =====================

if **name**=="**main**":

```
start()
```

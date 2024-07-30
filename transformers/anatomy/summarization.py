

text = """Dear Amazon, last week I ordered an Optimus Prime action figure from your online store in Germany. Unfortunately, when I opened the package, I discoverd to my horror that I had been sent an action figure of Gashtuk instead ! As a lifelong enemy of Decepticons, I hope you can understand my dilemma. I really feel stuck! To resolve the issue, I demand an exchange of Gashtuk for the Optimus Prime figure I ordereed. Enclosed are copies of my records concerning this purchase. I expect to hear from your soon. Sincerely, Bumblebee. """

#text = """Dear Amazon, last week I ordered an Optimus Prime action figure from your online store in Germany. Unfortunately, when I opened the package, I discoverd to my horror that the package was empty ! As a lifelong enemy of Decepticons, I hope you can understand my dilemma. I really feel stuck! To resolve the issue, I demand you resend the Optimus Prime I ordereed, this time with the actual Optimus Prime. Enclosed are copies of my records concerning this purchase. I expect to hear from your soon. Sincerely, Bumblebee. """

from transformers import pipeline
summarizer = pipeline("summarization")

import pandas as pd
outputs = summarizer(text, max_length=56, clean_up_tokenization_spaces=True)
print(outputs[0]['summary_text'])





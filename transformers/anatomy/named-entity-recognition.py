

text = """Dear Amazon, last week I ordered an Optimus Prime action figure from your online store in Germany. Unfortunately, when I opened the package, I discoverd to my horror that I had been sent an action figure of Megatron instead ! As a lifelong enemy of Decepticons, I hope you can understand my dilemma. To resolve the issue, I demand an exchange of Megatron for the Optimus Prime figure I ordereed. Enclosed are copies of my records concerning this purchase. I expect to hear from your soon. Sincerely, Bumblebee. """

from transformers import pipeline
ner_tagger = pipeline("ner", aggregation_strategy = "simple")

import pandas as pd
outputs = ner_tagger(text)
print(pd.DataFrame(outputs))


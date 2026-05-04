import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

texts = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        p = pattern.lower()

        texts.append(p)
        labels.append(intent["tag"])

        # Add variations automatically
        texts.append("tell me about " + p)
        labels.append(intent["tag"])

        texts.append(p + " trip")
        labels.append(intent["tag"])

        texts.append("cost of " + p)
        labels.append(intent["tag"])

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression(max_iter=200)
model.fit(X, labels)

pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained successfully")
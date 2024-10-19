import torch
from transformers import ElectraTokenizer, ElectraForSequenceClassification

name = 'beomi/KcELECTRA-base-v2022'
model = ElectraForSequenceClassification.from_pretrained(name, num_labels=3)
tokenizer = ElectraTokenizer.from_pretrained(name)
label = ['부정', '중립', '긍정']

def get_emotions(titles, contents):
    results = []
    for title, content in zip(titles, contents):
        text = title + content
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)

        with torch.no_grad():
            outputs = model(**inputs)

        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        sentiment = torch.argmax(probs, dim=1).item()
        predict = label[sentiment]

        results.append(predict)

    return results
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
result = classifier([
    "I've been waiting for a hugging face course my whole life",
    "I'm not satisfied with the course"
    ])

print(result)


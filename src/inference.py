from transformers import AutoTokenizer, pipeline

# Load the base model tokenizer
tokenizer = AutoTokenizer.from_pretrained('tabularisai/multilingual-sentiment-analysis')

# Load the classification pipeline with the specified model
pipe = pipeline("text-classification", model="Neleac/yelp-review-classifier", tokenizer=tokenizer)

# Classify a new Yelp review
review = "This is by far my favorite Panera location in the Pittsburgh area. \
        Friendly, plenty of room to sit, and good quality food & coffee. \
        Panera is a great place to hang out and read the news - they even have free WiFi! \
        Try their toasted sandwiches, especially the chicken bacon dijon."

result = pipe(review)

# Print the result
print(result) # [{'label': 'Very Positive', 'score': 0.7158929109573364}]

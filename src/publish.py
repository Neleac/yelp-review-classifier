from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained('trainer_output/checkpoint-22000')

model.push_to_hub('Neleac/yelp-review-classifier')
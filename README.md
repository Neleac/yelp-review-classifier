<h1 align='center'> Yelp Review Classification Model </h1>

<div align="center">
  <a href="https://huggingface.co/Neleac/yelp-review-classifier">
    <img src="https://img.shields.io/badge/Hugging%20Face-Neleac/yelp--review--classifier-yellow.svg">
  </a>
</div>

This model takes the text from a Yelp review and predicts a label corresponding to the number of stars for the review. The labels are:
* "Very Negative" = 1 star
* "Negative" = 2 stars
* "Neutral" = 3 stars
* "Positive" = 4 stars
* "Very Positive" = 5 stars

## Base Model
[Tabularis.ai Multilingual Sentiment Classification Model](https://huggingface.co/tabularisai/multilingual-sentiment-analysis)

## Dataset
[Yelp Review Full](https://huggingface.co/datasets/Yelp/yelp_review_full)
* train samples: 520000
* validation samples: 130000

## Training Hyperparameters
* initial learning rate: 1e-5
* learning rate decay: linear
* batch size: 64
* epochs: 5

## Evaluation
* test samples: 50000
* accuracy: 0.6772

## Usage
The easiest way to inference the model is through its [Hugging Face checkpoint](https://huggingface.co/Neleac/yelp-review-classifier).

Alternatively, clone this repo and run the code with [uv](https://docs.astral.sh/uv/):
```
uv run src/inference.py
```

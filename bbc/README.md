# BBC Dataset

This dataset contains categorized BBC news articles. It is intended for natural language processing tasks such as text classification, sentiment analysis, and topic modeling.

## Dataset Information

- **Source**: BBC News
- **Number of Samples**: 2,000
- **Categories**: Business, Entertainment, Politics, Sport, Tech
- **Format**: CSV

## Usage

To load this dataset in your project:

```python
from datasets import load_dataset

dataset = load_dataset("davidstroudLLJD/bbc")

from datasets import Dataset, DatasetDict
import pandas as pd
# Load your dataset
df = pd.read_csv('/Users/davidstroud/Desktop/bbc_dataset.csv')
dataset = Dataset.from_pandas(df)

# Push to Hugging Face
dataset.push_to_hub("davidstroudLLJD/bbc")

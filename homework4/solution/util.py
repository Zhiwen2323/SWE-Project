import boto3
import torch
from torch.utils.data import Dataset
from transformers import AutoTokenizer


def load_data_from_s3(path: str):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Load the file from S3
    obj = s3.get_object(Bucket='your-bucket', Key=path)
    content = obj['Body'].read().decode('utf-8')

    return content


def write_data_to_s3(data: str, path: str):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Write the data to S3
    s3.put_object(Bucket='your-bucket', Key=path, Body=data.encode('utf-8'))


def tokenize(context, pretrain_model):
    # Instantiate a tokenizer
    tokenizer = AutoTokenizer.from_pretrained(pretrain_model)

    # Add a new padding token to the tokenizer
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})

    tokenized_text = tokenizer(context, truncation=True)

    return tokenizer, tokenized_text


class TextDataset(Dataset):
    def __init__(self, tokenized_text):
        self.input_ids = tokenized_text['input_ids']
        self.attention_mask = tokenized_text['attention_mask']

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, index):
        return {
            'input_ids': torch.tensor(self.input_ids[index], dtype=torch.long),
            'attention_mask': torch.tensor(self.attention_mask[index], dtype=torch.long)
        }


import torch
from torch.utils.data import Dataset
from transformers import AutoTokenizer


def load_data_from_s3(path: str):
    # TODO: finish this function to be able to read data from aws s3
    content = ""
    return content


def write_data_to_s3():
    # TODO finish this function to write data to s3
    return None


def tokenize(context, pretrain_model):
    # Instantiate a tokenizer
    tokenizer = AutoTokenizer.from_pretrained(pretrain_model)

    # TODO: Add a new padding token to the tokenizer
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

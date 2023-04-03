
from transformers import AutoModelWithLMHead
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForLanguageModeling
from util import load_data_from_s3, tokenize, TextDataset


def main():
    # Instantiate a pretrained model
    model = AutoModelWithLMHead.from_pretrained("distilgpt2")

    # Load data from s3
    data = load_data_from_s3("s3://your-bucket/your-data.txt")

    # Tokenize the content
    tokenizer = model.tokenizer
    tokenized_text = tokenizer.batch_encode_plus(
        [data], max_length=512, truncation=True, padding="max_length"
    )["input_ids"]

    # Create the dataset
    dataset = TextDataset(tokenized_text)

    # Instantiate a data collator
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False
    )

    # Define training arguments
    training_args = TrainingArguments(
        output_dir='./results',
        evaluation_strategy='steps',
        eval_steps=1000,
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        num_train_epochs=1,
        save_steps=1000,
        save_total_limit=2
    )

    # Instantiate a trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        tokenizer=tokenizer,
        eval_dataset=dataset,
        data_collator=data_collator,
        compute_metrics=None  # we don't need to compute any metrics for language modeling
    )

    # Train the model
    trainer.train()

    # Save the model and upload to S3
    trainer.save_model("./saved_model")


if __name__ == '__main__':
    main()

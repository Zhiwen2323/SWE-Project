
from transformers import AutoModelWithLMHead
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForLanguageModeling
from util import load_data_from_s3, tokenize, TextDataset


def main():
    # Instantiate a pretrained model
    model = AutoModelWithLMHead.from_pretrained("distilgpt2")

    # TODO: load data from s3
    data = load_data_from_s3()

    # TODO finish to tokenize the content
    tokenizer, tokenized_text = tokenize(data, model)

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

    # TODO Train the model

    # TODO save the model and upload to S3
    trainer.save_model("saved_model")


if __name__ == '__main__':
    main()

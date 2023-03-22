# homework 4 Train GPT to write harry potter story

## Instruction
The goal of this homework is to let you experience of data engieering and machine learning. 


## Tasks
1. Finish all the TODOs in the python scripts
2. run `docker-compose up` at homework4 to start spark cluster
   a. More details of using Spark cluster locally refer to: https://github.com/cluster-apps-on-docker/spark-standalone-cluster-on-docker#quick-start 
3. run the data engineering step in spark and write cleaned data back to S3.
4. run the training pipeline to train the GPT-2 model using your cleaned data in s3, and save the model
5. Update the homework1 api using the `serving.py` module to serve the model
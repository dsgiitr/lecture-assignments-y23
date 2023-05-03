# Random Text Generator using Character Level Transformer

A simple script to train transformer decoder like model on any text corpus you want and generate random text out of it. It will automatically run on GPU if detected and set up properly.  

## Instructions
---
Before training make sure you have Weights and Biases API keys set up as you will be needing it for logging.  
### To run the training script :
```console
$ sh script.sh
```
Then it will prompt for all the details required and start training. The dataset link should be .txt URL which will be downloaded in `dataset/file.txt` and the generated text will be on based on that file.
While traning it will checkpoint the model and optimizer every iteration in `checkpoint.pt` so that you can resume the traning afterwards. 
### To generate sample text based on [Tiny Shakespeare Dataset](https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt) : 
This was trained on same model with 8 layers and 8 heads
```console
$ python3 sample_generation.py [TEXT] [NUM_GENERATIONS]
```
`[NUM_GENERATIONS]` means the number of characters that will be generated  
`[TEXT]` is the initial input given to the model which it will continue and generate
### To generate on the basis of your text run :
```console
$ python3 generate.py [TEXT] [NUM_GENERATIONS]
```
All the outputs generated will be written in `output.txt` file 

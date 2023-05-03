import sys
import torch
import torch.nn as nn
import torch.nn.functional as f
import os
import wandb
from tqdm import tqdm
num_epochs = int(sys.argv[1])
batch_size = int(sys.argv[2])

resume = False
if 'checkpoint.pt' in os.listdir():
    resume = input('Do you wish to resume training (previous checkpoint will be deleted) ? [Y/n] ')
    if resume.lower() == 'y' :
        resume = True
    else :
        resume = False


text = open('dataset/file.txt').read()
chars = sorted(list(set(text)))

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

stoi = dict()
itos = dict()
for i, j in enumerate(chars):
    stoi[j] = i
    itos[i] = j
def encode(s):
    return torch.tensor([stoi[i] for i in s]).long()
def decode(l):
    return ''.join([itos[i.item()] for i in l])


def getPositionEncoding(seq_len, d, n=100):
    P = torch.zeros((seq_len, d))
    for k in range(seq_len):
        for i in range(int(d/2)):
            denominator = n ** (2*i/d)
            P[k, 2*i] = torch.tensor((k/denominator)).sin()
            P[k, 2*i+1] = torch.tensor((k/denominator)).cos()
    return P.float()


vocab_size = len(stoi)
embed_dim = 128
block_size = 32

class NN(nn.Module):
    def __init__(self):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.fc1 = nn.Linear(embed_dim, vocab_size)
        self.layer = nn.TransformerEncoderLayer(embed_dim, 8, 512, batch_first = True)
        self.transformer_encoder = nn.TransformerEncoder(self.layer, num_layers = 8)
    def forward(self, x):
        x = self.embedding(x)
        B, T, C = x.shape
        self.pos_embed = getPositionEncoding(T, embed_dim)
        x = x + self.pos_embed
        mask = (torch.triu(torch.ones(T, T)) == 1).transpose(0, 1)
        mask = mask.float().masked_fill(mask == 0, float('-inf')).masked_fill(mask == 1, float(0.0))
        mask = mask.to(device)
        out = self.transformer_encoder(x, mask)
        out = self.fc1(out)
        return out
    
encoded = encode(text)

def get_batch():
    idx = torch.randint(0, len(text) - block_size, (batch_size, ))
    x = torch.stack([encoded[i : i + block_size] for i in idx])
    y = torch.stack([encoded[i : i + block_size] for i in idx])
    return x, y

old_epoch = 0
if resume :
    model = NN().to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr = 1e-3)
    checkpoint = torch.load('models/checkpoint.pt')
    model.load_state_dict(checkpoint['model'])
    optimizer.load_state_dict(checkpoint['optimizer'])
    old_epoch = checkpoint['epoch']
else :
    model = NN().to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr = 1e-3)


wandb.init(
    project = sys.argv[3],
    config = { 
    "dataset" : sys.argv[4],
    "architecture": "transformer",
    "epochs": old_epoch + num_epochs
    } ,
)
for epoch in tqdm(range(old_epoch, num_epochs + old_epoch)):
    x, y = get_batch()
    y_hat = model(x)
    loss = f.cross_entropy(model(x).view(-1, vocab_size), y.view(-1))
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    wandb.log({ "loss": loss.item()})
    torch.save({
        'epoch' : epoch,
        'model' : model.state_dict(),
        'optimizer' : optimizer.state_dict()
    }, "checkpoint.pt")

print("Training completed !")
wandb.finish()
 



import torch
import torch.nn as nn
import torch.nn.functional as f
import sys

text = open('dataset/shakespeare.txt').read()
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

generated = ''

@torch.no_grad()
def generate(inp, max_new_tokens):
    global generated
    final = decode(inp[0])
    print(final, end = '')
    inp = inp.to(device)
    for i in range(max_new_tokens):
        out = model(inp).detach()
        out = out[:,-1, :]
        out = out[0]
        i = torch.multinomial(f.softmax(out, 0), 1)
        final += itos[i[0].item()]
        generated += itos[i[0].item()]
        print(itos[i[0].item()], end = '')
        inp = torch.cat((inp, i.view(1, 1)), 1)
        a, b = inp.shape
        if b > 16 :
            inp = inp[:, 1:]
    #return None
block_size = 32
vocab_size = 65
embed_dim = 128



model = NN()
model.load_state_dict(torch.load('pretrained.pt', map_location = device))
print(generate(encode(
f'''{sys.argv[1]}''').view(1, -1), int(sys.argv[2])))

print()

with open('output.txt','w') as file:
    file.write(generated)
print('Generated output written in output.txt')
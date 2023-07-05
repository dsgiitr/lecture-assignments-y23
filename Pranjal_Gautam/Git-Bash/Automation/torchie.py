import torch
import torch.nn as nn
from torch.autograd import variable
from torch.utils.data import Dataset, DataLoader
import torch.optim as optim
import pandas as pd
import sys
if __name__=="__main__":
    testpath=(sys.argv[6])
    trainpath=sys.argv[1]
    lrcheck=int(sys.argv[2])
    learn_rate=float(sys.argv[4])
    epoch=int(sys.argv[3])
    batch_size=int(sys.argv[5])

df = pd.read_csv(trainpath)

num_features = len(df.columns) - 1

target_variable = df.columns[-1]

num_classes = len(df[target_variable].unique())

class CustomDataset(Dataset):
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        x = torch.Tensor(self.data.iloc[idx, :-1].values.astype(float))
        y = torch.Tensor(self.data.iloc[idx, -1:].values.astype(float))
        return x, y
train_dataset = CustomDataset(trainpath)
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_dataset = CustomDataset(testpath)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

class Net(nn.Module):
    
    def __init__(self,input_size,hidden1_size,hidden2_size,num_classes):
        
        super(Net,self).__init__()
        self.fc1=nn.Linear(input_size,hidden1_size)
        self.fc2=nn.Linear(hidden1_size,hidden2_size)
        self.fc3=nn.Linear(hidden2_size,num_classes)
        
        self.relu1=nn.ReLU()
        self.relu2=nn.ReLU()
    
    def forward(self,x):
        x =self.fc1(x)
        x =self.relu1(x)
        x =self.fc2(x)
        x =self.relu2(x)
        x =self.fc3(x)
        return x

if lrcheck==2:
    model = Net(num_features,100,50,num_classes)
    optimizer = optim.SGD(model.parameters(), lr=learn_rate)
    for i in range(epoch):
        for input, target in train_loader:
            optimizer.zero_grad()
            output = model(input)
            loss = nn.functional.mse_loss(output, target)
            loss.backward()
            optimizer.step()
else:
    model = Net(num_features,100,50,1)
    optimizer = optim.SGD(model.parameters(), lr=learn_rate)
    for i in range(epoch):
        for input, target in train_loader:
            optimizer.zero_grad()
            output = model(input)
            loss = nn.functional.mse_loss(output, target)
            loss.backward()
            optimizer.step()

predictions = []
with torch.no_grad():
    for data, _ in test_loader:
        output = model(data)
        _, predicted = torch.max(output, 1)
        predictions.extend(predicted.tolist())

output_df = pd.DataFrame({'predicted_class': predictions})
output_df.to_csv('output.csv', index=False)


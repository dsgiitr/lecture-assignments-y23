import tensorflow as tf
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os
import sys


handle=sys.argv[1]
npage=sys.argv[2]
my_string=sys.argv[3]
n=sys.argv[4]




# handle = input("Type Your Handle ")

for i in range (1,npage):
    # print('grabbing data')
    gen_url='https://codeforces.com/submissions/'+handle+'/page/'+str(i)
#     print(gen_url)
    r=urlopen(gen_url)
#     print('done')

problem_id=[]
no_name=[]
soup=BeautifulSoup(r)
co=soup.find_all('td')

for row in range(1,len(co)):
    if len(co[row].attrs)==4:
        if len(co[row].span.attrs)==5:
            if co[row].span.attrs['submissionverdict'] == 'OK':
                problem_id.append(co[row].span.attrs['submissionid'])
                no_name.append(row)


contest_id = []
for j in range(0,len(no_name)):
    query = no_name[j]
    contest_id.append(co[query-2].a.attrs['href'].split('/')[2])
    
    
    
for j in range(0, len(contest_id)):
    url = 'http://codeforces.com/contest/'+contest_id[j]+'/submission/'+problem_id[j]
    r =urlopen(url)
    soup = BeautifulSoup(r)
    var = soup.find_all('td')
    problem_name = var[2].a['href'].split('/')[4]
#     print(var[2].a['href'].split('/')[4])
#     print('getting code '+contest_id[j]+'-'+problem_name)
    
    co=soup.find_all('div')
    target=open('collect11.txt','a')
    
    for row in co[3].find_all('pre',attrs={"class" : "program-source"}):
        target.write(row.text+'\n\n')
        
#     print('got code'+contest_id[j]+'-'+problem_name)
    target.close()
    

f=open('collect.txt')
Collection=f.read()


text_vec_layer=tf.keras.layers.TextVectorization(split="character",standardize="lower")
text_vec_layer.adapt([Collection])
encoded=text_vec_layer([Collection])[0]

encoded-=2
n_tokens=text_vec_layer.vocabulary_size()-2
dataset_size=len(encoded)

def to_dataset(sequence, length,shuffle=False, seed=None, batch_size=32):
  ds=tf.data.Dataset.from_tensor_slices(sequence)
  ds=ds.window(length+1,shift=1,drop_remainder=True)
  ds=ds.flat_map(lambda window_ds:window_ds.batch(length+1))
  if shuffle:
    ds=ds.shuffle(buffer_size=100_000,seed=seed)

  ds=ds.batch(batch_size)
  return ds.map(lambda window: (window[:,:-1],window[:,1:])).prefetch(1)
  
  
  
length=100
tf.random.set_seed(42)
train_set=to_dataset(encoded[:1_000_000],length=length,shuffle=True,seed=42)
valid_set=to_dataset(encoded[1_000_000:1_06_000],length=length)
test_set=to_dataset(encoded[1_06_000:],length=length)


model=tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=n_tokens, output_dim=16),
    tf.keras.layers.GRU(128,return_sequences=True),
    tf.keras.layers.Dense(n_tokens,activation="softmax")
])
model.compile(loss="sparse_categorical_crossentropy",optimizer="nadam",
metrics=["accuracy"])
model_ckpt=tf.keras.callbacks.ModelCheckpoint(
    "my_model", monitor="val_accuracy",save_best_only=True)
history=model.fit(train_set,validation_data=valid_set,epochs=10,callbacks=[model_ckpt])


my_model=tf.keras.Sequential([
    text_vec_layer,
    tf.keras.layers.Lambda(lambda X: X-2),
    model
])

y_proba=my_model.predict(["whi"])[0,-1]
y_pred=tf.argmax(y_proba)
text_vec_layer.get_vocabulary()[y_pred+2]

log_probas=tf.math.log([[0.5,0.4,0.1]])
tf.random.set_seed(42)
tf.random.categorical(log_probas, num_samples=8)


#my_string = "int main()"
for i in range(n):
  y_proba=my_model.predict([my_string])[0,-1]
  y_pred=tf.argmax(y_proba)
  ch = text_vec_layer.get_vocabulary()[y_pred+2]
  my_string += ch
  
  
with open('output.txt','w') as file:
    file.write(my_string)
print('Generated output written in output.txt')

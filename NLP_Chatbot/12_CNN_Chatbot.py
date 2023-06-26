# 필요한 모듈 임포트 
import pandas as pd
import tensorflow as tf
from tensorflow.keras import preprocessing
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dense, Dropout, Conv1D, GlobalMaxPool1D, concatenate


# 데이터 읽어오기 ❶
train_file = "./ChatbotData.csv"
data = pd.read_csv(train_file, delimiter=',')
features = data['Q'].tolist()
labels = data['label'].tolist()

# 단어 인덱스 시퀀스 벡터 ❷
corpus = [preprocessing.text.text_to_word_sequence(text) for text in features]

tokenizer = preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(corpus)
sequences = tokenizer.texts_to_sequences(corpus) # 문장내 모든 단어를 시퀀스 번호로 변환함 
word_index = tokenizer.word_index


MAX_SEQ_LEN = 15  # 단어시퀀스 벡터 크기 ---> 시퀀스 번호로 변환된 전체 벡터 크기를 동일하게 맞추기위해 상수선언 
padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')
        #  케라스에서는 pad_sequences ( ) 함수를 통해 시퀀스의 패딩 처리함 167 그림6-18하단설명



# 학습용, 검증용, 테스트용 데이터셋 생성 ➌ 
# 학습셋:검증셋:테스트셋 = 7:2:1
ds = tf.data.Dataset.from_tensor_slices((padded_seqs, labels))  #패딩 처리된 시퀀스(padded_seqs) 벡터리스트와 감정 (labels)리스트 전체를 데이터셋 객체로 만듬 
ds = ds.shuffle(len(features))  # 데이터셋 객체를 랜덤하게 섞음 
train_size = int(len(padded_seqs) * 0.7)    # 실제 학습에 필요한 데이터셋을 각각 분리함  7:2;1의 비율을 정해진 것은 아님 
val_size = int(len(padded_seqs) * 0.2)      # 상동 
test_size = int(len(padded_seqs) * 0.1)     # 상동
train_ds = ds.take(train_size).batch(20)
val_ds = ds.skip(train_size).take(val_size).batch(20)
test_ds = ds.skip(train_size + val_size).take(test_size).batch(20)

# 하이퍼파라미터 설정
dropout_prob = 0.5
EMB_SIZE = 128
EPOCH = 5
VOCAB_SIZE = len(word_index) + 1  # 전체 단어 수

# CNN 모델 정의 ❹                          # CNN 모델을 케라스 함수형 모델 방식으로 구현함 
input_layer = Input(shape=(MAX_SEQ_LEN,))                                                       # 그림-6-19의 단어임베딩 
embedding_layer = Embedding(VOCAB_SIZE, EMB_SIZE, input_length=MAX_SEQ_LEN)(input_layer)        # 상동
dropout_emb = Dropout(rate=dropout_prob)(embedding_layer)                                       # 상동

conv1 = Conv1D(filters=128, kernel_size=3, padding='valid', activation=tf.nn.relu)(dropout_emb) # 그림-6-19의 특징추출
pool1 = GlobalMaxPool1D()(conv1)                                                                #상동
#
conv2 = Conv1D(filters=128, kernel_size=4, padding='valid', activation=tf.nn.relu)(dropout_emb) #상동
pool2 = GlobalMaxPool1D()(conv2)                                                                #상동
#
conv3 = Conv1D(filters=128, kernel_size=5, padding='valid', activation=tf.nn.relu)(dropout_emb) #상동
pool3 = GlobalMaxPool1D()(conv3)                                                                #상동                                                           #

# 3, 4, 5- gram 이후 합치기
concat = concatenate([pool1, pool2, pool3])                                                     # 그림-6-19의 분류
hidden = Dense(128, activation=tf.nn.relu)(concat)                                              #상동
dropout_hidden = Dropout(rate=dropout_prob)(hidden)                                             #상동
logits = Dense(3, name='logits')(dropout_hidden)                                                #상동
predictions = Dense(3, activation=tf.nn.softmax)(logits)                                        #상동

# 모델 생성 ❺
model = Model(inputs=input_layer, outputs=predictions)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 모델 학습 ❻
model.fit(train_ds, validation_data=val_ds, epochs=EPOCH, verbose=1)

# 모델 평가(테스트 데이터셋 이용) ❼
loss, accuracy = model.evaluate(test_ds, verbose=1)
print('Accuracy: %f' % (accuracy * 100))
print('loss: %f' % (loss))

# 모델 저장 ❽
model.save('cnn_model.h5')

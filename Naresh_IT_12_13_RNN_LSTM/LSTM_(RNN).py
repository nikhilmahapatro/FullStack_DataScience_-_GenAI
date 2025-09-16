
# Import Libraries ----------------------------------------------------------
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load text -----------------------------------------------------------------
with open('Mutants.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Tokenize ------------------------------------------------------------------
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
total_words = len(tokenizer.word_index) + 1
print("Total vocab size:", total_words)

# 3. Create sequences -------------------------------------------------------
input_sequences = []
token_list = tokenizer.texts_to_sequences([text])[0]

for i in range(1, len(token_list)):
    n_gram_seq = token_list[:i+1]
    input_sequences.append(n_gram_seq)

print("Total sequences:", len(input_sequences))

# 4. Pad sequences ----------------------------------------------------------
max_seq_len = max([len(x) for x in input_sequences])
input_sequences = pad_sequences(input_sequences, maxlen=max_seq_len, padding='pre')

X = input_sequences[:,:-1]
y = input_sequences[:,-1]

y = tf.keras.utils.to_categorical(y, num_classes=total_words)

print("X shape:", X.shape)
print("y shape:", y.shape)


# Build Model --------------------------------------------------------------
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(total_words, 50, input_length=max_seq_len-1),
    tf.keras.layers.LSTM(100, return_sequences=True),
    tf.keras.layers.LSTM(100),
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(total_words, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()


# Train -------------------------------------------------------------------
model.fit(X, y, epochs=50, verbose=1)

# Generate new text (user input) ------------------------------------------
def generate_text(seed_text, next_words=20):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_seq_len-1, padding='pre')
        predicted = np.argmax(model.predict(token_list, verbose=0), axis=-1)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text

# Input prompt ------------------------------------------------------------
while True:
    seed = input("\nEnter a starting phrase (or type 'quit' to exit): ")
    if seed.lower() == "quit":
        break
    generated = generate_text(seed, next_words=10)  # generate 30 words
    print("\nGenerated text:\n", generated)

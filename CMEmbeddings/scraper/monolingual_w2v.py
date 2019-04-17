 #!/usr/bin/env python
# coding: utf-8

# Reading the data
import sys
import editdistance
from gensim.models import Word2Vec
from gensim.models import FastText 
from gensim.test.utils import common_texts
from gensim.models import Phrases

from datetime import datetime

def prepare_embeddings(file_name, emb_type="w2v"):

	lines = open(file_name).read().splitlines()
	sentences = []

	for line in lines:
		sentence = line.split(",")
		if(len(sentence)>=2):
			sentences.append([word for word in sentence[1].split()])
		else:
			print(sentence)

	# Train Model
	if(emb_type=="w2v"):
		model = Word2Vec(sentences, size=64, alpha=0.025, window=5, min_count=20, max_vocab_size=None, sample=0.001, seed=1, workers=100, min_alpha=0.0001, sg=0, hs=0, negative=5, ns_exponent=0.75, cbow_mean=1, iter=100, null_word=0, trim_rule=None, sorted_vocab=1, batch_words=10000, compute_loss=False, callbacks=(), max_final_vocab=None)

	else:
		model = FastText(sentences, sg=0, hs=0, size=64, alpha=0.025, window=5, min_count=20, max_vocab_size=None, word_ngrams=1, sample=0.001, seed=1, workers=100, min_alpha=0.0001, negative=5, ns_exponent=0.75, cbow_mean=1, iter=100, null_word=0, min_n=3, max_n=6, sorted_vocab=1, bucket=2000000, trim_rule=None, batch_words=10000, callbacks=(), compatible_hash=True)

	print(model)

	#Code for phrase queries
	#bigram_transformer = Phrases(sentences)
	#model = Word2Vec(bigram_transformer[sentences], min_count=1)

	# Code to plot
	# from sklearn.decomposition import PCA
	# from matplotlib import pyplot
	# # fit a 2d PCA model to the vectors
	# X = model[model.wv.vocab]
	# pca = PCA(n_components=2)
	# result = pca.fit_transform(X)
	# # create a scatter plot of the projection
	# pyplot.scatter(result[:, 0], result[:, 1])
	# words = list(model.wv.vocab)
	# for i, word in enumerate(words):
	# 	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
	# pyplot.show()

	# summarize vocabulary
	# words = list(model.wv.vocab)
	# print(words)

	# In[30]:

	# # access vector for one word
	# print(model['haan'])

	# Save Model
	model.save('models/'+"model_size_64"+"mar30"+'.bin')
	#print(model.most_similar("acha",topn=20))

# Arguments
# train/test
argument_one = sys.argv[1]

if(argument_one=="train"):
	
	# w2v or FT
	emb_type = sys.argv[2]
	
	# File name
	file_name = sys.argv[3]
	
	prepare_embeddings(file_name, emb_type)

else:
	model_path = sys.argv[2]
	input_word = sys.argv[3]
	number = int(sys.argv[4])

	#Load model
	new_model = Word2Vec.load(model_path)

	for word, score in new_model.most_similar(input_word,topn=number):
		print(word, score, editdistance.eval(input_word,word))

print("Done!")


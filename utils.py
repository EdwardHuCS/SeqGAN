import cPickle
# load preprocessed dataset
with open('./dataset/dataset2', 'rb') as fp:
    data = cPickle.load(fp)
# load list of unique tokens
with open('./tokens', 'rb') as fp:
    tokens_ref = cPickle.load(fp)

#tokens = []
cnt_tokens = [0] * len(tokens_ref)

for song in data:
    for token in song:
        # count the number of times tokens appear
        idx = tokens_ref.index(token)
        cnt_tokens[idx] += 1
        #if token not in tokens:
        #    tokens.append(token)

print('a')
from __future__ import print_function
from data import IMDB
from model import VRAE
import tensorflow as tf


def main():
    dataloader = IMDB()
    model = VRAE(dataloader.word2idx, dataloader.idx2word)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    print("Loading trained model ...")
    model.saver.restore(sess, model.model_path)

    # lowercase, no punctuation, please 
    model.customized_reconstruct(sess, 'i love this firm and it is beyond my expectation')
    model.customized_reconstruct(sess, 'i want to watch this movie again because it is so interesting')
    model.customized_reconstruct(sess, 'the time taken to develop the characters is quite long')
    model.customized_reconstruct(sess, 'is there any point to make a bad movie like this')
    model.customized_reconstruct(sess, 'sorry but there is no point to watch this movie again')
    model.customized_reconstruct(sess, 'to be honest this movie is not worth my time and money')
    

if __name__ == '__main__':
    main()
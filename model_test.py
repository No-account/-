import tensorflow as tf
in_size=101
out_size=2
Weights = tf.Variable(tf.random_normal([in_size, out_size]), name="weights")
biases=tf.Variable(tf.zeros([1,out_size])+0.1,name="biases")
saver=tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.restore(sess,"/home/ada/PycharmProjects/neural_network/model.ckpt")

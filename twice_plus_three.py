import tensorflow as tf

tf.app.flags.DEFINE_integer('version', 0, 'version')
FLAGS = tf.app.flags.FLAGS

def main(arg):
    export_path = './saved_model_twice_plus_three/{}'.format(str(FLAGS.version))
    with tf.Session() as sess:
        x = tf.placeholder(tf.float32)

        a = tf.Variable(2.0)
        b = tf.Variable(3.0)
        y = tf.add(tf.multiply(a, x), b)

        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        tf.saved_model.simple_save(
            sess,
            export_path,
            inputs={'x': x},
            outputs={'y': y})

if __name__ == "__main__":
    tf.app.run()

                    _aa = tf.one_hot(tf.argmax(_aa, axis=-1), self.a_counts, dtype=tf.float32)
        z = np.correlate(self.x, self.y, 'full')
        assert_array_almost_equal(z, self.z1)
        z = np.correlate(self.y, self.x, 'full')
        z = np.correlate(self.x, self.y, 'full')
        assert_array_almost_equal(z, self.z1)
        z = np.correlate(self.y, self.x, 'full')
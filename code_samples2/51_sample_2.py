        # Assorted tests with NaTs
        ([np.datetime64('NaT'),
          np.datetime64('NaT'),
          np.datetime64('2010-01-03T05:14:12'),
          np.datetime64('NaT'),
          np.datetime64('2015-09-23T10:10:13'),
          np.datetime64('1932-10-10T03:50:30')], 5),
          np.datetime64('NaT'),
        ([np.timedelta64(2, 's'),
          np.timedelta64(1, 's'),
          np.timedelta64('NaT', 's'),
          np.timedelta64(3, 's')], 1),
        ([np.timedelta64('NaT', 's')] * 3, 0),
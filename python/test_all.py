import sys
import unittest

if __name__ == '__main__':
    pattern = 'test*_py%s.py' % sys.version_info.major
    print('running with loader pattern %s' % pattern)
    print('')

    loader = unittest.TestLoader()
    unittest.TextTestRunner(verbosity=2).run(loader.discover('.', pattern=pattern))

# -*- coding: utf-8 -*-

import datetime
import random
import uuid

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from time_uuid import TimeUUID


class TestTimeUUID(unittest.TestCase):

    def test_upgrade(self):
        self.assertIsNone(TimeUUID.upgrade(None))

        origin = TimeUUID(int=random.randrange(1e7))
        upgraded = TimeUUID.upgrade(origin)
        self.assertIsInstance(upgraded, uuid.UUID)
        self.assertIsInstance(upgraded, TimeUUID)
        self.assertEqual(str(upgraded), str(origin))

        origin = uuid.uuid1()
        upgraded = TimeUUID.upgrade(origin)
        self.assertIsInstance(upgraded, uuid.UUID)
        self.assertIsInstance(upgraded, TimeUUID)
        self.assertEqual(str(upgraded), str(origin))

        self.assertRaises(TypeError, TimeUUID.upgrade, 'coucou')

    def test_with_utc(self):
        time = datetime.datetime.utcnow()
        res = TimeUUID.with_utc(time, randomize=True)

        self.assertIsInstance(res, uuid.UUID)
        self.assertIsInstance(res, TimeUUID)

        res1 = TimeUUID.with_utc(time, randomize=False)
        res2 = TimeUUID.with_utc(time, randomize=False)

        self.assertEqual(res1, res2)

    def test_with_utcnow(self):
        res = TimeUUID.with_utcnow()

        self.assertIsInstance(res, uuid.UUID)
        self.assertIsInstance(res, TimeUUID)

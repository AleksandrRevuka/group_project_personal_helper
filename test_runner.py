"""runner"""

import unittest
from tests import (
    test_class_AB,
    test_class_Email,
    test_class_Phone,
    test_class_Record,
    test_class_User,
    test_validation)

ABTestSuite = unittest.TestSuite()
ABTestSuite.addTest(unittest.makeSuite(test_class_AB.TestAddressBook))
ABTestSuite.addTest(unittest.makeSuite(test_class_Email.TestEmail))
ABTestSuite.addTest(unittest.makeSuite(test_class_Phone.TestPhone))
ABTestSuite.addTest(unittest.makeSuite(test_class_Record.TestRecord))
ABTestSuite.addTest(unittest.makeSuite(test_class_User.TestUser))
ABTestSuite.addTest(unittest.makeSuite(test_validation.TestValidation))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(ABTestSuite)

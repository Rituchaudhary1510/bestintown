import unittest


# from test_mobile_view import MobileViewTesting
from test_website_elements import TestWebsite
from test_townpizza import TestTownpizza
from test_menuitems import TestMenuItems
from test_logins import TestBestInTownPizzaLogin
from test_profile_elements import TestBestInTownPizzaProfile
from test_schedule_order import TestOrderSettings

test_suite = unittest.TestSuite([])

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)

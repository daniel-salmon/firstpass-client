# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from firstpass_client.models.user_create import UserCreate

class TestUserCreate(unittest.TestCase):
    """UserCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserCreate:
        """Test UserCreate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserCreate`
        """
        model = UserCreate()
        if include_optional:
            return UserCreate(
                username = '0',
                password = ''
            )
        else:
            return UserCreate(
                username = '0',
                password = '',
        )
        """

    def testUserCreate(self):
        """Test UserCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

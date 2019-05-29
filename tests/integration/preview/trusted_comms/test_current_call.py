# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class CurrentCallTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.trusted_comms.current_calls().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/TrustedComms/CurrentCall',
        ))

    def test_read_found_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "CAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "from": "+15000000000",
                "to": "+573000000000",
                "reason": "Hello Jhon, your appointment has been confirmed.",
                "created_at": "2019-05-01T20:00:00Z",
                "url": "https://preview.twilio.com/TrustedComms/CurrentCall"
            }
            '''
        ))

        actual = self.client.preview.trusted_comms.current_calls().fetch()

        self.assertIsNotNone(actual)
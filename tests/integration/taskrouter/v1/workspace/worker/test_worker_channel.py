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


class WorkerChannelTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces("WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .workers("WKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .worker_channels.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Workers/WKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Channels',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels?PageSize=50",
                    "key": "channels",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels?PageSize=50"
                },
                "channels": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "assigned_tasks": 0,
                        "available": true,
                        "available_capacity_percentage": 100,
                        "configured_capacity": 1,
                        "date_created": "2016-04-14T17:35:54Z",
                        "date_updated": "2016-04-14T17:35:54Z",
                        "sid": "WCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "task_channel_sid": "TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "task_channel_unique_name": "default",
                        "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/WCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "worker_sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces("WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .workers("WKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .worker_channels.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels?PageSize=50",
                    "key": "channels",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels?PageSize=50"
                },
                "channels": []
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces("WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .workers("WKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .worker_channels.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces("WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .workers("WKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .worker_channels("WCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Workers/WKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Channels/WCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_sid_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "assigned_tasks": 0,
                "available": true,
                "available_capacity_percentage": 100,
                "configured_capacity": 1,
                "date_created": "2016-04-14T17:35:54Z",
                "date_updated": "2016-04-14T17:35:54Z",
                "sid": "WCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "task_channel_sid": "TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "task_channel_unique_name": "default",
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/WCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "worker_sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces("WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .workers("WKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .worker_channels("WCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces("WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .workers("WKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .worker_channels("WCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://taskrouter.twilio.com/v1/Workspaces/WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Workers/WKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Channels/WCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "assigned_tasks": 0,
                "available": true,
                "available_capacity_percentage": 100,
                "configured_capacity": 3,
                "date_created": "2016-04-14T17:35:54Z",
                "date_updated": "2016-04-14T17:35:54Z",
                "sid": "WCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "task_channel_sid": "TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "task_channel_unique_name": "default",
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Workers/WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/WCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "worker_sid": "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces("WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .workers("WKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .worker_channels("WCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class HostedNumberOrderList(ListResource):

    def __init__(self, version):
        """
        Initialize the HostedNumberOrderList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderList
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderList
        """
        super(HostedNumberOrderList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/HostedNumberOrders'.format(**self._solution)

    def stream(self, status=values.unset, phone_number=values.unset,
               incoming_phone_number_sid=values.unset, friendly_name=values.unset,
               unique_name=values.unset, limit=None, page_size=None):
        """
        Streams HostedNumberOrderInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param HostedNumberOrderInstance.Status status: The Status of this HostedNumberOrder.
        :param unicode phone_number: An E164 formatted phone number.
        :param unicode incoming_phone_number_sid: IncomingPhoneNumber sid.
        :param unicode friendly_name: A human readable description of this resource.
        :param unicode unique_name: A unique, developer assigned name of this HostedNumberOrder.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            status=status,
            phone_number=phone_number,
            incoming_phone_number_sid=incoming_phone_number_sid,
            friendly_name=friendly_name,
            unique_name=unique_name,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, status=values.unset, phone_number=values.unset,
             incoming_phone_number_sid=values.unset, friendly_name=values.unset,
             unique_name=values.unset, limit=None, page_size=None):
        """
        Lists HostedNumberOrderInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param HostedNumberOrderInstance.Status status: The Status of this HostedNumberOrder.
        :param unicode phone_number: An E164 formatted phone number.
        :param unicode incoming_phone_number_sid: IncomingPhoneNumber sid.
        :param unicode friendly_name: A human readable description of this resource.
        :param unicode unique_name: A unique, developer assigned name of this HostedNumberOrder.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance]
        """
        return list(self.stream(
            status=status,
            phone_number=phone_number,
            incoming_phone_number_sid=incoming_phone_number_sid,
            friendly_name=friendly_name,
            unique_name=unique_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, phone_number=values.unset,
             incoming_phone_number_sid=values.unset, friendly_name=values.unset,
             unique_name=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of HostedNumberOrderInstance records from the API.
        Request is executed immediately

        :param HostedNumberOrderInstance.Status status: The Status of this HostedNumberOrder.
        :param unicode phone_number: An E164 formatted phone number.
        :param unicode incoming_phone_number_sid: IncomingPhoneNumber sid.
        :param unicode friendly_name: A human readable description of this resource.
        :param unicode unique_name: A unique, developer assigned name of this HostedNumberOrder.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderPage
        """
        params = values.of({
            'Status': status,
            'PhoneNumber': phone_number,
            'IncomingPhoneNumberSid': incoming_phone_number_sid,
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return HostedNumberOrderPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of HostedNumberOrderInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return HostedNumberOrderPage(self._version, response, self._solution)

    def create(self, address_sid, phone_number, iso_country, sms_capability, email,
               account_sid=values.unset, friendly_name=values.unset,
               unique_name=values.unset, cc_emails=values.unset,
               sms_url=values.unset, sms_method=values.unset,
               sms_fallback_url=values.unset, sms_fallback_method=values.unset):
        """
        Create a new HostedNumberOrderInstance

        :param unicode address_sid: Address sid.
        :param unicode phone_number: An E164 formatted phone number.
        :param unicode iso_country: ISO country code.
        :param bool sms_capability: Specify SMS capability to host.
        :param unicode email: Email.
        :param unicode account_sid: Account Sid.
        :param unicode friendly_name: A human readable description of this resource.
        :param unicode unique_name: A unique, developer assigned name of this HostedNumberOrder.
        :param unicode cc_emails: A list of emails.
        :param unicode sms_url: SMS URL.
        :param unicode sms_method: SMS Method.
        :param unicode sms_fallback_url: SMS Fallback URL.
        :param unicode sms_fallback_method: SMS Fallback Method.

        :returns: Newly created HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        """
        data = values.of({
            'AddressSid': address_sid,
            'PhoneNumber': phone_number,
            'IsoCountry': iso_country,
            'SmsCapability': sms_capability,
            'Email': email,
            'AccountSid': account_sid,
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'CcEmails': cc_emails,
            'SmsUrl': sms_url,
            'SmsMethod': sms_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsFallbackMethod': sms_fallback_method,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return HostedNumberOrderInstance(
            self._version,
            payload,
        )

    def get(self, sid):
        """
        Constructs a HostedNumberOrderContext

        :param sid: HostedNumberOrder sid.

        :returns: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderContext
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderContext
        """
        return HostedNumberOrderContext(
            self._version,
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a HostedNumberOrderContext

        :param sid: HostedNumberOrder sid.

        :returns: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderContext
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderContext
        """
        return HostedNumberOrderContext(
            self._version,
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.HostedNumbers.HostedNumberOrderList>'


class HostedNumberOrderPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the HostedNumberOrderPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderPage
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderPage
        """
        super(HostedNumberOrderPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of HostedNumberOrderInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        """
        return HostedNumberOrderInstance(
            self._version,
            payload,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.HostedNumbers.HostedNumberOrderPage>'


class HostedNumberOrderContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the HostedNumberOrderContext

        :param Version version: Version that contains the resource
        :param sid: HostedNumberOrder sid.

        :returns: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderContext
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderContext
        """
        super(HostedNumberOrderContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'sid': sid,
        }
        self._uri = '/HostedNumberOrders/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a HostedNumberOrderInstance

        :returns: Fetched HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return HostedNumberOrderInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the HostedNumberOrderInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, friendly_name=values.unset, unique_name=values.unset,
               email=values.unset, cc_emails=values.unset, status=values.unset):
        """
        Update the HostedNumberOrderInstance

        :param unicode friendly_name: A human readable description of this resource.
        :param unicode unique_name: A unique, developer assigned name of this HostedNumberOrder.
        :param unicode email: Email.
        :param unicode cc_emails: A list of emails.
        :param HostedNumberOrderInstance.Status status: The Status of this HostedNumberOrder.

        :returns: Updated HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'Email': email,
            'CcEmails': cc_emails,
            'Status': status,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return HostedNumberOrderInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.HostedNumbers.HostedNumberOrderContext {}>'.format(context)


class HostedNumberOrderInstance(InstanceResource):

    class Status(object):
        RECEIVED = "received"
        PENDING_LOA = "pending-loa"
        CARRIER_PROCESSING = "carrier-processing"
        TESTING = "testing"
        COMPLETED = "completed"
        FAILED = "failed"
        ACTION_REQUIRED = "action-required"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the HostedNumberOrderInstance

        :returns: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        """
        super(HostedNumberOrderInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'incoming_phone_number_sid': payload['incoming_phone_number_sid'],
            'address_sid': payload['address_sid'],
            'signing_document_sid': payload['signing_document_sid'],
            'phone_number': payload['phone_number'],
            'capabilities': payload['capabilities'],
            'friendly_name': payload['friendly_name'],
            'unique_name': payload['unique_name'],
            'status': payload['status'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'email': payload['email'],
            'cc_emails': payload['cc_emails'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: HostedNumberOrderContext for this HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderContext
        """
        if self._context is None:
            self._context = HostedNumberOrderContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: HostedNumberOrder sid.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def incoming_phone_number_sid(self):
        """
        :returns: IncomingPhoneNumber sid.
        :rtype: unicode
        """
        return self._properties['incoming_phone_number_sid']

    @property
    def address_sid(self):
        """
        :returns: Address sid.
        :rtype: unicode
        """
        return self._properties['address_sid']

    @property
    def signing_document_sid(self):
        """
        :returns: LOA document sid.
        :rtype: unicode
        """
        return self._properties['signing_document_sid']

    @property
    def phone_number(self):
        """
        :returns: An E164 formatted phone number.
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def capabilities(self):
        """
        :returns: A mapping of phone number capabilities.
        :rtype: unicode
        """
        return self._properties['capabilities']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description of this resource.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def unique_name(self):
        """
        :returns: A unique, developer assigned name of this HostedNumberOrder.
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def status(self):
        """
        :returns: The Status of this HostedNumberOrder.
        :rtype: HostedNumberOrderInstance.Status
        """
        return self._properties['status']

    @property
    def date_created(self):
        """
        :returns: The date this HostedNumberOrder was created.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this HostedNumberOrder was updated.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def email(self):
        """
        :returns: Email.
        :rtype: unicode
        """
        return self._properties['email']

    @property
    def cc_emails(self):
        """
        :returns: A list of emails.
        :rtype: unicode
        """
        return self._properties['cc_emails']

    @property
    def url(self):
        """
        :returns: The URL of this HostedNumberOrder.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a HostedNumberOrderInstance

        :returns: Fetched HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the HostedNumberOrderInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, friendly_name=values.unset, unique_name=values.unset,
               email=values.unset, cc_emails=values.unset, status=values.unset):
        """
        Update the HostedNumberOrderInstance

        :param unicode friendly_name: A human readable description of this resource.
        :param unicode unique_name: A unique, developer assigned name of this HostedNumberOrder.
        :param unicode email: Email.
        :param unicode cc_emails: A list of emails.
        :param HostedNumberOrderInstance.Status status: The Status of this HostedNumberOrder.

        :returns: Updated HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            unique_name=unique_name,
            email=email,
            cc_emails=cc_emails,
            status=status,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.HostedNumbers.HostedNumberOrderInstance {}>'.format(context)
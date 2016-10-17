#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import inspect

import six

from watcher.objects import base as base
from watcher.objects import fields as wfields
from watcher.objects.notifications import base as notificationbase


@base.WatcherObjectRegistry.register_notification
class ExceptionPayload(notificationbase.NotificationPayloadBase):
    # Version 1.0: Initial version
    VERSION = '1.0'
    fields = {
        'module_name': wfields.StringField(),
        'function_name': wfields.StringField(),
        'exception': wfields.StringField(),
        'exception_message': wfields.StringField()
    }

    @classmethod
    def from_exception(cls, fault):
        trace = inspect.trace()[-1]
        # TODO(gibi): apply strutils.mask_password on exception_message and
        # consider emitting the exception_message only if the safe flag is
        # true in the exception like in the REST API
        return cls(
            function_name=trace[3],
            module_name=inspect.getmodule(trace[0]).__name__,
            exception=fault.__class__.__name__,
            exception_message=six.text_type(fault))


@notificationbase.notification_sample('infra-optim-exception.json')
@base.WatcherObjectRegistry.register_notification
class ExceptionNotification(notificationbase.NotificationBase):
    # Version 1.0: Initial version
    VERSION = '1.0'
    fields = {
        'payload': wfields.ObjectField('ExceptionPayload')
    }

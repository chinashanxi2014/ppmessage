# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2016 PPMessage.
# Guijin Ding, dingguijin@gmail.com
#
#

from .basehandler import BaseHandler
from ppmessage.db.models import DeviceUser

from ppmessage.core.redis import redis_hash_to_dict
from ppmessage.api.handlers.ppgetorggroupuserlisthandler import single_user

from ppmessage.api.error import API_ERR
from ppmessage.core.constant import API_LEVEL

import json
import time
import logging

class PPGetServiceUserListHandler(BaseHandler):
    """
    """
    def _get(self):            
        _r = self.getReturnData()
        _r["list"] = _users
        return

    def initialize(self):
        self.addPermission(api_level=API_LEVEL.PPCOM)
        self.addPermission(api_level=API_LEVEL.PPKEFU)
        self.addPermission(api_level=API_LEVEL.PPCONSOLE)
        self.addPermission(api_level=API_LEVEL.THIRD_PARTY_KEFU)
        self.addPermission(api_level=API_LEVEL.THIRD_PARTY_CONSOLE)
        return

    def _Task(self):
        super(self.__class__, self)._Task()
        self._get()
        return

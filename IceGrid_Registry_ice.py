# **********************************************************************
#
# Copyright (c) 2003-2015 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.6.1
#
# <auto-generated>
#
# Generated from file `Registry.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy
import IceGrid_Exception_ice
import IceGrid_Session_ice
import IceGrid_Admin_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module IceGrid
_M_IceGrid = Ice.openModule('IceGrid')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Start of module IceGrid
__name__ = 'IceGrid'

if 'Registry' not in _M_IceGrid.__dict__:
    _M_IceGrid.Registry = Ice.createTempClass()
    class Registry(Ice.Object):
        '''The IceGrid registry allows clients create sessions
directly with the registry.'''
        def __init__(self):
            if Ice.getType(self) == _M_IceGrid.Registry:
                raise RuntimeError('IceGrid.Registry is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::IceGrid::Registry')

        def ice_id(self, current=None):
            return '::IceGrid::Registry'

        def ice_staticId():
            return '::IceGrid::Registry'
        ice_staticId = staticmethod(ice_staticId)

        def createSession(self, userId, password, current=None):
            '''Create a client session.

Returns:
    A proxy for the newly created session.

Arguments:
    userId The user id.

    password The password for the given user id.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
            pass

        def createAdminSession(self, userId, password, current=None):
            '''Create an administrative session.

Returns:
    A proxy for the newly created session.

Arguments:
    userId The user id.

    password The password for the given user id.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
            pass

        def createSessionFromSecureConnection(self, current=None):
            '''Create a client session from a secure connection.

Returns:
    A proxy for the newly created session.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
            pass

        def createAdminSessionFromSecureConnection(self, current=None):
            '''Create an administrative session from a secure connection.

Returns:
    A proxy for the newly created session.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
            pass

        def getSessionTimeout(self, current=None):
            '''Get the session timeout. If a client or administrative client
doesn't call the session keepAlive method in the time interval
defined by this timeout, IceGrid might reap the session.

Returns:
    The timeout (in seconds).'''
            pass

        def getACMTimeout(self, current=None):
            '''Get the value of the ACM timeout. Clients supporting ACM
connection heartbeats can enable them instead of explicitly
sending keep alives requests.

NOTE: This method is only available since Ice 3.6.

Returns:
    The timeout (in seconds).'''
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_IceGrid._t_Registry)

        __repr__ = __str__

    _M_IceGrid.RegistryPrx = Ice.createTempClass()
    class RegistryPrx(Ice.ObjectPrx):

        '''Create a client session.

Returns:
    A proxy for the newly created session.

Arguments:
    userId The user id.

    password The password for the given user id.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
        def createSession(self, userId, password, _ctx=None):
            return _M_IceGrid.Registry._op_createSession.invoke(self, ((userId, password), _ctx))

        '''Create a client session.

Returns:
    A proxy for the newly created session.

Arguments:
    userId The user id.

    password The password for the given user id.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
        def begin_createSession(self, userId, password, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_IceGrid.Registry._op_createSession.begin(self, ((userId, password), _response, _ex, _sent, _ctx))

        '''Create a client session.

Returns:
    A proxy for the newly created session.

Arguments:
    userId The user id.

    password The password for the given user id.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
        def end_createSession(self, _r):
            return _M_IceGrid.Registry._op_createSession.end(self, _r)

        '''Create an administrative session.

Returns:
    A proxy for the newly created session.

Arguments:
    userId The user id.

    password The password for the given user id.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
        def createAdminSession(self, userId, password, _ctx=None):
            return _M_IceGrid.Registry._op_createAdminSession.invoke(self, ((userId, password), _ctx))

        '''Create an administrative session.

Returns:
    A proxy for the newly created session.

Arguments:
    userId The user id.

    password The password for the given user id.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
        def begin_createAdminSession(self, userId, password, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_IceGrid.Registry._op_createAdminSession.begin(self, ((userId, password), _response, _ex, _sent, _ctx))

        '''Create an administrative session.

Returns:
    A proxy for the newly created session.

Arguments:
    userId The user id.

    password The password for the given user id.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
        def end_createAdminSession(self, _r):
            return _M_IceGrid.Registry._op_createAdminSession.end(self, _r)

        '''Create a client session from a secure connection.

Returns:
    A proxy for the newly created session.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
        def createSessionFromSecureConnection(self, _ctx=None):
            return _M_IceGrid.Registry._op_createSessionFromSecureConnection.invoke(self, ((), _ctx))

        '''Create a client session from a secure connection.

Returns:
    A proxy for the newly created session.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
        def begin_createSessionFromSecureConnection(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_IceGrid.Registry._op_createSessionFromSecureConnection.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Create a client session from a secure connection.

Returns:
    A proxy for the newly created session.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
        def end_createSessionFromSecureConnection(self, _r):
            return _M_IceGrid.Registry._op_createSessionFromSecureConnection.end(self, _r)

        '''Create an administrative session from a secure connection.

Returns:
    A proxy for the newly created session.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
        def createAdminSessionFromSecureConnection(self, _ctx=None):
            return _M_IceGrid.Registry._op_createAdminSessionFromSecureConnection.invoke(self, ((), _ctx))

        '''Create an administrative session from a secure connection.

Returns:
    A proxy for the newly created session.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
        def begin_createAdminSessionFromSecureConnection(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_IceGrid.Registry._op_createAdminSessionFromSecureConnection.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Create an administrative session from a secure connection.

Returns:
    A proxy for the newly created session.

Exceptions:
    PermissionDeniedException Raised if the password for
the given user id is not correct, or if the user is not allowed
access.'''
        def end_createAdminSessionFromSecureConnection(self, _r):
            return _M_IceGrid.Registry._op_createAdminSessionFromSecureConnection.end(self, _r)

        '''Get the session timeout. If a client or administrative client
doesn't call the session keepAlive method in the time interval
defined by this timeout, IceGrid might reap the session.

Returns:
    The timeout (in seconds).'''
        def getSessionTimeout(self, _ctx=None):
            return _M_IceGrid.Registry._op_getSessionTimeout.invoke(self, ((), _ctx))

        '''Get the session timeout. If a client or administrative client
doesn't call the session keepAlive method in the time interval
defined by this timeout, IceGrid might reap the session.

Returns:
    The timeout (in seconds).'''
        def begin_getSessionTimeout(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_IceGrid.Registry._op_getSessionTimeout.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Get the session timeout. If a client or administrative client
doesn't call the session keepAlive method in the time interval
defined by this timeout, IceGrid might reap the session.

Returns:
    The timeout (in seconds).'''
        def end_getSessionTimeout(self, _r):
            return _M_IceGrid.Registry._op_getSessionTimeout.end(self, _r)

        '''Get the value of the ACM timeout. Clients supporting ACM
connection heartbeats can enable them instead of explicitly
sending keep alives requests.

NOTE: This method is only available since Ice 3.6.

Returns:
    The timeout (in seconds).'''
        def getACMTimeout(self, _ctx=None):
            return _M_IceGrid.Registry._op_getACMTimeout.invoke(self, ((), _ctx))

        '''Get the value of the ACM timeout. Clients supporting ACM
connection heartbeats can enable them instead of explicitly
sending keep alives requests.

NOTE: This method is only available since Ice 3.6.

Returns:
    The timeout (in seconds).'''
        def begin_getACMTimeout(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_IceGrid.Registry._op_getACMTimeout.begin(self, ((), _response, _ex, _sent, _ctx))

        '''Get the value of the ACM timeout. Clients supporting ACM
connection heartbeats can enable them instead of explicitly
sending keep alives requests.

NOTE: This method is only available since Ice 3.6.

Returns:
    The timeout (in seconds).'''
        def end_getACMTimeout(self, _r):
            return _M_IceGrid.Registry._op_getACMTimeout.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_IceGrid.RegistryPrx.ice_checkedCast(proxy, '::IceGrid::Registry', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_IceGrid.RegistryPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::IceGrid::Registry'
        ice_staticId = staticmethod(ice_staticId)

    _M_IceGrid._t_RegistryPrx = IcePy.defineProxy('::IceGrid::Registry', RegistryPrx)

    _M_IceGrid._t_Registry = IcePy.defineClass('::IceGrid::Registry', Registry, -1, (), True, False, None, (), ())
    Registry._ice_type = _M_IceGrid._t_Registry

    Registry._op_createSession = IcePy.Operation('createSession', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), ((), _M_IceGrid._t_SessionPrx, False, 0), (_M_IceGrid._t_PermissionDeniedException,))
    Registry._op_createAdminSession = IcePy.Operation('createAdminSession', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), ((), _M_IceGrid._t_AdminSessionPrx, False, 0), (_M_IceGrid._t_PermissionDeniedException,))
    Registry._op_createSessionFromSecureConnection = IcePy.Operation('createSessionFromSecureConnection', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_IceGrid._t_SessionPrx, False, 0), (_M_IceGrid._t_PermissionDeniedException,))
    Registry._op_createAdminSessionFromSecureConnection = IcePy.Operation('createAdminSessionFromSecureConnection', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_IceGrid._t_AdminSessionPrx, False, 0), (_M_IceGrid._t_PermissionDeniedException,))
    Registry._op_getSessionTimeout = IcePy.Operation('getSessionTimeout', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, None, (), (), (), ((), IcePy._t_int, False, 0), ())
    Registry._op_getACMTimeout = IcePy.Operation('getACMTimeout', Ice.OperationMode.Idempotent, Ice.OperationMode.Nonmutating, False, None, (), (), (), ((), IcePy._t_int, False, 0), ())

    _M_IceGrid.Registry = Registry
    del Registry

    _M_IceGrid.RegistryPrx = RegistryPrx
    del RegistryPrx

# End of module IceGrid

Ice.sliceChecksums["::IceGrid::Registry"] = "8298cc0aba1a722d75eb79034fbb076"
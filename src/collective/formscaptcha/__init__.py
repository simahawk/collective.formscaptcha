# -*- extra stuff goes here -*-

from zope.i18nmessageid import MessageFactory

formsCaptchaMF = MessageFactory("collective.formscaptcha")
_ = formsCaptchaMF


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

from zope.schema import ASCIILine
from zope import interface


class ICaptchaField(interface.Interface):
    """ marker interface for CaptchaField
    """


class CaptchaField(ASCIILine):
    interface.implements(ICaptchaField)

from zope.app.form.browser import ASCIIWidget

from .utils import get_image_tag


class CaptchaWidget(ASCIIWidget):

    def __call__(self):
        return get_image_tag()

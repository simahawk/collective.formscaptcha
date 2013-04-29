from zope.app.form.browser import ASCIIWidget
from zope.component.hooks import getSite


class CaptchaWidget(ASCIIWidget):

    @property
    def captcha_view(self):
        site = getSite()
        return site.restrictedTraverse('@@captcha')

    def __call__(self):
        html = self.captcha_view.image_tag()
        return html

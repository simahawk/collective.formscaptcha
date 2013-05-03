# THIS SUCKS!
# need to refactor this properly!

from zope.component.hooks import getSite


def get_image_tag():
    raise NotImplementedError("No captch product found!")

try:
    import collective.recaptcha

    def get_image_tag():
        site = getSite()
        return site.restrictedTraverse('@@captcha').image_tag()

    def verify(context, request):
        return context.restrictedTraverse('@@captcha').verify()


except ImportError:
    pass

try:
    import collective.captcha

    def get_image_tag():
        site = getSite()
        return '<input type="text" name="captcha" />\n' + site.restrictedTraverse('@@captcha').image_tag()

    def verify(context, request):
        view = context.restrictedTraverse('@@captcha')
        value = request.get('captcha')
        return view.verify(value)

except ImportError:
    pass

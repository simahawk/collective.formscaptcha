from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CollectiveformscaptchaLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.formscaptcha
        xmlconfig.file(
            'configure.zcml',
            collective.formscaptcha,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.formscaptcha:default')

COLLECTIVE_FORMSCAPTCHA_FIXTURE = CollectiveformscaptchaLayer()
COLLECTIVE_FORMSCAPTCHA_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_FORMSCAPTCHA_FIXTURE,),
    name="CollectiveformscaptchaLayer:Integration"
)

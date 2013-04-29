# -*- coding: utf-8 -*-

from zope.formlib import form
from zope.app.form.interfaces import WidgetInputError

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName

from plone.app.users.browser.register import RegistrationForm \
                                                as BaseRegistrationForm


from zope.interface import Interface

from .field import CaptchaField
from .widget import CaptchaWidget
from .. import _


class ICaptchaSchema(Interface):
    captcha = CaptchaField(
        title=_(u'Verification'),
        description=_(
            u'Type the code from the picture shown below.'
        ),
    )


class RegistrationForm(BaseRegistrationForm):
    """ Dynamically get fields from user data, through admin
        config settings.
    """
    template = ViewPageTemplateFile('register_form.pt')

    @property
    def portal_props(self):
        return getToolByName(self.context, 'portal_properties')

    @property
    def site_props(self):
        return self.portal_props.site_properties

    @property
    def form_fields(self):
        # Get the fields so we can fiddle with them
        fields = super(RegistrationForm, self).form_fields

        # Add a captcha field to the schema
        fields += form.Fields(ICaptchaSchema)
        fields['captcha'].custom_widget = CaptchaWidget

        return fields

    def validate_registration(self, action, data):
        """
        specific business logic for this join form
        note: all this logic was taken directly from the old
        validate_registration.py script in
        Products/CMFPlone/skins/plone_login/join_form_validate.vpy
        """
        errors = super(RegistrationForm, self).validate_registration(action,
                                                                     data)

        if not self.context.restrictedTraverse('@@captcha').verify():
            error = WidgetInputError('captcha',
                                     u'label_captcha',
                                     u'Wrong captcha')
            errors.append(error)
        return errors

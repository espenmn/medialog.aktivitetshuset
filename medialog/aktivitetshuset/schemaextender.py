from zope.interface import implements
from zope.component import adapts
from zope.i18nmessageid import MessageFactory

from Products.Archetypes.public import StringField, BooleanField

from Products.ATContentTypes.interfaces.news import IATNewsItem
from Products.Archetypes.atapi import MultiSelectionWidget, StringWidget
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender, ISchemaExtender, IBrowserLayerAwareExtender 
from archetypes.schemaextender.field import ExtensionField
from medialog.aktivitetshuset.interfaces import IAktivitetsObject


_ = MessageFactory('medialog.aktivitetshuset')


class _StringExtensionField (ExtensionField, StringField): 
    pass
        
class _BooleanExtensionField(ExtensionField, BooleanField):
	pass    

 
 

class ContentTypeExtender(object):
    """Adapter that adds custom data """
    adapts(IATNewsItem)
    implements(IOrderableSchemaExtender, ISchemaExtender, IBrowserLayerAwareExtender)
    layer = IAktivitetsObject
    _fields = [
        _StringExtensionField("day",
            schemata = "default",
            vocabulary_factory='medialog.aktivitetshuset.DayVocabulary',
            default="",
            interfaces = (IAktivitetsObject,),
            widget = MultiSelectionWidget(
                label = _(u"label_day",
                    default=u"Dag"),
                description = _(u"help_day",
                    default=u"Velg dag"),
                ),
            ),
        _StringExtensionField("time",
            schemata = "default",
            default="",
            interfaces = (IAktivitetsObject,),
            widget = StringWidget(
                label = _(u"label_time",
                    default=u"Klokkeslett"),
                description = _(u"help_time",
                    default=u"Skriv inn klokkeslett"),
                ),
            ),
        ]

    def __init__(self, context):
    	self.context = context

    def getFields(self):
        return self._fields
        
    def getOrder(self, schematas):
        """ Manipulate the order in which fields appear.

        @param schematas: Dictonary of schemata name -> field lists

        @return: Dictionary of reordered field lists per schemata.
        """
        schematas["default"] = ['id', 'title', 'description', 'day', 'time', 'text', 'image', 'imageCaption']

        return schematas


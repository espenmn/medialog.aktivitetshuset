from Products.CMFCore.utils import getToolByName
from zope.interface import directlyProvides
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory

try:
    from zope.app.component.hooks import getSite
except ImportError:
    from zope.component.hooks import getSite

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.aktivitetshuset')

def format_size(size):
    return "".join(size).split(' ')[0]


def DayVocabulary(context):
    site = getSite()
   
    portal_properties = getToolByName(site, 'portal_properties', None)
    if 'day_properties' in portal_properties.objectIds():
        sizes = portal_properties.day_properties.getProperty('allowed_days')
        sizes += ('none',)
        # sizes.append('none')
        terms = [ SimpleTerm(value=format_size(pair), token=format_size(pair), title=pair) for pair in sizes ]
        return SimpleVocabulary(terms)
    else:
        return SimpleVocabulary([
            SimpleTerm('monday', 'monday', u'Mandag'),
            SimpleTerm('tuesday', 'tuesday', u'Tirsdag'),
            SimpleTerm('wednesday', 'wednesday', u'Onsdag'),
            SimpleTerm('thursday', 'thursday', u'Torsdag'),
            SimpleTerm('friday', 'friday', u'Fredag'),
            SimpleTerm('saturday', 'saturday', u'Lordag'),
            SimpleTerm('sunday', 'sunday', u'Sondag'),
        ])  
      
    return SimpleVocabulary(terms)

directlyProvides(DayVocabulary, IVocabularyFactory)

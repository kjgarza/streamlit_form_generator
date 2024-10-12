import streamlit as st
import streamlit_pydantic as sp

from models import Type
from models import Attributes
from models import Activity
from models import Type1
from models import Issn
from models import Type2
from models import Attributes2
from models import Type3
from models import Event
from models import Identifier
from models import AlternateIdentifier
from models import ViewsOverTimeItem
from models import DownloadsOverTimeItem
from models import CitationsOverTimeItem
from models import LandingPage
from models import NameIdentifier
from models import AffiliationItem
from models import Publisher
from models import Container
from models import Subject
from models import DateType
from models import Date
from models import NumberType
from models import RightsListItem
from models import DescriptionType
from models import Description
from models import GeoLocationPoint
from models import GeoLocationBox
from models import GeoLocation
from models import FunderIdentifierType
from models import FundingReference
from models import DoiPropertiesDates
from models import Type5
from models import MessageAction
from models import Type6
from models import Attributes6
from models import Type7
from models import Attributes7
from models import Type8
from models import ProviderContact
from models import ReportingPeriod
from models import Exception
from models import ReportHeader
from models import DatasetIdItem
from models import Period
from models import MetricType
from models import AccessMethod
from models import InstanceItem
from models import PerformanceItem
from models import PublisherIdItem
from models import Type9
from models import DatasetDate
from models import Type10
from models import DatasetContributor
from models import ReportDataset
from models import ReportSubset
from models import Report
from models import DataObject
from models import DataArray
from models import MetaObject
from models import MetaArray
from models import MetaCore
from models import Links
from models import RelationType
from models import ResourceTypeGeneral
from models import ContributorType
from models import RelatedIdentifierType
from models import TitleType
from models import NameType
from models import Certificate
from models import ClientType
from models import State
from models import Source
from models import Region
from models import MemberType
from models import OrganizationTypeEnum
from models import OrganizationType
from models import FocusAreaEnum
from models import FocusArea
from models import SourceId
from models import RelationTypeId
from models import ViewCount
from models import DownloadCount
from models import ReferenceCount
from models import CitationCount
from models import PartCount
from models import PartOfCount
from models import VersionCount
from models import VersionOfCount
from models import Attributes1
from models import Provider
from models import Consortium
from models import Prefixes
from models import Relationships
from models import Client
from models import Client1
from models import ProviderPrefix
from models import Prefix
from models import Relationships1
from models import ClientPrefix
from models import Media
from models import References
from models import Citations
from models import Parts
from models import PartOf
from models import Versions
from models import VersionOf
from models import Relationships2
from models import Relationships3
from models import Creator
from models import Title
from models import Contributor
from models import Types
from models import RelatedIdentifier
from models import RelatedItemIdentifier
from models import Creator1
from models import Title1
from models import Contributor1
from models import RelatedItem
from models import DoiPropertiesMetadata
from models import DoiPropertiesOther
from models import Subj
from models import Obj
from models import Relationships4
from models import Attributes5
from models import Event1
from models import Clients
from models import Providers
from models import ClientPrefixes
from models import ProviderPrefixes
from models import Relationships5
from models import Prefix1
from models import Prefix2
from models import Relationships6
from models import ProviderPrefix1
from models import Attributes8
from models import Contacts
from models import ConsortiumOrganizations
from models import Relationships7
from models import Provider4
from models import Temporal
from models import TotalsObject
from models import Attributes3
from models import Data
from models import DoiDetailItem
from models import Attributes4
from models import DoiListItem

models = [Type, Attributes, Activity, Type1, Issn, Type2, Attributes2, Type3, Event, Identifier, AlternateIdentifier, ViewsOverTimeItem, DownloadsOverTimeItem, CitationsOverTimeItem, LandingPage, NameIdentifier, AffiliationItem, Publisher, Container, Subject, DateType, Date, NumberType, RightsListItem, DescriptionType, Description, GeoLocationPoint, GeoLocationBox, GeoLocation, FunderIdentifierType, FundingReference, DoiPropertiesDates, Type5, MessageAction, Type6, Attributes6, Type7, Attributes7, Type8, ProviderContact, ReportingPeriod, Exception, ReportHeader, DatasetIdItem, Period, MetricType, AccessMethod, InstanceItem, PerformanceItem, PublisherIdItem, Type9, DatasetDate, Type10, DatasetContributor, ReportDataset, ReportSubset, Report, DataObject, DataArray, MetaObject, MetaArray, MetaCore, Links, RelationType, ResourceTypeGeneral, ContributorType, RelatedIdentifierType, TitleType, NameType, Certificate, ClientType, State, Source, Region, MemberType, OrganizationTypeEnum, OrganizationType, FocusAreaEnum, FocusArea, SourceId, RelationTypeId, ViewCount, DownloadCount, ReferenceCount, CitationCount, PartCount, PartOfCount, VersionCount, VersionOfCount, Attributes1, Provider, Consortium, Prefixes, Relationships, Client, Client1, ProviderPrefix, Prefix, Relationships1, ClientPrefix, Media, References, Citations, Parts, PartOf, Versions, VersionOf, Relationships2, Relationships3, Creator, Title, Contributor, Types, RelatedIdentifier, RelatedItemIdentifier, Creator1, Title1, Contributor1, RelatedItem, DoiPropertiesMetadata, DoiPropertiesOther, Subj, Obj, Relationships4, Attributes5, Event1, Clients, Providers, ClientPrefixes, ProviderPrefixes, Relationships5, Prefix1, Prefix2, Relationships6, ProviderPrefix1, Attributes8, Contacts, ConsortiumOrganizations, Relationships7, Provider4, Temporal, TotalsObject, Attributes3, Data, DoiDetailItem, Attributes4, DoiListItem]
model = st.sidebar.radio(
    label="Which Model to Use in Form",
    options=models,
    format_func=lambda x: x.__name__,
)
input_data = sp.pydantic_form(key="pydantic_form", model=model)

if not input_data:
    st.warning("Submit the Form to continue")
    st.stop()

st.code(repr(input_data))
st.json(input_data.json())


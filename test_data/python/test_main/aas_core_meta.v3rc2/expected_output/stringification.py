"""De-serialize enumerations from string representations."""


# This code has been automatically generated by aas-core-codegen.
# Do NOT edit or append.


from typing import (
    Mapping,
    Optional,
)

import aas_core3_rc02.types as aas_types


_MODELING_KIND_FROM_STR: Mapping[str, aas_types.ModelingKind] = {
    'Template': aas_types.ModelingKind.TEMPLATE,
    'Instance': aas_types.ModelingKind.INSTANCE,
}


def modeling_kind_from_str(
        text: str
) -> Optional[aas_types.ModelingKind]:
    """
    Parse :paramref:`text` as string representation
    of :py:class:`aas_core3_rc02.ModelingKind`.

    If :paramref:`text` is not a valid string representation of a literal
    of :py:class:`aas_core3_rc02.ModelingKind`, return ``None``.

    :param text: to be parsed
    :return:
        the corresponding literal of :py:class:`aas_core3_rc02.ModelingKind`
        or ``None``, if :paramref:`text` invalid.
    """
    return _MODELING_KIND_FROM_STR.get(text, None)


_QUALIFIER_KIND_FROM_STR: Mapping[str, aas_types.QualifierKind] = {
    'ValueQualifier': aas_types.QualifierKind.VALUE_QUALIFIER,
    'ConceptQualifier': aas_types.QualifierKind.CONCEPT_QUALIFIER,
    'TemplateQualifier': aas_types.QualifierKind.TEMPLATE_QUALIFIER,
}


def qualifier_kind_from_str(
        text: str
) -> Optional[aas_types.QualifierKind]:
    """
    Parse :paramref:`text` as string representation
    of :py:class:`aas_core3_rc02.QualifierKind`.

    If :paramref:`text` is not a valid string representation of a literal
    of :py:class:`aas_core3_rc02.QualifierKind`, return ``None``.

    :param text: to be parsed
    :return:
        the corresponding literal of :py:class:`aas_core3_rc02.QualifierKind`
        or ``None``, if :paramref:`text` invalid.
    """
    return _QUALIFIER_KIND_FROM_STR.get(text, None)


_ASSET_KIND_FROM_STR: Mapping[str, aas_types.AssetKind] = {
    'Type': aas_types.AssetKind.TYPE,
    'Instance': aas_types.AssetKind.INSTANCE,
}


def asset_kind_from_str(
        text: str
) -> Optional[aas_types.AssetKind]:
    """
    Parse :paramref:`text` as string representation
    of :py:class:`aas_core3_rc02.AssetKind`.

    If :paramref:`text` is not a valid string representation of a literal
    of :py:class:`aas_core3_rc02.AssetKind`, return ``None``.

    :param text: to be parsed
    :return:
        the corresponding literal of :py:class:`aas_core3_rc02.AssetKind`
        or ``None``, if :paramref:`text` invalid.
    """
    return _ASSET_KIND_FROM_STR.get(text, None)


_AAS_SUBMODEL_ELEMENTS_FROM_STR: Mapping[str, aas_types.AASSubmodelElements] = {
    'AnnotatedRelationshipElement': aas_types.AASSubmodelElements.ANNOTATED_RELATIONSHIP_ELEMENT,
    'BasicEventElement': aas_types.AASSubmodelElements.BASIC_EVENT_ELEMENT,
    'Blob': aas_types.AASSubmodelElements.BLOB,
    'Capability': aas_types.AASSubmodelElements.CAPABILITY,
    'DataElement': aas_types.AASSubmodelElements.DATA_ELEMENT,
    'Entity': aas_types.AASSubmodelElements.ENTITY,
    'EventElement': aas_types.AASSubmodelElements.EVENT_ELEMENT,
    'File': aas_types.AASSubmodelElements.FILE,
    'MultiLanguageProperty': aas_types.AASSubmodelElements.MULTI_LANGUAGE_PROPERTY,
    'Operation': aas_types.AASSubmodelElements.OPERATION,
    'Property': aas_types.AASSubmodelElements.PROPERTY,
    'Range': aas_types.AASSubmodelElements.RANGE,
    'ReferenceElement': aas_types.AASSubmodelElements.REFERENCE_ELEMENT,
    'RelationshipElement': aas_types.AASSubmodelElements.RELATIONSHIP_ELEMENT,
    'SubmodelElement': aas_types.AASSubmodelElements.SUBMODEL_ELEMENT,
    'SubmodelElementList': aas_types.AASSubmodelElements.SUBMODEL_ELEMENT_LIST,
    'SubmodelElementCollection': aas_types.AASSubmodelElements.SUBMODEL_ELEMENT_COLLECTION,
}


def aas_submodel_elements_from_str(
        text: str
) -> Optional[aas_types.AASSubmodelElements]:
    """
    Parse :paramref:`text` as string representation
    of :py:class:`aas_core3_rc02.AASSubmodelElements`.

    If :paramref:`text` is not a valid string representation of a literal
    of :py:class:`aas_core3_rc02.AASSubmodelElements`, return ``None``.

    :param text: to be parsed
    :return:
        the corresponding literal of :py:class:`aas_core3_rc02.AASSubmodelElements`
        or ``None``, if :paramref:`text` invalid.
    """
    return _AAS_SUBMODEL_ELEMENTS_FROM_STR.get(text, None)


_ENTITY_TYPE_FROM_STR: Mapping[str, aas_types.EntityType] = {
    'CoManagedEntity': aas_types.EntityType.CO_MANAGED_ENTITY,
    'SelfManagedEntity': aas_types.EntityType.SELF_MANAGED_ENTITY,
}


def entity_type_from_str(
        text: str
) -> Optional[aas_types.EntityType]:
    """
    Parse :paramref:`text` as string representation
    of :py:class:`aas_core3_rc02.EntityType`.

    If :paramref:`text` is not a valid string representation of a literal
    of :py:class:`aas_core3_rc02.EntityType`, return ``None``.

    :param text: to be parsed
    :return:
        the corresponding literal of :py:class:`aas_core3_rc02.EntityType`
        or ``None``, if :paramref:`text` invalid.
    """
    return _ENTITY_TYPE_FROM_STR.get(text, None)


_DIRECTION_FROM_STR: Mapping[str, aas_types.Direction] = {
    'input': aas_types.Direction.INPUT,
    'output': aas_types.Direction.OUTPUT,
}


def direction_from_str(
        text: str
) -> Optional[aas_types.Direction]:
    """
    Parse :paramref:`text` as string representation
    of :py:class:`aas_core3_rc02.Direction`.

    If :paramref:`text` is not a valid string representation of a literal
    of :py:class:`aas_core3_rc02.Direction`, return ``None``.

    :param text: to be parsed
    :return:
        the corresponding literal of :py:class:`aas_core3_rc02.Direction`
        or ``None``, if :paramref:`text` invalid.
    """
    return _DIRECTION_FROM_STR.get(text, None)


_STATE_OF_EVENT_FROM_STR: Mapping[str, aas_types.StateOfEvent] = {
    'on': aas_types.StateOfEvent.ON,
    'off': aas_types.StateOfEvent.OFF,
}


def state_of_event_from_str(
        text: str
) -> Optional[aas_types.StateOfEvent]:
    """
    Parse :paramref:`text` as string representation
    of :py:class:`aas_core3_rc02.StateOfEvent`.

    If :paramref:`text` is not a valid string representation of a literal
    of :py:class:`aas_core3_rc02.StateOfEvent`, return ``None``.

    :param text: to be parsed
    :return:
        the corresponding literal of :py:class:`aas_core3_rc02.StateOfEvent`
        or ``None``, if :paramref:`text` invalid.
    """
    return _STATE_OF_EVENT_FROM_STR.get(text, None)


_REFERENCE_TYPES_FROM_STR: Mapping[str, aas_types.ReferenceTypes] = {
    'GlobalReference': aas_types.ReferenceTypes.GLOBAL_REFERENCE,
    'ModelReference': aas_types.ReferenceTypes.MODEL_REFERENCE,
}


def reference_types_from_str(
        text: str
) -> Optional[aas_types.ReferenceTypes]:
    """
    Parse :paramref:`text` as string representation
    of :py:class:`aas_core3_rc02.ReferenceTypes`.

    If :paramref:`text` is not a valid string representation of a literal
    of :py:class:`aas_core3_rc02.ReferenceTypes`, return ``None``.

    :param text: to be parsed
    :return:
        the corresponding literal of :py:class:`aas_core3_rc02.ReferenceTypes`
        or ``None``, if :paramref:`text` invalid.
    """
    return _REFERENCE_TYPES_FROM_STR.get(text, None)


_KEY_TYPES_FROM_STR: Mapping[str, aas_types.KeyTypes] = {
    'FragmentReference': aas_types.KeyTypes.FRAGMENT_REFERENCE,
    'GlobalReference': aas_types.KeyTypes.GLOBAL_REFERENCE,
    'AnnotatedRelationshipElement': aas_types.KeyTypes.ANNOTATED_RELATIONSHIP_ELEMENT,
    'AssetAdministrationShell': aas_types.KeyTypes.ASSET_ADMINISTRATION_SHELL,
    'BasicEventElement': aas_types.KeyTypes.BASIC_EVENT_ELEMENT,
    'Blob': aas_types.KeyTypes.BLOB,
    'Capability': aas_types.KeyTypes.CAPABILITY,
    'ConceptDescription': aas_types.KeyTypes.CONCEPT_DESCRIPTION,
    'Identifiable': aas_types.KeyTypes.IDENTIFIABLE,
    'DataElement': aas_types.KeyTypes.DATA_ELEMENT,
    'Entity': aas_types.KeyTypes.ENTITY,
    'EventElement': aas_types.KeyTypes.EVENT_ELEMENT,
    'File': aas_types.KeyTypes.FILE,
    'MultiLanguageProperty': aas_types.KeyTypes.MULTI_LANGUAGE_PROPERTY,
    'Operation': aas_types.KeyTypes.OPERATION,
    'Property': aas_types.KeyTypes.PROPERTY,
    'Range': aas_types.KeyTypes.RANGE,
    'ReferenceElement': aas_types.KeyTypes.REFERENCE_ELEMENT,
    'Referable': aas_types.KeyTypes.REFERABLE,
    'RelationshipElement': aas_types.KeyTypes.RELATIONSHIP_ELEMENT,
    'Submodel': aas_types.KeyTypes.SUBMODEL,
    'SubmodelElement': aas_types.KeyTypes.SUBMODEL_ELEMENT,
    'SubmodelElementList': aas_types.KeyTypes.SUBMODEL_ELEMENT_LIST,
    'SubmodelElementCollection': aas_types.KeyTypes.SUBMODEL_ELEMENT_COLLECTION,
}


def key_types_from_str(
        text: str
) -> Optional[aas_types.KeyTypes]:
    """
    Parse :paramref:`text` as string representation
    of :py:class:`aas_core3_rc02.KeyTypes`.

    If :paramref:`text` is not a valid string representation of a literal
    of :py:class:`aas_core3_rc02.KeyTypes`, return ``None``.

    :param text: to be parsed
    :return:
        the corresponding literal of :py:class:`aas_core3_rc02.KeyTypes`
        or ``None``, if :paramref:`text` invalid.
    """
    return _KEY_TYPES_FROM_STR.get(text, None)


_DATA_TYPE_DEF_XSD_FROM_STR: Mapping[str, aas_types.DataTypeDefXSD] = {
    'xs:anyURI': aas_types.DataTypeDefXSD.ANY_URI,
    'xs:base64Binary': aas_types.DataTypeDefXSD.BASE_64_BINARY,
    'xs:boolean': aas_types.DataTypeDefXSD.BOOLEAN,
    'xs:date': aas_types.DataTypeDefXSD.DATE,
    'xs:dateTime': aas_types.DataTypeDefXSD.DATE_TIME,
    'xs:dateTimeStamp': aas_types.DataTypeDefXSD.DATE_TIME_STAMP,
    'xs:decimal': aas_types.DataTypeDefXSD.DECIMAL,
    'xs:double': aas_types.DataTypeDefXSD.DOUBLE,
    'xs:duration': aas_types.DataTypeDefXSD.DURATION,
    'xs:float': aas_types.DataTypeDefXSD.FLOAT,
    'xs:gDay': aas_types.DataTypeDefXSD.G_DAY,
    'xs:gMonth': aas_types.DataTypeDefXSD.G_MONTH,
    'xs:gMonthDay': aas_types.DataTypeDefXSD.G_MONTH_DAY,
    'xs:gYear': aas_types.DataTypeDefXSD.G_YEAR,
    'xs:gYearMonth': aas_types.DataTypeDefXSD.G_YEAR_MONTH,
    'xs:hexBinary': aas_types.DataTypeDefXSD.HEX_BINARY,
    'xs:string': aas_types.DataTypeDefXSD.STRING,
    'xs:time': aas_types.DataTypeDefXSD.TIME,
    'xs:dayTimeDuration': aas_types.DataTypeDefXSD.DAY_TIME_DURATION,
    'xs:yearMonthDuration': aas_types.DataTypeDefXSD.YEAR_MONTH_DURATION,
    'xs:integer': aas_types.DataTypeDefXSD.INTEGER,
    'xs:long': aas_types.DataTypeDefXSD.LONG,
    'xs:int': aas_types.DataTypeDefXSD.INT,
    'xs:short': aas_types.DataTypeDefXSD.SHORT,
    'xs:byte': aas_types.DataTypeDefXSD.BYTE,
    'xs:nonNegativeInteger': aas_types.DataTypeDefXSD.NON_NEGATIVE_INTEGER,
    'xs:positiveInteger': aas_types.DataTypeDefXSD.POSITIVE_INTEGER,
    'xs:unsignedLong': aas_types.DataTypeDefXSD.UNSIGNED_LONG,
    'xs:unsignedInt': aas_types.DataTypeDefXSD.UNSIGNED_INT,
    'xs:unsignedShort': aas_types.DataTypeDefXSD.UNSIGNED_SHORT,
    'xs:unsignedByte': aas_types.DataTypeDefXSD.UNSIGNED_BYTE,
    'xs:nonPositiveInteger': aas_types.DataTypeDefXSD.NON_POSITIVE_INTEGER,
    'xs:negativeInteger': aas_types.DataTypeDefXSD.NEGATIVE_INTEGER,
}


def data_type_def_xsd_from_str(
        text: str
) -> Optional[aas_types.DataTypeDefXSD]:
    """
    Parse :paramref:`text` as string representation
    of :py:class:`aas_core3_rc02.DataTypeDefXSD`.

    If :paramref:`text` is not a valid string representation of a literal
    of :py:class:`aas_core3_rc02.DataTypeDefXSD`, return ``None``.

    :param text: to be parsed
    :return:
        the corresponding literal of :py:class:`aas_core3_rc02.DataTypeDefXSD`
        or ``None``, if :paramref:`text` invalid.
    """
    return _DATA_TYPE_DEF_XSD_FROM_STR.get(text, None)


_DATA_TYPE_IEC_61360_FROM_STR: Mapping[str, aas_types.DataTypeIEC61360] = {
    'DATE': aas_types.DataTypeIEC61360.DATE,
    'STRING': aas_types.DataTypeIEC61360.STRING,
    'STRING_TRANSLATABLE': aas_types.DataTypeIEC61360.STRING_TRANSLATABLE,
    'INTEGER_MEASURE': aas_types.DataTypeIEC61360.INTEGER_MEASURE,
    'INTEGER_COUNT': aas_types.DataTypeIEC61360.INTEGER_COUNT,
    'INTEGER_CURRENCY': aas_types.DataTypeIEC61360.INTEGER_CURRENCY,
    'REAL_MEASURE': aas_types.DataTypeIEC61360.REAL_MEASURE,
    'REAL_COUNT': aas_types.DataTypeIEC61360.REAL_COUNT,
    'REAL_CURRENCY': aas_types.DataTypeIEC61360.REAL_CURRENCY,
    'BOOLEAN': aas_types.DataTypeIEC61360.BOOLEAN,
    'IRI': aas_types.DataTypeIEC61360.IRI,
    'IRDI': aas_types.DataTypeIEC61360.IRDI,
    'RATIONAL': aas_types.DataTypeIEC61360.RATIONAL,
    'RATIONAL_MEASURE': aas_types.DataTypeIEC61360.RATIONAL_MEASURE,
    'TIME': aas_types.DataTypeIEC61360.TIME,
    'TIMESTAMP': aas_types.DataTypeIEC61360.TIMESTAMP,
    'FILE': aas_types.DataTypeIEC61360.FILE,
    'HTML': aas_types.DataTypeIEC61360.HTML,
    'BLOB': aas_types.DataTypeIEC61360.BLOB,
}


def data_type_iec_61360_from_str(
        text: str
) -> Optional[aas_types.DataTypeIEC61360]:
    """
    Parse :paramref:`text` as string representation
    of :py:class:`aas_core3_rc02.DataTypeIEC61360`.

    If :paramref:`text` is not a valid string representation of a literal
    of :py:class:`aas_core3_rc02.DataTypeIEC61360`, return ``None``.

    :param text: to be parsed
    :return:
        the corresponding literal of :py:class:`aas_core3_rc02.DataTypeIEC61360`
        or ``None``, if :paramref:`text` invalid.
    """
    return _DATA_TYPE_IEC_61360_FROM_STR.get(text, None)


_LEVEL_TYPE_FROM_STR: Mapping[str, aas_types.LevelType] = {
    'Min': aas_types.LevelType.MIN,
    'Max': aas_types.LevelType.MAX,
    'Nom': aas_types.LevelType.NOM,
    'Typ': aas_types.LevelType.TYP,
}


def level_type_from_str(
        text: str
) -> Optional[aas_types.LevelType]:
    """
    Parse :paramref:`text` as string representation
    of :py:class:`aas_core3_rc02.LevelType`.

    If :paramref:`text` is not a valid string representation of a literal
    of :py:class:`aas_core3_rc02.LevelType`, return ``None``.

    :param text: to be parsed
    :return:
        the corresponding literal of :py:class:`aas_core3_rc02.LevelType`
        or ``None``, if :paramref:`text` invalid.
    """
    return _LEVEL_TYPE_FROM_STR.get(text, None)


# This code has been automatically generated by aas-core-codegen.
# Do NOT edit or append.

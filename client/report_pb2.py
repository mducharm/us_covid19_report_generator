# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: report.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='report.proto',
  package='report',
  syntax='proto3',
  serialized_options=b'Z\017./server/report',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0creport.proto\x12\x06report\"\x1d\n\rReportRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"8\n\nCurrencies\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06symbol\x18\x03 \x01(\t\"\xa6\x01\n\x0eReportResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nalpha2Code\x18\x02 \x01(\t\x12\x0f\n\x07\x63\x61pital\x18\x03 \x01(\t\x12\x11\n\tsubregion\x18\x04 \x01(\t\x12\x12\n\npopulation\x18\x05 \x01(\x05\x12\x12\n\nnativeName\x18\x06 \x01(\t\x12&\n\ncurrencies\x18\x07 \x03(\x0b\x32\x12.report.Currencies2K\n\x06Report\x12\x41\n\x0eGetReportAsCSV\x12\x15.report.ReportRequest\x1a\x16.report.ReportResponse\"\x00\x42\x11Z\x0f./server/reportb\x06proto3'
)




_REPORTREQUEST = _descriptor.Descriptor(
  name='ReportRequest',
  full_name='report.ReportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='report.ReportRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=53,
)


_CURRENCIES = _descriptor.Descriptor(
  name='Currencies',
  full_name='report.Currencies',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='report.Currencies.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='report.Currencies.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='report.Currencies.symbol', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=111,
)


_REPORTRESPONSE = _descriptor.Descriptor(
  name='ReportResponse',
  full_name='report.ReportResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='report.ReportResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alpha2Code', full_name='report.ReportResponse.alpha2Code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='capital', full_name='report.ReportResponse.capital', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subregion', full_name='report.ReportResponse.subregion', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='population', full_name='report.ReportResponse.population', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nativeName', full_name='report.ReportResponse.nativeName', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='currencies', full_name='report.ReportResponse.currencies', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=280,
)

_REPORTRESPONSE.fields_by_name['currencies'].message_type = _CURRENCIES
DESCRIPTOR.message_types_by_name['ReportRequest'] = _REPORTREQUEST
DESCRIPTOR.message_types_by_name['Currencies'] = _CURRENCIES
DESCRIPTOR.message_types_by_name['ReportResponse'] = _REPORTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReportRequest = _reflection.GeneratedProtocolMessageType('ReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTREQUEST,
  '__module__' : 'report_pb2'
  # @@protoc_insertion_point(class_scope:report.ReportRequest)
  })
_sym_db.RegisterMessage(ReportRequest)

Currencies = _reflection.GeneratedProtocolMessageType('Currencies', (_message.Message,), {
  'DESCRIPTOR' : _CURRENCIES,
  '__module__' : 'report_pb2'
  # @@protoc_insertion_point(class_scope:report.Currencies)
  })
_sym_db.RegisterMessage(Currencies)

ReportResponse = _reflection.GeneratedProtocolMessageType('ReportResponse', (_message.Message,), {
  'DESCRIPTOR' : _REPORTRESPONSE,
  '__module__' : 'report_pb2'
  # @@protoc_insertion_point(class_scope:report.ReportResponse)
  })
_sym_db.RegisterMessage(ReportResponse)


DESCRIPTOR._options = None

_REPORT = _descriptor.ServiceDescriptor(
  name='Report',
  full_name='report.Report',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=282,
  serialized_end=357,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetReportAsCSV',
    full_name='report.Report.GetReportAsCSV',
    index=0,
    containing_service=None,
    input_type=_REPORTREQUEST,
    output_type=_REPORTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REPORT)

DESCRIPTOR.services_by_name['Report'] = _REPORT

# @@protoc_insertion_point(module_scope)

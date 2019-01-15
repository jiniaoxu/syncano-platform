# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pkg/script/proto/script.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
    name='pkg/script/proto/script.proto',
    package='script',
    syntax='proto3',
    serialized_options=_b('Z+github.com/Syncano/codebox/pkg/script/proto'),
    serialized_pb=_b('\n\x1dpkg/script/proto/script.proto\x12\x06script\"\xeb\x03\n\nRunRequest\x12.\n\x04meta\x18\x01 \x01(\x0b\x32\x1e.script.RunRequest.MetaMessageH\x00\x12\x30\n\x05\x63hunk\x18\x02 \x01(\x0b\x32\x1f.script.RunRequest.ChunkMessageH\x00\x1a\x9e\x02\n\x0bMetaMessage\x12\x0f\n\x07runtime\x18\x01 \x01(\t\x12\x12\n\nsourceHash\x18\x02 \x01(\t\x12\x0e\n\x06userID\x18\x03 \x01(\t\x12>\n\x07options\x18\x05 \x01(\x0b\x32-.script.RunRequest.MetaMessage.OptionsMessage\x12\x13\n\x0b\x65nvironment\x18\x06 \x01(\t\x1a\x84\x01\n\x0eOptionsMessage\x12\x12\n\nentryPoint\x18\x01 \x01(\t\x12\x13\n\x0boutputLimit\x18\x02 \x01(\r\x12\x0f\n\x07timeout\x18\x03 \x01(\x03\x12\x0c\n\x04mCPU\x18\x07 \x01(\r\x12\x0c\n\x04\x61rgs\x18\x04 \x01(\x0c\x12\x0e\n\x06\x63onfig\x18\x05 \x01(\x0c\x12\x0c\n\x04meta\x18\x06 \x01(\x0c\x1aQ\n\x0c\x43hunkMessage\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x13\n\x0b\x63ontentType\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x42\x07\n\x05value\"\xba\x01\n\x13HTTPResponseMessage\x12\x12\n\nstatusCode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63ontentType\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\x12\x39\n\x07headers\x18\x04 \x03(\x0b\x32(.script.HTTPResponseMessage.HeadersEntry\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xa6\x01\n\x0bRunResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0e\n\x06stdout\x18\x02 \x01(\x0c\x12\x0e\n\x06stderr\x18\x03 \x01(\x0c\x12-\n\x08response\x18\x04 \x01(\x0b\x32\x1b.script.HTTPResponseMessage\x12\x0c\n\x04took\x18\x05 \x01(\x03\x12\x0e\n\x06\x63\x61\x63hed\x18\x06 \x01(\x08\x12\x0c\n\x04time\x18\x07 \x01(\x03\x12\x0e\n\x06weight\x18\x08 \x01(\r2B\n\x0cScriptRunner\x12\x32\n\x03Run\x12\x12.script.RunRequest\x1a\x13.script.RunResponse(\x01\x30\x01\x42-Z+github.com/Syncano/codebox/pkg/script/protob\x06proto3')
)




_RUNREQUEST_METAMESSAGE_OPTIONSMESSAGE = _descriptor.Descriptor(
    name='OptionsMessage',
    full_name='script.RunRequest.MetaMessage.OptionsMessage',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='entryPoint', full_name='script.RunRequest.MetaMessage.OptionsMessage.entryPoint', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='outputLimit', full_name='script.RunRequest.MetaMessage.OptionsMessage.outputLimit', index=1,
            number=2, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='timeout', full_name='script.RunRequest.MetaMessage.OptionsMessage.timeout', index=2,
            number=3, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='mCPU', full_name='script.RunRequest.MetaMessage.OptionsMessage.mCPU', index=3,
            number=7, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='args', full_name='script.RunRequest.MetaMessage.OptionsMessage.args', index=4,
            number=4, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='config', full_name='script.RunRequest.MetaMessage.OptionsMessage.config', index=5,
            number=5, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='meta', full_name='script.RunRequest.MetaMessage.OptionsMessage.meta', index=6,
            number=6, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=309,
    serialized_end=441,
)

_RUNREQUEST_METAMESSAGE = _descriptor.Descriptor(
    name='MetaMessage',
    full_name='script.RunRequest.MetaMessage',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='runtime', full_name='script.RunRequest.MetaMessage.runtime', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='sourceHash', full_name='script.RunRequest.MetaMessage.sourceHash', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='userID', full_name='script.RunRequest.MetaMessage.userID', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='options', full_name='script.RunRequest.MetaMessage.options', index=3,
            number=5, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='environment', full_name='script.RunRequest.MetaMessage.environment', index=4,
            number=6, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_RUNREQUEST_METAMESSAGE_OPTIONSMESSAGE, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=155,
    serialized_end=441,
)

_RUNREQUEST_CHUNKMESSAGE = _descriptor.Descriptor(
    name='ChunkMessage',
    full_name='script.RunRequest.ChunkMessage',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='script.RunRequest.ChunkMessage.name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='filename', full_name='script.RunRequest.ChunkMessage.filename', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='contentType', full_name='script.RunRequest.ChunkMessage.contentType', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data', full_name='script.RunRequest.ChunkMessage.data', index=3,
            number=4, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=443,
    serialized_end=524,
)

_RUNREQUEST = _descriptor.Descriptor(
    name='RunRequest',
    full_name='script.RunRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='meta', full_name='script.RunRequest.meta', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='chunk', full_name='script.RunRequest.chunk', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_RUNREQUEST_METAMESSAGE, _RUNREQUEST_CHUNKMESSAGE, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name='value', full_name='script.RunRequest.value',
            index=0, containing_type=None, fields=[]),
    ],
    serialized_start=42,
    serialized_end=533,
)


_HTTPRESPONSEMESSAGE_HEADERSENTRY = _descriptor.Descriptor(
    name='HeadersEntry',
    full_name='script.HTTPResponseMessage.HeadersEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='script.HTTPResponseMessage.HeadersEntry.key', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='value', full_name='script.HTTPResponseMessage.HeadersEntry.value', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=_b('8\001'),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=676,
    serialized_end=722,
)

_HTTPRESPONSEMESSAGE = _descriptor.Descriptor(
    name='HTTPResponseMessage',
    full_name='script.HTTPResponseMessage',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='statusCode', full_name='script.HTTPResponseMessage.statusCode', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='contentType', full_name='script.HTTPResponseMessage.contentType', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='content', full_name='script.HTTPResponseMessage.content', index=2,
            number=3, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='headers', full_name='script.HTTPResponseMessage.headers', index=3,
            number=4, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[_HTTPRESPONSEMESSAGE_HEADERSENTRY, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=536,
    serialized_end=722,
)


_RUNRESPONSE = _descriptor.Descriptor(
    name='RunResponse',
    full_name='script.RunResponse',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='code', full_name='script.RunResponse.code', index=0,
            number=1, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='stdout', full_name='script.RunResponse.stdout', index=1,
            number=2, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='stderr', full_name='script.RunResponse.stderr', index=2,
            number=3, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='response', full_name='script.RunResponse.response', index=3,
            number=4, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='took', full_name='script.RunResponse.took', index=4,
            number=5, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='cached', full_name='script.RunResponse.cached', index=5,
            number=6, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='time', full_name='script.RunResponse.time', index=6,
            number=7, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='weight', full_name='script.RunResponse.weight', index=7,
            number=8, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=725,
    serialized_end=891,
)

_RUNREQUEST_METAMESSAGE_OPTIONSMESSAGE.containing_type = _RUNREQUEST_METAMESSAGE
_RUNREQUEST_METAMESSAGE.fields_by_name['options'].message_type = _RUNREQUEST_METAMESSAGE_OPTIONSMESSAGE
_RUNREQUEST_METAMESSAGE.containing_type = _RUNREQUEST
_RUNREQUEST_CHUNKMESSAGE.containing_type = _RUNREQUEST
_RUNREQUEST.fields_by_name['meta'].message_type = _RUNREQUEST_METAMESSAGE
_RUNREQUEST.fields_by_name['chunk'].message_type = _RUNREQUEST_CHUNKMESSAGE
_RUNREQUEST.oneofs_by_name['value'].fields.append(
    _RUNREQUEST.fields_by_name['meta'])
_RUNREQUEST.fields_by_name['meta'].containing_oneof = _RUNREQUEST.oneofs_by_name['value']
_RUNREQUEST.oneofs_by_name['value'].fields.append(
    _RUNREQUEST.fields_by_name['chunk'])
_RUNREQUEST.fields_by_name['chunk'].containing_oneof = _RUNREQUEST.oneofs_by_name['value']
_HTTPRESPONSEMESSAGE_HEADERSENTRY.containing_type = _HTTPRESPONSEMESSAGE
_HTTPRESPONSEMESSAGE.fields_by_name['headers'].message_type = _HTTPRESPONSEMESSAGE_HEADERSENTRY
_RUNRESPONSE.fields_by_name['response'].message_type = _HTTPRESPONSEMESSAGE
DESCRIPTOR.message_types_by_name['RunRequest'] = _RUNREQUEST
DESCRIPTOR.message_types_by_name['HTTPResponseMessage'] = _HTTPRESPONSEMESSAGE
DESCRIPTOR.message_types_by_name['RunResponse'] = _RUNRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RunRequest = _reflection.GeneratedProtocolMessageType('RunRequest', (_message.Message,), dict(

    MetaMessage = _reflection.GeneratedProtocolMessageType('MetaMessage', (_message.Message,), dict(

        OptionsMessage = _reflection.GeneratedProtocolMessageType('OptionsMessage', (_message.Message,), dict(
            DESCRIPTOR = _RUNREQUEST_METAMESSAGE_OPTIONSMESSAGE,
            __module__ = 'pkg.script.proto.script_pb2'
            # @@protoc_insertion_point(class_scope:script.RunRequest.MetaMessage.OptionsMessage)
        ))
        ,
        DESCRIPTOR = _RUNREQUEST_METAMESSAGE,
        __module__ = 'pkg.script.proto.script_pb2'
        # @@protoc_insertion_point(class_scope:script.RunRequest.MetaMessage)
    ))
    ,

    ChunkMessage = _reflection.GeneratedProtocolMessageType('ChunkMessage', (_message.Message,), dict(
        DESCRIPTOR = _RUNREQUEST_CHUNKMESSAGE,
        __module__ = 'pkg.script.proto.script_pb2'
        # @@protoc_insertion_point(class_scope:script.RunRequest.ChunkMessage)
    ))
    ,
    DESCRIPTOR = _RUNREQUEST,
    __module__ = 'pkg.script.proto.script_pb2'
    # @@protoc_insertion_point(class_scope:script.RunRequest)
))
_sym_db.RegisterMessage(RunRequest)
_sym_db.RegisterMessage(RunRequest.MetaMessage)
_sym_db.RegisterMessage(RunRequest.MetaMessage.OptionsMessage)
_sym_db.RegisterMessage(RunRequest.ChunkMessage)

HTTPResponseMessage = _reflection.GeneratedProtocolMessageType('HTTPResponseMessage', (_message.Message,), dict(

    HeadersEntry = _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), dict(
        DESCRIPTOR = _HTTPRESPONSEMESSAGE_HEADERSENTRY,
        __module__ = 'pkg.script.proto.script_pb2'
        # @@protoc_insertion_point(class_scope:script.HTTPResponseMessage.HeadersEntry)
    ))
    ,
    DESCRIPTOR = _HTTPRESPONSEMESSAGE,
    __module__ = 'pkg.script.proto.script_pb2'
    # @@protoc_insertion_point(class_scope:script.HTTPResponseMessage)
))
_sym_db.RegisterMessage(HTTPResponseMessage)
_sym_db.RegisterMessage(HTTPResponseMessage.HeadersEntry)

RunResponse = _reflection.GeneratedProtocolMessageType('RunResponse', (_message.Message,), dict(
    DESCRIPTOR = _RUNRESPONSE,
    __module__ = 'pkg.script.proto.script_pb2'
    # @@protoc_insertion_point(class_scope:script.RunResponse)
))
_sym_db.RegisterMessage(RunResponse)


DESCRIPTOR._options = None
_HTTPRESPONSEMESSAGE_HEADERSENTRY._options = None

_SCRIPTRUNNER = _descriptor.ServiceDescriptor(
    name='ScriptRunner',
    full_name='script.ScriptRunner',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=893,
    serialized_end=959,
    methods=[
        _descriptor.MethodDescriptor(
            name='Run',
            full_name='script.ScriptRunner.Run',
            index=0,
            containing_service=None,
            input_type=_RUNREQUEST,
            output_type=_RUNRESPONSE,
            serialized_options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_SCRIPTRUNNER)

DESCRIPTOR.services_by_name['ScriptRunner'] = _SCRIPTRUNNER

# @@protoc_insertion_point(module_scope)

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apis/dm_api_search/search.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1f\x61pis/dm_api_search/search.proto"c\n\rSearchRequest\x12\r\n\x05query\x18\x01 \x01(\t\x12\'\n\x0csearchAcross\x18\x02 \x03(\x0e\x32\x11.SearchEntityType\x12\x0c\n\x04skip\x18\x03 \x01(\x05\x12\x0c\n\x04size\x18\x04 \x01(\x05"\xd6\x01\n\x0eSearchResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x34\n\x08\x65ntities\x18\x02 \x03(\x0b\x32".SearchResponse.SearchResultEntity\x1a\x7f\n\x12SearchResultEntity\x12\n\n\x02id\x18\x01 \x01(\t\x12\x1f\n\x04type\x18\x02 \x01(\x0e\x32\x11.SearchEntityType\x12\x12\n\nfoundTitle\x18\x03 \x01(\t\x12\x15\n\roriginalTitle\x18\x04 \x01(\t\x12\x11\n\tfoundText\x18\x05 \x01(\t*W\n\x10SearchEntityType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0b\x46ORUM_TOPIC\x10\x01\x12\x11\n\rFORUM_COMMENT\x10\x02\x12\x08\n\x04GAME\x10\x03\x12\x08\n\x04USER\x10\x04\x32\x39\n\x0cSearchEngine\x12)\n\x06Search\x12\x0e.SearchRequest\x1a\x0f.SearchResponseB\x1a\xaa\x02\x17\x44M.Services.Search.Grpcb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "apis.dm_api_search.search_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\252\002\027DM.Services.Search.Grpc"
    _SEARCHENTITYTYPE._serialized_start = 353
    _SEARCHENTITYTYPE._serialized_end = 440
    _SEARCHREQUEST._serialized_start = 35
    _SEARCHREQUEST._serialized_end = 134
    _SEARCHRESPONSE._serialized_start = 137
    _SEARCHRESPONSE._serialized_end = 351
    _SEARCHRESPONSE_SEARCHRESULTENTITY._serialized_start = 224
    _SEARCHRESPONSE_SEARCHRESULTENTITY._serialized_end = 351
    _SEARCHENGINE._serialized_start = 442
    _SEARCHENGINE._serialized_end = 499
# @@protoc_insertion_point(module_scope)

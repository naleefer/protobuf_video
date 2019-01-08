# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: video.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='video.proto',
  package='video',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0bvideo.proto\x12\x05video\"m\n\x05Image\x12\x11\n\ttimestamp\x18\x01 \x02(\x03\x12\x0c\n\x04\x63ols\x18\x02 \x02(\x05\x12\x0c\n\x04rows\x18\x03 \x02(\x05\x12\x10\n\x08\x63hannels\x18\x04 \x02(\x05\x12\x0e\n\x06\x66ormat\x18\x05 \x02(\t\x12\x13\n\x0bimage_bytes\x18\x06 \x02(\x0c\"%\n\x05Video\x12\x1c\n\x06\x66rames\x18\x01 \x03(\x0b\x32\x0c.video.Image')
)




_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='video.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='video.Image.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cols', full_name='video.Image.cols', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rows', full_name='video.Image.rows', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channels', full_name='video.Image.channels', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='format', full_name='video.Image.format', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_bytes', full_name='video.Image.image_bytes', index=5,
      number=6, type=12, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=131,
)


_VIDEO = _descriptor.Descriptor(
  name='Video',
  full_name='video.Video',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frames', full_name='video.Video.frames', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=170,
)

_VIDEO.fields_by_name['frames'].message_type = _IMAGE
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['Video'] = _VIDEO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), dict(
  DESCRIPTOR = _IMAGE,
  __module__ = 'video_pb2'
  # @@protoc_insertion_point(class_scope:video.Image)
  ))
_sym_db.RegisterMessage(Image)

Video = _reflection.GeneratedProtocolMessageType('Video', (_message.Message,), dict(
  DESCRIPTOR = _VIDEO,
  __module__ = 'video_pb2'
  # @@protoc_insertion_point(class_scope:video.Video)
  ))
_sym_db.RegisterMessage(Video)


# @@protoc_insertion_point(module_scope)

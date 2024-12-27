import uuid

from construct import Adapter, Byte


EPOCH_AS_FILETIME = 116444736000000000  # January 1, 1970 as MS file time
HUNDREDS_OF_NANOSECONDS = 10000000


class GUIDAdapter(Adapter):
    def _decode(self, obj, context, path):
        guid_obj = uuid.UUID(bytes=bytes(obj))
        return str(guid_obj)

    def _encode(self, obj, context, path):
        guid_obj = uuid.UUID(obj)
        return guid_obj.bytes


GUID = GUIDAdapter(Byte[16])


# TODO: write `FILETIME` structure adapter

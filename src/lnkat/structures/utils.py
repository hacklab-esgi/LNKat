import uuid
import datetime
import pytz

from construct import Adapter, Byte, Int64un


EPOCH_AS_FILETIME = 116444736000000000  # January 1, 1970 as MS file time
HUNDREDS_OF_NANOSECONDS = 10000000


class GUIDAdapter(Adapter):
    def _decode(self, obj, context, path):
        guid_obj = uuid.UUID(bytes=bytes(obj))
        return str(guid_obj)

    def _encode(self, obj, context, path):
        guid_obj = uuid.UUID(obj)
        return guid_obj.bytes


class FileTimeAdapter(Adapter):
    def _decode(self, obj, context, path):
        # FILETIME is in 100-nanosecond intervals since Jan 1, 1601 UTC
        # Convert to seconds
        seconds = obj / 10000000

        # Convert to a datetime object
        datetime_obj = datetime.datetime(1601, 1, 1) + datetime.timedelta(
            seconds=seconds
        )

        return datetime_obj.isoformat()

    def _encode(self, obj, context, path):
        datetime_obj = datetime.datetime.fromisoformat(obj)

        # Get the number of seconds since Jan 1, 1601 UTC
        epoch = datetime.datetime(1601, 1, 1, tzinfo=pytz.utc)
        seconds = (datetime_obj - epoch).total_seconds()

        # FILETIME is in 100-nanosecond intervals
        filetime = int(seconds * 10000000)
        return filetime


GUID = GUIDAdapter(Byte[16])
FileTime = FileTimeAdapter(Int64un)

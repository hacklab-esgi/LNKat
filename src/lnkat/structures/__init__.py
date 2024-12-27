from construct import Struct, Bytes, Int16ul, If, this

from .shell_lnk_header import ShellLinkHeader
from .linktarget_idlist import LinkTargetIDList


StringData = Struct("CountCharacters" / Int16ul, "String" / Bytes(this.CountCharacters))

ShellLink = Struct(
    "ShellLinkHeader" / ShellLinkHeader,
    "LinkTargetIDList"
    / If(this.ShellLinkHeader.LinkFlags.HasLinkTargetIDList, LinkTargetIDList),
    # "RELATIVE_PATH" / If(this.ShellLinkHeader.LinkFlags.HasRelativePath, StringData),
    # "ICON_LOCATION" / If(this.ShellLinkHeader.LinkFlags.HasIconLocation, StringData)
)

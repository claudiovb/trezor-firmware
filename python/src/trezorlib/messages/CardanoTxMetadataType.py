# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .CardanoCatalystRegistrationParametersType import CardanoCatalystRegistrationParametersType

if __debug__:
    try:
        from typing import Dict, List, Optional  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeCardanoMetadataType = Literal[0]
    except ImportError:
        pass


class CardanoTxMetadataType(p.MessageType):

    def __init__(
        self,
        *,
        type: EnumTypeCardanoMetadataType,
        catalyst_registration_parameters: Optional[CardanoCatalystRegistrationParametersType] = None,
    ) -> None:
        self.type = type
        self.catalyst_registration_parameters = catalyst_registration_parameters

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('type', p.EnumType("CardanoMetadataType", (0,)), p.FLAG_REQUIRED),
            2: ('catalyst_registration_parameters', CardanoCatalystRegistrationParametersType, None),
        }

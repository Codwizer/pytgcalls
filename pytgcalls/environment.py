from .exceptions import TooOldTelethonVersion
from .version_manager import VersionManager


class Environment:
    def __init__(
        self,
        min_telethon_version: str,
        client_name: str,
    ):
        self._REQUIRED_TELETHON_VERSION = min_telethon_version
        self._client_name = client_name

    def check_environment(self):
        if self._client_name == "telethon":
            import telethon

            if VersionManager.version_tuple(
                telethon.__version__,
            ) < VersionManager.version_tuple(
                self._REQUIRED_TELETHON_VERSION,
            ):
                raise TooOldTelethonVersion(
                    self._REQUIRED_TELETHON_VERSION,
                    telethon.__version__,
                )

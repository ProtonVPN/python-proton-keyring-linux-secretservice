"""Secret Service Keyring backend."""

import logging
from proton.keyring_linux.core import KeyringBackendLinux

logger = logging.getLogger(__name__)


# pylint: disable=too-few-public-methods
class KeyringBackendLinuxSecretService(KeyringBackendLinux):
    """Implements the Secret Service keyring backend."""
    @classmethod
    def _get_priority(cls):
        return 5.

    @classmethod
    def _validate(cls):
        try:
            # pylint: disable=import-outside-toplevel
            from keyring.backends import SecretService
            return cls._is_backend_working(SecretService.Keyring())
        except ModuleNotFoundError:
            logger.debug("Gnome-Keyring module not found")
            return False

    def __init__(self):
        # pylint: disable=import-outside-toplevel
        from keyring.backends import SecretService
        super().__init__(SecretService.Keyring())

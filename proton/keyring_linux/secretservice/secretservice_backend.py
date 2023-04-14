"""Module for Linux Secret Service Keyring backend.


Copyright (c) 2023 Proton AG

This file is part of Proton VPN.

Proton VPN is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Proton VPN is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ProtonVPN.  If not, see <https://www.gnu.org/licenses/>.
"""

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

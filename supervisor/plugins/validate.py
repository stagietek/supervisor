"""Validate functions."""

import voluptuous as vol

from supervisor.plugins.const import ATTR_FALLBACK

from ..const import ATTR_ACCESS_TOKEN, ATTR_IMAGE, ATTR_SERVERS, ATTR_VERSION
from ..validate import dns_server_list, docker_image, token, version_tag

# pylint: disable=no-value-for-parameter
SCHEMA_DNS_CONFIG = vol.Schema(
    {
        vol.Optional(ATTR_VERSION): version_tag,
        vol.Optional(ATTR_IMAGE): docker_image,
        vol.Optional(ATTR_SERVERS, default=list): dns_server_list,
        vol.Optional(ATTR_FALLBACK, default=True): vol.Boolean(),
    },
    extra=vol.REMOVE_EXTRA,
)


SCHEMA_AUDIO_CONFIG = vol.Schema(
    {vol.Optional(ATTR_VERSION): version_tag, vol.Optional(ATTR_IMAGE): docker_image},
    extra=vol.REMOVE_EXTRA,
)


SCHEMA_CLI_CONFIG = vol.Schema(
    {
        vol.Optional(ATTR_VERSION): version_tag,
        vol.Optional(ATTR_IMAGE): docker_image,
        vol.Optional(ATTR_ACCESS_TOKEN): token,
    },
    extra=vol.REMOVE_EXTRA,
)


SCHEMA_MULTICAST_CONFIG = vol.Schema(
    {vol.Optional(ATTR_VERSION): version_tag, vol.Optional(ATTR_IMAGE): docker_image},
    extra=vol.REMOVE_EXTRA,
)


SCHEMA_OBSERVER_CONFIG = vol.Schema(
    {
        vol.Optional(ATTR_VERSION): version_tag,
        vol.Optional(ATTR_IMAGE): docker_image,
        vol.Optional(ATTR_ACCESS_TOKEN): token,
    },
    extra=vol.REMOVE_EXTRA,
)

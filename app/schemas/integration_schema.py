from enum import Enum


class IntegrationType(str, Enum):
    modrinth = "modrinth"
    curseforge = "curseforge"
    cdn = "cdn"

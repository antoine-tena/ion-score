"""The installed version of ion-score, said in what it reports."""

from importlib.metadata import PackageNotFoundError, version

DISTRIBUTION = "ion-score"
UNKNOWN = "unknown"


def installed_version() -> str:
    try:
        return version(DISTRIBUTION)
    except PackageNotFoundError:
        return UNKNOWN

import re

from lib.settings import HTTP_HEADER

__product__ = "Sucuri Firewall (Sucuri Cloudproxy)"


def detect(content, **kwargs):
    content = str(content)
    headers = kwargs.get("headers", None)
    detection_schema = (
        re.compile(r"access.denied.-.sucuri.website.firewall", re.I),
        re.compile(r"sucuri.webSite.firewall.-.cloudProxy.-.access.denied", re.I),
        re.compile(r"questions\?.+cloudproxy@sucuri\.net", re.I),
        re.compile(r"http(s)?.\/\/(cdn|supportx.)?sucuri(.net|com)?", re.I)
    )
    for detection in detection_schema:
        if detection.search(content) is not None:
            return True
    if headers.get("X-Sucuri-Block", None) is not None:
        return True
    if headers.get(HTTP_HEADER.SERVER, "") == "Sucuri/Cloudproxy":
        return True

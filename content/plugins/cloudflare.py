import re

from lib.settings import HTTP_HEADER


__product__ = "CloudFlare Web Application Firewall (CloudFlare)"


def detect(content, **kwargs):
    headers = kwargs.get("headers", None)
    content = str(content)
    detection_schemas = (
        re.compile(r"cloudflare.ray.id.|var.cloudflare.", re.I),
        re.compile(r"cloudflare.nginx", re.I),
        re.compile(r"..cfduid=([a-z0-9]{43})?", re.I),
        re.compile(r"cf[-|_]ray(..)?([0-9a-f]{16})?[-|_]?(dfw|iad)?", re.I),
        re.compile(r"<.+>attention.required\S.\S.cloudflare<.+.>", re.I),
        re.compile(r"http(s)?.//report.uri.cloudflare.com(/cdn.cgi(.beacon/expect.ct)?)?", re.I)
    )
    for detection in detection_schemas:
        if detection.search(content) is not None:
            return True
        if detection.search(headers.get(HTTP_HEADER.SERVER, "")) is not None:
            return True
        if detection.search(headers.get(HTTP_HEADER.COOKIE, "")) is not None:
            return True
        if detection.search(headers.get(HTTP_HEADER.SET_COOKIE, "")) is not None:
            return True
        if detection.search(headers.get(HTTP_HEADER.CF_RAY, "")) is not None:
            return True
        if detection.search(headers.get(HTTP_HEADER.EXPECT_CT, "")) is not None:
            return True

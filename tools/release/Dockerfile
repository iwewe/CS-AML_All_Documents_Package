# CS-AML specification release toolchain (pinned).
# pandoc 3.10 + XeTeX (TeX Live 2026) on Debian 12; DejaVu fonts (core in base image, oblique variants from fonts-dejavu-extra).
FROM pandoc/latex:3.10.0.0-debian@sha256:391dfdd1a31087c444d30bd5ead84c34ecf0dc1937723c37bf7b67a52fcc8e2d
RUN apt-get update \
 && apt-get install -y --no-install-recommends python3 python3-docx poppler-utils fonts-dejavu-extra \
 && rm -rf /var/lib/apt/lists/* \
 && tlmgr update --self \
 && tlmgr install fvextra lineno pdflscape lastpage
ENTRYPOINT []

from __future__ import annotations

import os
import platform
import shutil
from dataclasses import asdict, dataclass


@dataclass
class SystemInfo:
    hostname: str
    operating_system: str
    kernel: str
    architecture: str
    processor: str
    cpu_count: int | None
    total_disk_gb: float
    free_disk_gb: float


def get_system_info() -> dict:
    """Return basic read-only information about the host system."""

    disk = shutil.disk_usage("/")

    info = SystemInfo(
        hostname=platform.node(),
        operating_system=platform.platform(),
        kernel=platform.release(),
        architecture=platform.machine(),
        processor=platform.processor() or "Unknown",
        cpu_count=os.cpu_count(),
        total_disk_gb=round(disk.total / (1024**3), 2),
        free_disk_gb=round(disk.free / (1024**3), 2),
    )

    return asdict(info)


if __name__ == "__main__":
    for key, value in get_system_info().items():
        print(f"{key}: {value}")

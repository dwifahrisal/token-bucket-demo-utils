#!/usr/bin/env python3
"""A minimal token bucket rate limiter, written for readability."""

import time


class TokenBucket:
    def __init__(self, rate: float, capacity: int):
        self.rate = rate          # tokens added per second
        self.capacity = capacity  # max burst size
        self.tokens = float(capacity)
        self.last = time.monotonic()

    def allow(self) -> bool:
        now = time.monotonic()
        self.tokens = min(self.capacity, self.tokens + (now - self.last) * self.rate)
        self.last = now
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False


def main() -> None:
    bucket = TokenBucket(rate=2, capacity=5)  # 2 req/s, burst of 5
    for i in range(12):
        ok = bucket.allow()
        print(f"req {i + 1:2}: {'ALLOWED' if ok else 'DENIED'}")
        time.sleep(0.3)


if __name__ == "__main__":
    main()

"""Lamina-style reusable background execution for blocking desktop work."""

from __future__ import annotations

import threading
from concurrent.futures import Future, ThreadPoolExecutor
from typing import Callable

from perfect_prompts.contracts.ports import CancellationTokenPort


class CancellationToken:
    def __init__(self, event: threading.Event):
        self._event = event

    @property
    def is_cancelled(self) -> bool:
        return self._event.is_set()


class TaskHandle:
    def __init__(self, future: Future, event: threading.Event):
        self._future = future
        self._event = event

    @property
    def is_done(self) -> bool:
        return self._future.done()

    def cancel(self) -> None:
        self._event.set()


class ThreadPoolTaskRunner:
    def __init__(self, max_workers: int = 2):
        self._executor = ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="perfect-prompts")

    def submit(self, work: Callable[[CancellationTokenPort], object], done: Callable[[object | None, BaseException | None], None]) -> TaskHandle:
        event = threading.Event()
        token = CancellationToken(event)
        future = self._executor.submit(work, token)

        def completed(future_: Future) -> None:
            try:
                done(future_.result(), None)
            except BaseException as error:
                done(None, error)

        future.add_done_callback(completed)
        return TaskHandle(future, event)

    def shutdown(self, wait: bool = True) -> None:
        self._executor.shutdown(wait=wait, cancel_futures=False)

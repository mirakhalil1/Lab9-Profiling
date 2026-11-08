
import time
import unittest
import memory_profiler

from profiler import (
    slow_function,
    fast_function,
    memory_intensive_function,
)


class TestProfiler(unittest.TestCase):

    def time_function(self, func):
        start_time = time.perf_counter()
        result = func()
        end_time = time.perf_counter()
        return end_time - start_time, result

    def test_slow_function(self):
        duration, result = self.time_function(slow_function)

        print(f"\nslow_function: {duration:.4f} seconds")

        self.assertGreaterEqual(duration, 2)
        self.assertEqual(result, sum(i ** 2 for i in range(10000)))

    def test_fast_function(self):
        duration, result = self.time_function(fast_function)

        print(f"\nfast_function: {duration:.6f} seconds")

        self.assertLess(duration, 1)
        self.assertEqual(result, sum(i ** 2 for i in range(100)))

    def test_memory_intensive_function(self):
        memory_before = memory_profiler.memory_usage()[0]

        duration, result = self.time_function(
            memory_intensive_function
        )

        memory_after = memory_profiler.memory_usage()[0]

        print(f"\nmemory_intensive_function: {duration:.4f} seconds")
        print(f"Memory before: {memory_before:.2f} MiB")
        print(f"Memory after: {memory_after:.2f} MiB")

        self.assertEqual(
            result,
            sum(i ** 2 for i in range(10000000))
        )


if __name__ == "__main__":
    unittest.main()

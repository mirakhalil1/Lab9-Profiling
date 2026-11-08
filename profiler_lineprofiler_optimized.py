
from line_profiler import LineProfiler

from profiler_optimized import (
    slow_function,
    optimized_fast_function,
    memory_intensive_function,
    main,
)


def profile_main():
    profiler = LineProfiler()

    profiler.add_function(slow_function)
    profiler.add_function(optimized_fast_function)
    profiler.add_function(memory_intensive_function)

    profiler.runcall(main)
    profiler.print_stats()


if __name__ == "__main__":
    profile_main()

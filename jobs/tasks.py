from jobs.models import Job


def add(x: int, y: int) -> int:
    result: int = x + y
    print(f"{x} + {y} is {result}")
    print(Job.objects.all())
    return result

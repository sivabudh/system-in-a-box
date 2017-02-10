from secrets import randbelow

import django_rq
from django.http import HttpResponse

from jobs import tasks


def index(request):
    # 2 random numbers
    first_random_number: int = randbelow(10)
    second_random_number: int = randbelow(10)

    # Create a task
    queue = django_rq.get_queue('default')
    queue.enqueue(tasks.add, first_random_number, second_random_number)

    return HttpResponse(f"Adding {first_random_number} with {second_random_number} will yield which number? Find out in the RQ terminal!")

from platforms import step

from cores.utils import TimeUtil


@step('[API][Common] Sleep <time_in_ms> seconds')
def sleep(time_in_ms: str):
    TimeUtil.sleep(float(time_in_ms))

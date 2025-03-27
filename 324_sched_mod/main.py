# 324. sched
#
# sched.scheduler is an in-process timer queue. enterabs and enter schedule events. run()
# blocks. For real jobs use cron, celery, or asyncio.
#
# Run: python 324_sched_mod/main.py

import sched, time
s = sched.scheduler(time.time, time.sleep)
out = []
s.enter(0, 1, out.append, argument=("tick",))
s.run()
print(out)

import time
import webbrowser


total_breaks = 3
break_count = 0
before = time.ctime()

print "This program started on "+before
while (break_count < total_breaks):
  time.sleep(10)
  webbrowser.open ("http://www.youtube.com/watch?v=K9Ai7uNjp0I")
  break_count = break_count + 1

after = time.ctime()
duration = after - before
print "This program finished on "+after
print "Duration ="+duration

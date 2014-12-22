#from datetime import date
#from datetime import datetime

#today = datetime.today()

#today_writed = date(2014,12,22)
#birth_date = date(1985,05,17)

 
#diff = today_writed - birth_date
#print diff.days

#Still need to understand how to transform the datetime.today only on days to be possible to do the difference

    

import datetime
from datetime import date

today = datetime.date.today()
birth_date = date(1985,05,17)

diff = today - birth_date
print diff.days

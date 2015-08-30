#import syslog

# If openlog() has not been called prior to the call to syslog(),
# openlog() will be called with no arguments
syslog.syslog('Processing started')

error = True

if error:
  syslog.syslog(syslog.LOG_ERR, 'Processing started')


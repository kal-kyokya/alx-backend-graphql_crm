INSTALLED_APPS += ['django_crontab']

CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartBeat'),
]

# Enable logging to a different file
# CRONTAB_COMMAND_PREFIX = 'PATH=/usr/bin:/bin:/usr/sbin:/sbin'
# Optional for env clarity

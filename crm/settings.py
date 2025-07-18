from celery.schedules import crontab


INSTALLED_APPS += ['django_crontab']

CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartBeat'),
    ('0 */12 * * *', 'crm.cron.update_low_stock'),
]

# Enable logging to a different file
# CRONTAB_COMMAND_PREFIX = 'PATH=/usr/bin:/bin:/usr/sbin:/sbin'
# Optional for env clarity

INSTALLED_APPS += ['django_celery_beat']

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

CELERY_BEAT_SCHEDULE = {
    'generate-crm-report': {
        'task': 'crm.tasks.generate_crm_report',
        'schedule': crontab(day_of_week='mon', hour=6, minute=0)
    }
}

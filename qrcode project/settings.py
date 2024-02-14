# Add these lines at the end.


import os
STATIC_URL = '/static/'

# For development only
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
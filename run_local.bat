@echo off
echo Starting Korean Cars Shop - Local Development Server
echo.
echo Setting environment variables...
set ENVIRONMENT=development
set DEBUG=True
echo.
echo Running Django development server...
python manage.py runserver
pause 
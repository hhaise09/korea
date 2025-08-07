#!/usr/bin/env python
"""
Local development server runner
"""
import os
import sys
import subprocess

def main():
    """Run the local development server"""
    # Set environment variables for local development
    os.environ.setdefault('ENVIRONMENT', 'development')
    os.environ.setdefault('DEBUG', 'True')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'korean_cars_shop.settings')
    
    # Run Django development server
    from django.core.management import execute_from_command_line
    
    # Add runserver command if no arguments provided
    if len(sys.argv) == 1:
        sys.argv.append('runserver')
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main() 
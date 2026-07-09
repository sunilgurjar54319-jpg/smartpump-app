[app]

# (string) Title of your application
title = SmartPump

# (string) Package name
package.name = smartpump

# (string) Package domain
package.domain = org.smartpump

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json

# (string) Application version
version = 1.0

# SABSE BADA FIX: Yahan se ==2.3.0 hata diya hai taaki Kivy compile ho sake
requirements = python3,kivy,requests

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# =============================================================================
# Android specific configuration
# =============================================================================

# (int) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow root execution
android.allow_root = 1

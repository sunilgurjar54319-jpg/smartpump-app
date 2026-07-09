[app]

# (string) Title of your application
title = SmartPump

# (string) Package name
package.name = smartpump

# (string) Package domain (needed for android packaging)
package.domain = org.smartpump

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (string) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy,requests

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# =============================================================================
# Android specific configuration
# =============================================================================

# (int) Android API to use (GitHub ke built-in SDK se match karne ke liye)
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow root execution
android.allow_root = 1

[app]

title = PENA AI
package.name = pena
package.domain = org.pena

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 0.1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,RECORD_AUDIO

android.minapi = 23
android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1

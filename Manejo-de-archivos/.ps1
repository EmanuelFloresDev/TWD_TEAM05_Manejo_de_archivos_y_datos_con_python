# 1. Crear directorios
New-Item -ItemType Directory -Path "app/static/css" -Force | Out-Null
New-Item -ItemType Directory -Path "app/static/js" -Force | Out-Null
New-Item -ItemType Directory -Path "app/templates" -Force | Out-Null

# 2. Crear archivos dentro de las carpetas
New-Item -ItemType File -Path "app/static/css/input.css" -Force | Out-Null
New-Item -ItemType File -Path "app/static/css/output.css" -Force | Out-Null
New-Item -ItemType File -Path "app/static/js/style.js" -Force | Out-Null
New-Item -ItemType File -Path "app/templates/base.html" -Force | Out-Null
New-Item -ItemType File -Path "app/templates/index.html" -Force | Out-Null

# 3. Crear archivos de la raíz de 'app'
New-Item -ItemType File -Path "app/__init__.py" -Force | Out-Null

# 4. Crear archivos de la raíz del proyecto
New-Item -ItemType File -Path "app.py" -Force | Out-Null
New-Item -ItemType File -Path "package.json" -Force | Out-Null
New-Item -ItemType File -Path "requirements.txt" -Force | Out-Null
New-Item -ItemType File -Path "tailwind.config.js" -Force | Out-Null

Write-Host "Estructura creada con exito." -ForegroundColor Green

# Comando para ejecutar este archivo .ps1
# .\crear_estructura.ps1
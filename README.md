# setting_netbird
Прописано как установить vpn netbird и добавлено как создать службу sustemd для автозапуска скрипта python для перезагрузки vpn


https://netbird.io/
Установить: curl -fsSL https://pkgs.netbird.io/install.sh | sh
Запустить: netbird up
Если после перезапуска системы netbird выдает ошибку то:
- sudo netbird service uninstall
- sudo netbird service install
- sudo netbird service start

Для автоматического перезапуска netbird необходимо через демон systemd установить автозапуск скрипта python (script.py)
Для настройки systemd
Создать сервис script.service (sudo nano /etc/systemd/system/script.service)
=======================================================================
[Unit]

Description=Python Script Service
After=network.target

[Service]

ExecStart=/usr/bin/python3 /полный/путь/к/вашему_скрипту.py
WorkingDirectory=/полный/путь/к/директории_со_скриптом
Restart=always
User=ваш_пользователь
StandardOutput=append:/полный/путь/к/output.log
StandardError=append:/полный/путь/к/error.log

[Install]

WantedBy=multi-user.target
=======================================================================

Далее вбить команды:
- sudo systemctl daemon-reload          // Обновление конфигурации systemd
- sudo systemctl enable script.service  // Включить авозапуска службы при запуске системы
- sudo systemctl start script.service   // Запуск службы сейчас
- systemctl status script.service       // Проверка статуса
- sudo systemctl stop script.service    // Остановка службы
- sudo systemctl restart script.service // Перезапуск службы

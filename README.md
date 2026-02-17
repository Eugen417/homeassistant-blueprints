# 🏠 Home Assistant Blueprints

Коллекция моих блупринтов (шаблонов автоматизаций) и скриптов для Home Assistant.
Здесь собраны решения для мониторинга батареек, "душевных" уведомлений о погоде и учета коммунальных услуг.

---

## 📋 Список блупринтов / Available Blueprints

| Blueprint | Описание / Description | Установка / Install |
| :--- | :--- | :---: |
| **Battery Report (EN)** | **[EN]** A blueprint to generate detailed battery status reports using the **Battery Notes** integration. It categorizes devices by battery level and type for easy monitoring. | [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint URL.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FEugen417%2Fhomeassistant-blueprints%2Fblob%2Fmain%2FBattery_Report_V3.4_EN.yaml) |
| **Battery Report (RU)** | **[RU]** Генерация подробного отчета о состоянии батареек (версия 3.4). Удобно для отслеживания устройств, требующих замены питания. Работает в паре с интеграцией **Battery Notes**. | [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint URL.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FEugen417%2Fhomeassistant-blueprints%2Fblob%2Fmain%2FBattery_Report_V3.4_RU.yaml) |
| **Battery+ TG Report** | **[RU]** Продвинутый скрипт (Battery+ / Батарея+) для отправки отчетов в Telegram. Группирует устройства по типам и статусу (отдельно "на замену", отдельно "на зарядку"). | [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint URL.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FEugen417%2Fhomeassistant-blueprints%2Fblob%2Fmain%2Fscript_battery_plus_tg_push_report.yaml) |
| **Weather Notifications** | **[RU]** Автоматизация утренних уведомлений о погоде с «душевными» комментариями. Напомнит взять зонт или одеться как капуста 🧣, если на улице серьезный минус. | [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint URL.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FEugen417%2Fhomeassistant-blueprints%2Fblob%2Fmain%2Fweather_notification.yaml) |
| **Google Sheets Counters**| **[RU]** Шаблон для автоматизации передачи показаний счетчиков (ЖКУ) напрямую в Google Таблицы для ведения домашней бухгалтерии. | [![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint URL.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2FEugen417%2Fhomeassistant-blueprints%2Fblob%2Fmain%2Fkommunalnye_schetchiki_google_sheets.yaml) |

---

## 🚀 Как установить / How to install

**Способ 1 (Рекомендуемый):**
Нажмите кнопку **Import Blueprint** в таблице выше. Ваш Home Assistant откроет диалог импорта автоматически (требуется настроенный `my.home-assistant.io`).

**Способ 2 (Вручную):**
1. Откройте нужный файл в репозитории.
2. Скопируйте ссылку на этот файл.
3. Перейдите в Home Assistant: **Настройки** > **Автоматизации и сцены** > **Чертежи**.
4. Нажмите кнопку **Импортировать чертеж** и вставьте ссылку.

---

## ⚠️ Важное примечание / Important Note

> **[RU]** При редактировании описаний внутри YAML-файлов избегайте использования двоеточий (`:`) в тексте, так как это может вызвать ошибку парсинга.
>
> **[EN]** When editing descriptions inside YAML files, avoid using colons (`:`) in the text, as this may cause parsing errors.

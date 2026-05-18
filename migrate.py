# Базовая ссылка на твой репозиторий (ветка main)
BASE_RAW_URL = "https://raw.githubusercontent.com/Eugen417/homeassistant-blueprints/main/"

# Словарь миграции: "старый_файл.yaml" : "новая_папка/новый_файл.yaml"
migration_map = {
    # --- 🔋 Battery & Devices (Устройства и Питание) ---
    "Battery_Report_V3.4_EN.yaml": "automation/devices/Battery_Report_V3.4_EN.yaml",
    "Battery_Report_V3.4_RU.yaml": "automation/devices/Battery_Report_V3.4_RU.yaml",
    "z2m_offline_detection.yaml": "automation/devices/z2m_offline_detection.yaml",
    "restart_integration_if_device_state_unknown.yaml": "automation/system/restart_integration_if_device_state_unknown.yaml",
    "ha_ikea_matter_controller.yaml": "automation/devices/ha_ikea_matter_controller.yaml",
    
    # Скрипты Home Assistant обычно кладут в отдельную папку script/
    "script_battery_plus_tg_push_report.yaml": "script/script_battery_plus_tg_push_report.yaml",

    # --- ⛅ Weather (Погода) ---
    "weather_smart_telegram.yaml": "automation/weather/weather_smart_telegram.yaml",
    "weather_smart_3hr_meteoosadki_telegram-report.yaml": "automation/weather/weather_smart_3hr_meteoosadki_telegram-report.yaml",
    "weather_smart_3hr_meteoosadki_vk-report.yaml": "automation/weather/weather_smart_3hr_meteoosadki_vk-report.yaml",

    # --- 📊 Notifications & Data (Уведомления и Данные) ---
    "ya_st_alice_simple.yaml": "automation/media/ya_st_alice_simple.yaml",
    "kommunalnye_schetchiki_google_sheets.yaml": "automation/data/kommunalnye_schetchiki_google_sheets.yaml",
    "blood_pressure_to_google.yaml": "automation/data/blood_pressure_to_google.yaml",
    "video_push_notifi_ru.yaml": "automation/camera/video_push_notifi_ru.yaml",
    "photo_push_notifi_ru.yaml": "automation/camera/photo_push_notifi_ru.yaml",
    "new_waterleackdeteckt_tts_push_notifi.yaml": "automation/security/new_waterleackdeteckt_tts_push_notifi.yaml",
    "sensor_state_notify.yaml": "automation/notify/sensor_state_notify.yaml",

    # --- 💡 Lighting & Climate (Свет и Климат) ---
    "gtc_co2_fan_speed_on-off.yaml": "automation/climate/gtc_co2_fan_speed_on-off.yaml",
    "complex_light_control_ru.yaml": "automation/lighting/complex_light_control_ru.yaml",
    "swet_1.yaml": "automation/lighting/swet_1.yaml",
    "swet_2.yaml": "automation/lighting/swet_2.yaml",
    "yandex_double_gang_wireless_switch.yaml": "automation/lighting/yandex_double_gang_wireless_switch.yaml",

    # --- 🛡️ Security & Other (Безопасность и Трекинг) ---
    "person_tracker_RU.yaml": "automation/presence/person_tracker_RU.yaml",
    "vk_person_tracker.yaml": "automation/presence/vk_person_tracker.yaml",
    "cover_collision_protect.yaml": "automation/cover/cover_collision_protect.yaml"
}

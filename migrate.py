import os
import shutil
import re

# Базовая ссылка на твой репозиторий (ветка main)
BASE_RAW_URL = "https://raw.githubusercontent.com/Eugen417/homeassistant-blueprints/main/"

# Полный словарь миграции твоих файлов
migration_map = {
    # --- 🔋 Battery & Devices (Устройства и Питание) ---
    "Battery_Report_V3.4_EN.yaml": "automation/devices/Battery_Report_V3.4_EN.yaml",
    "Battery_Report_V3.4_RU.yaml": "automation/devices/Battery_Report_V3.4_RU.yaml",
    "z2m_offline_detection.yaml": "automation/devices/z2m_offline_detection.yaml",
    "restart_integration_if_device_state_unknown.yaml": "automation/system/restart_integration_if_device_state_unknown.yaml",
    "ha_ikea_matter_controller.yaml": "automation/devices/ha_ikea_matter_controller.yaml",
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

def update_source_url(file_path, new_url):
    """Находит и заменяет source_url в файле, сохраняя форматирование."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated_content = re.sub(
        r'source_url:\s*https://raw\.githubusercontent\.com/.*', 
        f'source_url: {new_url}', 
        content
    )
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

print("Начинаем миграцию блюпринтов...\n")

for old_file, new_path in migration_map.items():
    if not os.path.exists(old_file):
        print(f"⚠️ Файл {old_file} не найден, пропускаем.")
        continue

    # 1. Создаем новые папки
    new_dir = os.path.dirname(new_path)
    if new_dir:
        os.makedirs(new_dir, exist_ok=True)
        
    # 2. Копируем файл 
    shutil.copy2(old_file, new_path)
    print(f"✅ Скопирован: {old_file} -> {new_path}")
    
    # Формируем новую ссылку
    new_raw_url = BASE_RAW_URL + new_path
    
    # 3. Обновляем ссылки в обоих файлах
    update_source_url(new_path, new_raw_url)
    update_source_url(old_file, new_raw_url)

print("\n🎉 Миграция успешно завершена!")
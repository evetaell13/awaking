init python:
    # настройки ===========================================================================
    config.automatic_images_minimum_components = 1 ### минимальное количество тегов
    config.automatic_images = [' ', '_', '/'] ### список разделителей для создания тегов
    config.automatic_images_strip = ["images", "char", "bg", "ava", "panorama", "interface", "dreamora", "phone"] ### здесь через запятую можно указать и другие папки из директории game

    config.hard_rollback_limit = 0
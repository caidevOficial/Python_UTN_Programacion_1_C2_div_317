def ordenar_quick_por(videos: list[dict], key: str, modo: str = 'ASC') -> list[dict]:

    if len(videos) < 2:
        return videos
    
    pivot = videos.pop()

    mas_grandes = []
    mas_chicos = []

    for video in videos:
        if video.get(key) > pivot.get(key):
            mas_grandes.append(video)
        else:
            mas_chicos.append(video)
    
    if modo == 'ASC':
        return ordenar_quick_por(mas_chicos, key, modo) + [pivot] + ordenar_quick_por(mas_grandes, key, modo)
    else:
        return ordenar_quick_por(mas_grandes, key, modo) + [pivot] + ordenar_quick_por(mas_chicos, key, modo)

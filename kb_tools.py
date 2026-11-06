from kb_data import KB

def get_entity(entity_id: str):
    if entity_id in KB:
        return KB[entity_id]
    else:
        return f"Записи с идентификатором '{entity_id}' не существует в базе знаний."

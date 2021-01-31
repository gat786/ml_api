import validators

def validate(str:str) -> bool:
    try:
        if validators.url(str):
            return True
    except:
        return False
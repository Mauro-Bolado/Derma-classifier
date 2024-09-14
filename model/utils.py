def get_last_name(path: str) -> str:
    names = path.split('\\')
    return names[-1]

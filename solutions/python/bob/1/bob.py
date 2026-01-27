def response(hey_bob: str):
    striped = hey_bob.strip()
    is_question = striped.endswith("?")
    is_yelling = striped.isupper()
    is_silence = striped == ""
    if is_question:
        return "Calm down, I know what I'm doing!" if is_yelling else "Sure."
    if is_silence:
        return "Fine. Be that way!"
    if is_yelling:
        return "Whoa, chill out!"
    return "Whatever."

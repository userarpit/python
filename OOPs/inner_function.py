def speak(volumn):
    def whisper(text):
        return text.lower()
    
    def yell(text):
        return text.upper()
    
    if volumn < 0.5:
        return whisper
    else:
        return yell
    
func = speak(0.6)
print(func("hi"))
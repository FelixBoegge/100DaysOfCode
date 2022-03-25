def look_and_say(data, maxlen):
    result = []
    for x in range(maxlen):
        current = ""
        current_char = ""
        count = 0
        for i in range(len(data)):
            if data[i] == current_char:
                count += 1
            else:
                if i > 0:
                    current += str(count)+current_char
                current_char = data[i]
                count = 1
        current += str(count)+current_char
        result.append(current)
        data = current
    return result

print(look_and_say('1', 5))

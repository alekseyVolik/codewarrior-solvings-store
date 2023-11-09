"""kata id: https://www.codewars.com/kata/59437bd7d8c9438fb5000004"""


def alphabet_war(battlefield: str) -> str:
    health: int = 0 if '#' in battlefield else 1
    last_deleted = False
    b_health = health
    sentence = []
    current_buffer = []
    for alpha in battlefield:
        if alpha.isalpha() and health > 0:
            current_buffer.append(alpha)
        elif alpha == '[':
            if current_buffer:
                sentence.append((''.join(current_buffer), health))
            health += 2
            current_buffer = []
        elif alpha == ']':
            if current_buffer:
                sentence.append((''.join(current_buffer), health))
            health = b_health
            current_buffer = []
            last_deleted = False
        elif alpha == '#':
            health -= 1
            last_buffer = sentence[-1] if sentence else None
            if last_buffer and last_buffer[1] + health <= 0 and last_deleted is False:
                last_deleted = True
                sentence.pop()
    else:
        if current_buffer:
            sentence.append((''.join(current_buffer), health))
    return ''.join((''.join(s[0]) for s in sentence))

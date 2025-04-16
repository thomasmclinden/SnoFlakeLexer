import re

KEYWORDS = {
    'truefalse': 'bool',
    'integer': 'int',
    'character': 'char',
    'nonchanging': 'const',
    'stoploop': 'break',
    'option': 'case',
    'none': 'void',
}

def tokenize(code):
    return re.findall(r'".*?"|\'.*?\'|\w+|[^\s\w]', code)

def transpile(tokens):
    transpiled = []
    i = 0
    while i < len(tokens):
        token = tokens[i]

        # Handle 'say'
        if token == 'say':
            output = 'std::cout'
            i += 1
            while i < len(tokens) and tokens[i] != ';':
                if tokens[i] == 'endl':
                    output += ' << std::endl'
                else:
                    output += f' << {tokens[i]}'
                i += 1
            output += ';'
            transpiled.append(output)
            i += 1  # skip the semicolon
            continue

        transpiled.append(KEYWORDS.get(token, token))
        i += 1

    return ' '.join(transpiled)

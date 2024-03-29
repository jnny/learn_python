def boxPrint(symbol, width, height):

    if len(symbol) != 1:
        raise Exception('"symbol" needs to be one character.')

    if (width < 2) or (height < 2):
        raise Exception('"width" and "heigh" must be greater than or equal to 2.')

    print(symbol * width)
    
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxPrint('*', 15, 5)

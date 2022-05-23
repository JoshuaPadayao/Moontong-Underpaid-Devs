def set_language():
    global lang, lang_ext, lang_data

    cprint('\nCHOOSE YOUR LANGUAGE (hit "enter" for default [English]):', 'green')
    for i in range(len(languages)):
        print(i+1, end='')
        print(". " + str(languages[i]['name']))

    lang = 0
    while not lang:
        try:
            lang = int(input('>>> ').strip())
            if lang not in range(1,len(languages)+1):
                raise ValueError
        except ValueError:
            if not lang:
                break
            else:
                lang = 0
                cprint("That's not an option!", "red")

    if lang == 1 or not lang:
        lang = 0
    else:
        lang = lang - 1 
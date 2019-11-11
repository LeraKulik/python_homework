импорт ре
re_float = re.compile ( " ^ [- +] {0,1} \ d + \. {0,1} \ d + $ " )


 валидатор def ( pattern , promt ):
    текст =  ввод (Promt)
    пока  не  bool (pattern.match (текст)):
        текст =  ввод (Promt)
    вернуть текст

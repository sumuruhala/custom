def util_get_cursor_point(self_view):
    region = self_view.sel()[0]
    return region.b

def util_get_cursor_rowcol(self_view):
    point = util_get_cursor_point(self_view)
    return self_view.rowcol(point)

def util_set_cursor_point(self_view, point):
    selec = self_view.sel()
    if len(selec) <= 0:
        return False

    region = selec[0]
    region.a, region.b = point, point
    selec.clear()
    selec.add(region)
    return True

def util_set_cursor_rowcol(self_view, row, col):
    point = self_view.text_point(row, col)
    return util_set_cursor_point(point)
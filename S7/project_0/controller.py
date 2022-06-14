
import user_interface as ui
import calc as c
import log


def button_click():
    value_a = ui.get_value()
    value_b = ui.get_value()
    value_c = ui.get_value()
    value_d = ui.get_value()
    do = ui.get_sign()

    c.init(value_a, value_b, value_c, value_d)
    if do == '+':
        result = c.sum()
    if do == '-':
        result = c.sub()
    if do == '*':
        result = c.mult()
    if do == '/':
        result = c.div()

    ui.view_data(f'{c.x} {do} {c.y} = {result}')
    log.logger(c.x, do, c.y, result)


import flet as ft
def main(page: ft.Page):
    page.title = "El Pizza Maker"
    pizza_base = ft.Image(src = "pizzabase.png", width = 300, height = 300)
    pepperoni = ft.Image(src = "pepperoni.png", width = 300, height = 300)
    sausage = ft.Image(src = "sausage.png", width = 300, height = 300)
    bell_peppers = ft.Image(src = "bellpepper.png", width = 300, height = 300)
    pizza_stack = ft.Stack(controls = [pizza_base], width = 300, height = 300)

    def update_pizza(e):
        if pepperoni_switch.value:
            if pepperoni not in pizza_stack.controls:
                pizza_stack.controls.append(pepperoni)
        else:
            if pepperoni in pizza_stack.controls:
                pizza_stack.controls.remove(pepperoni)
        if sausage_switch.value:
            if sausage not in pizza_stack.controls:
                pizza_stack.controls.append(sausage)
        else:
            if sausage in pizza_stack.controls:
                pizza_stack.controls.remove(sausage)
        if bell_peppers_switch.value:
            if bell_peppers not in pizza_stack.controls:
                pizza_stack.controls.append(bell_peppers)
        else:
            if bell_peppers in pizza_stack.controls:
                pizza_stack.controls.remove(bell_peppers)
        page.update()

    pepperoni_switch = ft.Switch(label = "Pepperoni", on_change = update_pizza)
    sausage_switch = ft.Switch(label = "Sausage", on_change = update_pizza)
    bell_peppers_switch = ft.Switch(label = "Bell Peppers", on_change = update_pizza)
    page.add(ft.Text("Make tu propia Pizza!", size = 30, weight = "bold"), pizza_stack, ft.Column([pepperoni_switch, sausage_switch, bell_peppers_switch]))

ft.app(target = main)
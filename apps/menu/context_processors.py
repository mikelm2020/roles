from .models import Menu, OptionMenu


def menu_context_processor(request):
    if request.user.is_authenticated and hasattr(request.user, "role"):
        # Obtener los menús que corresponden al rol del usuario.
        role_menus = request.user.role.menu.all()
    else:
        # Si el usuario no está autenticado o no tiene rol, no mostramos menús o mostramos menús por defecto.
        role_menus = Menu.objects.none()

    menu_dict = {}
    for menu in role_menus:
        options = OptionMenu.objects.filter(menu=menu).order_by("id")
        menu_dict[menu] = options
        print(f"Debug: Opciones del menú {menu.name}: {list(options)}")
        # menu_dict[menu] = OptionMenu.objects.filter(menu=menu).order_by("id")
    return {"menus": menu_dict}

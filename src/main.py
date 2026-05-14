from src.views import *


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    dani = read_json()
    dani["user_authorized"] = False
    dani["current_user"] = ""
    save_json(dani)

    def route_change():
        page.views.clear()

        if page.route == "/" or page.route == "/home":
            page.views.append(HomeView())

        elif page.route == "/login":
            page.views.append(LoginView())

        elif page.route == "/register":
            page.views.append(RegisterView())

        elif page.route == "/notes":
            page.views.append(NotesView(page))

        elif page.route == "/profile":
            page.views.append(ProfileView(page))

        elif page.route == "/fishing_weather":
            page.views.append(FishingWeatherViews())

        elif page.route == "/encyclopedia":
            page.views.append(EncyclopediaView())
        page.update()

    async def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            await page.push_route(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    route_change()


ft.run(main, view=ft.AppView.WEB_BROWSER)
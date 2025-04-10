import reflex as rx
from ..styles import styles

def experience() -> rx.Component:
    return rx.center(
        rx.section(
            rx.vstack(
                rx.hstack(
                    rx.heading(
                        "Experiencia",
                        size=rx.breakpoints(
                            initial="6",
                            sm="7",
                            lg="8"
                        ),
                        weight="bold",
                        as_="h2"
                    ),
                    justify="center",
                    width="100%",
                ),
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.text("Arlexdev",size="4",color_scheme="gray"),
                            rx.image(
                                src="/icons/arlexdev.svg",
                                width="40px",
                                height="auto",
                                border_radius="50%",
                                alt="Logo Arlexdev"
                            ),
                            justify="between",
                            align="center",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text("Founder | Software Developer",size="5",weight="bold"),
                            rx.cond(
                                "Feb. 2024 - actualidad" != "",
                                rx.badge("Feb. 2024 - Actualidad",
                                    #color=rx.color("cyan", 9),
                                    color_scheme="gray",
                                    size="3"
                                ),
                            ),
                            rx.unordered_list(
                                rx.list_item("Desarrollo Web"),
                                rx.list_item("Desarrollo de Software"),
                                color=rx.color("gray",11)
                            ),
                            width="100%"
                        ),
                        spacing="4",
                        width="100%"
                    ),
                    padding=rx.breakpoints(
                        initial="1.5em",
                        sm="2.5em",
                        lg="3.5em"
                    ),
                    border="1px solid #2A2A2A",
                    border_radius="12px",
                    width="100%",
                    #bg="#111111"
                ),
                rx.box(
                    rx.vstack(
                        rx.hstack(
                            rx.text("Mi Teleférico",size="4",color_scheme="gray"),
                            rx.image(
                                src="/icons/logo_mi_teleferico.svg",
                                width="40px",
                                height="auto",
                                border_radius="50%",
                                alt="Logo Mi Teleférico"
                            ),
                            justify="between",
                            align="center",
                            width="100%"
                        ),
                        rx.vstack(
                            rx.text("Software Development Internship",size="5", weight="bold"),
                            rx.vstack(
                                rx.cond(
                                    "Jul. 2023 - Ene.2024" != "",
                                    rx.badge(
                                        "Jul. 2023 - Ene. 2024",
                                        #color=rx.color("cyan", 9),
                                        color_scheme="gray",
                                        size="3"
                                    )
                                ),
                                align="end"
                            ),
                            rx.unordered_list(
                                rx.list_item("Brindé soporte técnico a los usuarios de la aplicación Yala."),
                                rx.list_item("Administré y realicé mejoras en la página web de la empresa."),
                                rx.list_item("Apoyé a los usuarios del sistema de Recursos Humanos."),
                                rx.list_item("Elaboré y optimicé manuales de sistemas informáticos."),
                                rx.list_item("Desarrollé nuevas funcionalidades para los sistemas internos de la empresa."),
                                color=rx.color("gray",11)
                            ),
                            width="100%"
                        ),
                        #flex_direction=["column-reverse", "row"],
                        spacing="4",
                        width="100%"
                    ),
                    padding=rx.breakpoints(
                        initial="1.5em",
                        sm="2.5em",
                        lg="3.5em"
                    ),
                    border="1px solid #2A2A2A",
                    border_radius="12px",
                    width="100%",
                    #bg="#111111"
                ),
                margin=rx.breakpoints(
                    initial="1.5em",
                    sm="2.5em",
                    lg="3.5em"
                ),
                spacing="8"
            ),
            style=styles.max_width_style,
            width="100%",
            size="2",
            id="experiencia",
        ),
        width="100%"
    )

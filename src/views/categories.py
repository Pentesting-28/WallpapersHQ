import flet as ft
from core.widgets import Carousel

carousel_images = list(
    [
        "https://cookinglsl.com/wp-content/uploads/2019/02/chocolate-dipped-strawberries-wide-1.jpg",
        "https://cdn.shopify.com/s/files/1/2305/2515/products/IMG_0746_3024x.jpg",
        "https://www.coleinthekitchen.com/wp-content/uploads/2022/11/Small-Charcuterie-Board-6.jpg",
        "https://media-cldnry.s-nbcnews.com/image/upload/newscms/2021_18/1712998/strawberry-shortcake-kb-main-210505.jpg"
    ]
)

def debugging_view(page: ft.Page):
    return Carousel(carousel_images, shuffle=True)
 
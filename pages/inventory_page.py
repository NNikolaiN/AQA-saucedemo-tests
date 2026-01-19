from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.title_span = page.locator("span.title")
        self.inventory_items = page.locator(".inventory_item") 
        self.cart_icon = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator(".product_sort_container")
    
    def is_loaded(self) -> bool:
    
        try:
            expect(self.title_span).to_be_visible(timeout=10000)
            expect(self.title_span).to_have_text("Products", timeout=5000)
            
            # Проверяем наличие хотя бы одного товара
            items_count = self.inventory_items.count()
            if items_count < 1:
                return False
                
            return True
        except:
            return False
    
    def get_title(self) -> str:
        return self.title_span.inner_text()
    
    def is_cart_visible(self) -> bool:
        return self.cart_icon.is_visible()
    
    def get_items_count(self) -> int:
        return self.inventory_items.count()
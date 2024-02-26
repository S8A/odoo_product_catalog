from odoo import http


class ProductCatalogController(http.Controller):

    @http.route("/s8a/product_catalog", auth="public", website=True)
    def product_catalog(self, **kwargs):
        products = http.request.env["product.template"].sudo().search([])
        context = {
            "products": products,
        }
        return http.request.render("s8a_product_catalog.product_catalog", context)

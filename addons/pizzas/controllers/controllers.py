# -*- coding: utf-8 -*-
# from odoo import http


# class Pizzas(http.Controller):
#     @http.route('/pizzas/pizzas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pizzas/pizzas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pizzas.listing', {
#             'root': '/pizzas/pizzas',
#             'objects': http.request.env['pizzas.pizzas'].search([]),
#         })

#     @http.route('/pizzas/pizzas/objects/<model("pizzas.pizzas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pizzas.object', {
#             'object': obj
#         })

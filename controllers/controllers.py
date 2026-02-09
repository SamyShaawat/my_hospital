# -*- coding: utf-8 -*-
# from odoo import http


# class MyHospital(http.Controller):
#     @http.route('/my_hospital/my_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_hospital/my_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_hospital.listing', {
#             'root': '/my_hospital/my_hospital',
#             'objects': http.request.env['my_hospital.my_hospital'].search([]),
#         })

#     @http.route('/my_hospital/my_hospital/objects/<model("my_hospital.my_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_hospital.object', {
#             'object': obj
#         })


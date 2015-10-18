# -*- coding: utf-8 -*-
from openerp import http

# class Mediatek(http.Controller):
#     @http.route('/mediatek/mediatek/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mediatek/mediatek/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mediatek.listing', {
#             'root': '/mediatek/mediatek',
#             'objects': http.request.env['mediatek.mediatek'].search([]),
#         })

#     @http.route('/mediatek/mediatek/objects/<model("mediatek.mediatek"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mediatek.object', {
#             'object': obj
#         })